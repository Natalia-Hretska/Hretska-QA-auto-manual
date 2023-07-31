import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(database):
    database.test_connection() 


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'
    

@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1, 25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25
    


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4,'печиво', 'солодке', 30)
    cookies_qnt = database.select_product_qnt_by_id(4)

    assert cookies_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99,'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] ==1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром' 

@pytest.mark.database
def test_product_insert_with_negative_qnt(database):
    database.insert_product(5,'печиво', 'солодке', -30)
    cookies_qnt = database.select_product_qnt_by_id(5)

    assert cookies_qnt[0][0] == -30



@pytest.mark.database
def test_negative_quantity_not_allowed(database):
    
    with pytest.raises(Exception) as e:
        database.insert_product(5, "Product B", "Description B", -5)

    assert "CHECK constraint failed" in str(e.value)

