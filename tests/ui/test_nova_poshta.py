import pytest
from modules.ui.page_objects.nova_poshta_page import NovaPoshtaPage


@pytest.mark.ui
def test_search_valid_tracking_number():
    # Створення об'єкту сторінки
    nova_poshta_page = NovaPoshtaPage()

    # Пошук посилки з валідним номером
    valid_tracking_number = '20450680973761'
    result_text = nova_poshta_page.search_parcel(valid_tracking_number)
    print(result_text)
    # Перевірка, що результат пошуку містить номер посилки
    assert result_text == "Посилка отримана"

    # Перевірка, що повідомлення про пошук з'явилося на сторінці
    assert nova_poshta_page.is_tracking_info_displayed(), "Повідомлення про пошук не з'явилося на сторінці"






    

    
  
