import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachine import STAGE
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

@pytest.fixture
def machine1():
    bm1 = BurgerMachine()
    return bm1

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("veggie")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    first_order.handle_pay(10000,"10000")
    return first_order



# add required test cases below

#UCID: av659
#Date: 02/20/23

def test_first_selection(machine):
    assert machine.currently_selecting.name == STAGE.Bun.name

#UCID: av659
#Date: 02/20/23
def test_patty_in_stock(machine):
    machine.patties[0].quantity = 1
    machine.handle_bun("no bun")
    machine.handle_patty("beef")
    try:
        machine.handle_patty("beef")
        assert machine.patties[0].quantity == 1
    except OutOfStockException:
        assert False

#UCID: av659
#Date: 02/20/23
def test_toppings_in_stock(machine):
    machine.toppings[0].quantity = 1
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("next")
    machine.handle_toppings("tomato")
    try:
        machine.handle_toppings("tomato")
        assert machine.toppings[0].quantity == 1
    except OutOfStockException:
        assert False

#UCID: av659
#Date: 02/20/23
def test_max_patties(machine):
    machine.handle_bun("white burger bun")
    for patty in range(machine.MAX_PATTIES - 1):
        machine.handle_patty("beef")
    try:
        machine.handle_patty("beef")
        assert machine.remaining_patties == 0
    except ExceededRemainingChoicesException:
        assert False

#UCID: av659
#Date: 02/20/23
def test_max_toppings(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("next")
    # loop to choose (maximum - 1) number of toppings
    for topping in range(machine.MAX_TOPPINGS - 1):
        machine.handle_toppings("bbq")
    try:
        machine.handle_toppings("bbq")
        assert machine.remaining_toppings == 0
    except ExceededRemainingChoicesException:
        assert False

#UCID: av659
#Date: 02/20/23
def test_total_cost(machine1):
    machine1.reset()
    machine1.handle_bun("wheat burger bun")
    machine1.handle_patty("veggie")
    machine1.handle_patty("turkey")
    machine1.handle_patty("next")
    machine1.handle_toppings("bbq")
    machine1.handle_toppings("ketchup")
    machine1.handle_toppings("tomato")
    machine1.handle_toppings("done")
    assert machine1.calculate_cost() == '4.00'
    

    machine1.reset()
    machine1.handle_bun("white burger bun")
    machine1.handle_patty("beef")
    machine1.handle_patty("next")
    machine1.handle_toppings("mayo")
    machine1.handle_toppings("ketchup")
    machine1.handle_toppings("pickles")
    machine1.handle_toppings("done")
    assert machine1.calculate_cost() == '2.75'
    

    machine1.reset()
    machine1.handle_bun("no bun")
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("bbq")
    machine1.handle_toppings("mustard")
    machine1.handle_toppings("cheese")
    machine1.handle_toppings("done")
    assert machine1.calculate_cost() == '1.75'
    


#UCID: av659
#Date: 02/20/23
def test_total_sales(machine1):
    machine1.handle_bun("white burger bun")
    machine1.handle_patty("veggie")
    machine1.handle_patty("beef")
    machine1.handle_patty("next")
    machine1.handle_toppings("mayo")
    machine1.handle_toppings("done")
    burgerCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost1, str(burgerCost1))

    machine1.handle_bun("wheat burger bun")
    machine1.handle_patty("beef")
    machine1.handle_patty("next")
    machine1.handle_toppings("pickles")
    machine1.handle_toppings("done")
    burgerCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost2, str(burgerCost2))
    
    machine1.handle_bun("no bun")
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("bbq")
    machine1.handle_toppings("mustard")
    machine1.handle_toppings("cheese")
    machine1.handle_toppings("done")
    burgerCost3 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost3, str(burgerCost3))

    assert machine1.total_sales == burgerCost1 + burgerCost2 + burgerCost3


#UCID: av659
#Date: 02/20/23
def test_total_burgers(second_order, machine1):
    machine1.handle_bun("no bun")
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("done")
    burgerCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost1, str(burgerCost1))

    machine1.handle_bun("Wheat burger bun")
    machine1.handle_patty("next")
    machine1.handle_toppings("mustard")
    machine1.handle_toppings("done")
    burgerCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost2, str(burgerCost2))

    machine1.handle_bun("White burger bun")
    machine1.handle_patty("next")
    machine1.handle_toppings("ketchup")
    machine1.handle_toppings("done")
    burgerCost3 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost3, str(burgerCost3))

    assert second_order.total_burgers == 2 and machine1.total_burgers == 3