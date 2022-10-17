from Menu import Menu
from MenuRepository import MenuRepository
from UserInterface import UserInterface
from Order import Order

def test_set_menu_item():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    menu2 = Menu(2, "Test 2", 5)
    menu3 = Menu(3, "Test 3", 2)

    # Act
    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    # Assert
    assert len(menu_repository.menu_itens) == 2
    assert not menu3 in menu_repository.menu_itens
    assert type(menu_repository.menu_itens) == list


def test_check_if_itens_exists():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)

    # Act
    menu_repository.set_menu_item(menu1)
    resultOK = menu_repository.check_if_itens_exists(Order(1, 10))

    # Assert
    assert len(menu_repository.menu_itens) == 1
    assert resultOK == True


 #-------------- test get user input and test_get total price ----------------#

def test_get_user_input():
    result = "1 10".split(" ")
    request = Order(int(result[0]), int(result[1]))

    assert type(request) == Order


def test_get_total_price():
    item = (4, "Hot dog", 2.00)

    menu = MenuRepository()
    menu.get_total_price(Order)
    order = Order(1, 10)

    total = item[2] * order.quantity

    assert total == 20


