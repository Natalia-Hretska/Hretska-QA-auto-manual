from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RozetkaCartPage(BasePage):
   
    URL = "https://rozetka.com.ua/"

    def __init__(self) -> None:
        super().__init__()

   
    def go_to_rozetka(self):
        self.driver.get(RozetkaCartPage.URL)
    

    def add_item_to_cart(self, item_name):
        # ... Implementation for adding item to cart
        search_box = self.driver.find_element(By.NAME, 'search')
        search_box.clear()
        search_box.send_keys(item_name)
                
        search_button =  WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-form__submit[_ngcontent-rz-client-c42]")))
        search_button.click()
        
        # Wait for the search results page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ng-star-inserted")))
                  
        # Wait for the "Add to cart" button to be clickable
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'goods-tile__buy-button'))
        )
        add_to_cart_button.click()             
   
    def is_item_added_to_cart(self, item_name):
        # ... Implementation for checking if the item is added to the cart
               
        # Wait for the cart modal to load (increase timeout if needed)
        cart_button = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'header__button ng-star-inserted')))
        cart_button.click()
        # Find the cart modal element
        cart_modal = self.driver.find_element(By.CLASS_NAME, 'cart-list__item ng-star-inserted')
         # Print the text of the cart modal
        print("Cart modal text:")
        print(cart_modal.text)

        #Check if the item name is present in the cart modal text
        if item_name in cart_modal.text:
            return item_name in cart_modal.text
            
    def get_cart_item_price(self, item_name):
         # Wait for the cart page to load
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,'modal__content')))

        # Find all cart items on the page
        cart_items = self.driver.find_elements(By.CLASS_NAME,'cart-list__item ng-star-inserted')

        # Loop through the cart items to find the item price
        for cart_item in cart_items:
            item_title = cart_item.find_element(By.CLASS_NAME, 'cart-product__title').text
            if item_title == item_name:
                # If the item is found, extract the price text
                item_price_element = cart_item.find_element(By.CLASS_NAME, 'product-price')
                return item_price_element.text
            
        return None
     


    def is_cart_empty(self):
       # ... Implementation for checking if the cart is empty
        cart_button = self.driver.find_element(By.CSS_SELECTOR, "body > app-root > div > div > rz-header > rz-main-header > header > div > div > ul > li.header-actions__item.header-actions__item--cart > rz-cart > button")
        cart_button.click()
        # Wait for the cart page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'modal__content')))
    
        # Find the element containing the cart items or the "empty cart" message
        cart_content_element = self.driver.find_element(By.CLASS_NAME, 'cart-dummy__heading')
    
        # Check if the element contains any cart items or the "empty cart" message
        if "Кошик порожній" in cart_content_element.text:
            return True
        else:
            return False
    

    def add_multiple_item_to_cart(self, item_names):
       
        for item_name in item_names:
            self.add_item_to_cart(item_name)
    

    def get_cart_item_count(self):
       # ... Implementation for retrieving the number of items in the cart
      # Go to the cart page
        cart_button = self.driver.find_element(By.CLASS_NAME, "header__button")
        cart_button.click()

       # Wait for the cart page to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'modal__content')))

       # Find all elements representing individual cart items
        cart_item_elements = self.driver.find_elements(By.CLASS_NAME, 'cart-modal__content .cart-product')

       # Return the count of cart item elements, which represents the number of items in the cart
        return len(cart_item_elements)
    #
    def clear_cart(self):
        # ... Implementation for removing all items from the cart
        
        # Go to the cart page
        cart_button = self.driver.find_element(By.CLASS_NAME, "header__button")
        cart_button.click()
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-modal__content')))
           # Find all elements representing individual cart items
        cart_item_elements = self.driver.find_elements(By.CLASS_NAME, 'cart-modal__content .cart-product')
           # Iterate through each cart item and remove it from the cart
        for cart_item in cart_item_elements:
            remove_button = cart_item.find_element(By.ID, 'cartProductActions0')
            remove_button.click()
        
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'empty-text'), 'Кошик порожній'))
        