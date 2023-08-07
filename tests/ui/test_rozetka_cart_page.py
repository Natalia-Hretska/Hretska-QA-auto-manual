import pytest
from modules.ui.page_objects.rozetka_cart_page import RozetkaCartPage



@pytest.mark.ui
def test_is_cart_empty(rozetka_cart_page):
    # Go to the cart page
    rozetka_cart_page.go_to_rozetka()

    # Check if the cart is empty
    is_empty = rozetka_cart_page.is_cart_empty()

    # Perform an assertion to check if the cart is empty
    assert is_empty, "The cart is not empty"

@pytest.mark.ui
def test_add_single_item_to_cart(rozetka_cart_page):
    
    item_name = "Ложка для мороженого Ardesto Gemini, сірий/синій, нейлон, пластик із софт тач" 
    rozetka_cart_page.go_to_rozetka()

    # Add a single item to the cart
    rozetka_cart_page.add_item_to_cart(item_name)

    # Verify that the item was added to the cart
    assert rozetka_cart_page.is_item_added_to_cart(item_name), f"Failed to add item: {item_name}"

   
@pytest.mark.ui
def test_add_multiple_items_to_cart(rozetka_cart_page):
    
    # Add multiple items to the cart
    #rozetka_cart_page.go_to_rozetka()
    item_names = ["Ложка Gefu Primeline для морозива 20 см (29220)", "Набір із шести ложок для морозива Frico L-SPN-S", "Набір довгих ложок десертних 4шт для коктейлю, морозива, смузі, льоду 22,5см"]  # Replace with actual product names
    rozetka_cart_page.add_multiple_item_to_cart(item_names)
    
    #for item_name in item_names:
    #    rozetka_cart_page.go_to_rozetka()
    #    rozetka_cart_page.add_item_to_cart(item_name)

    # Verify that all items were added to the cart
    for item_name in item_names:
        assert rozetka_cart_page.is_item_added_to_cart(item_name), f"Failed to add item: {item_name}"

@pytest.mark.ui 
def test_get_cart_item_price(rozetka_cart_page):
    item_name = "Ложка Gefu Primeline для морозива 20 см (29220)"  # Replace with an actual product name##
    # Add the item to the cart
    rozetka_cart_page.go_to_rozetka()
    rozetka_cart_page.add_item_to_cart(item_name)##
    # Retrieve the item price from the cart
    item_price = rozetka_cart_page.get_cart_item_price(item_name)#
    # Perform an assertion to check if the item price is not None (i.e., the item was found in the cart)
    assert item_price is not None, f"Item '{item_name}' not found in the cart"



@pytest.mark.ui
def test_cart_item_count(rozetka_cart_page):
    # ... Test implementation for verifying the number of items in the cart
     # Add multiple items to the cart
    item_names = ["Ложка для морозива ", "Набір із шести ложок для морозива Frico", "Набір довгих ложок десертних 4шт для коктейлю"]
    for item_name in item_names:
        rozetka_cart_page.add_item_to_cart(item_name)
        
    # Retrieve the count of items in the cart
    actual_item_count = rozetka_cart_page.get_cart_item_count()
    #print(actual_item_count)#
    # Perform an assertion to check if the count matches the expected number of items
    expected_item_count = len(item_names)
    assert actual_item_count == expected_item_count, f"Expected {expected_item_count} items in the cart, but found {actual_item_count}"
#
  