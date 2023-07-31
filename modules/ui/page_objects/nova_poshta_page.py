from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NovaPoshtaPage(BasePage):
    
    URL = "https://novaposhta.ua/"
        
    def __init__(self) -> None:
        super().__init__()

     # Відкриваємо сторінку Нової Пошти
    def search_parcel(self, tracking_number):
        self.driver.get(NovaPoshtaPage.URL)
    
     #Закриваємо popup_mask, якщо він є на сторінці
        try:
            popup_close_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[5]/div[1]/i")
            popup_close_btn.click()

        except NoSuchElementException:
            pass
       
                
        # Знаходимо поле для введення номера накладної
        search_box = self.driver.find_element(By.ID, 'cargo_number')
        search_box.clear()
        search_box.send_keys(tracking_number)  # Вводимо номер накладної в поле вводу
       
        # Знаходимо кнопку пошуку
        search_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[1]/div/div[2]/form/input[2]")
        
        # Натискаємо кнопку пошуку
        search_button.click() 
        
        #Закрити Зрозуміло
        try:   
            understand_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/main/section/div/div/div[1]/div/div/div[2]/button"))
            )
            understand_button.click()
        except NoSuchElementException:
            pass


        # Очікуємо завершення пошуку та отримуємо результати
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/main/section/div/div/div[1]"))
            )
            result_element = self.driver.find_element(By.CLASS_NAME, "header__status-text")
            return result_element.text
        except NoSuchElementException:
            return None
                   
 
    def is_tracking_info_displayed(self):
        try:
            # Використовуємо WebDriverWait для перевірки, чи з'явилася інформація про поштове відправлення
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__status-text")))
            return True
        except TimeoutException:
            return False
        
    