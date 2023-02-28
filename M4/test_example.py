import pytest
from MyCalc import MyCalc

#Defining pytest fixtures 
@pytest.fixture
def calc():
    return MyCalc()

# Test cases
def test_number_add_number():
    calc = MyCalc()
    assert calc.add(2,2) == 4
    assert calc.add(3,3) == 6
    assert calc.add(1,-5) == -4
#Ucid : av659
#Date : 02/22/23
#Summary : Performing addition while taking two different integers and then aseerting the values
#This checks in pytest if it passes.

def test_ans_add_number():
    calc = MyCalc()
    assert calc.add(7,3) == 10
    assert calc.add(10,calc.ans) == 20
    assert calc.add(calc.ans,-7) == 13
#Ucid : av659
#Date : 02/22/23
#Summary : Performing addition while taking two different integers and then aseerting the values
#The latest answer is taken as one of a valid integer and performing aseertion.
#This checks in pytest if it passes.

def test_number_sub_number():
    calc = MyCalc()
    assert calc.subtract(10,9) == 1
    assert calc.subtract(-9,-8) == -1
    assert calc.subtract(3,-2) == 5
#Ucid : av659
#Date : 02/22/23
#Summary : Performing subtraction while taking two different integers and then aseerting the values
#This checks in pytest if it passes.

def test_ans_sub_number():
    calc = MyCalc()
    assert calc.subtract(15,12) == 3
    assert calc.subtract(calc.ans,-1) == 4
    assert calc.subtract(calc.ans,3) == 1
#Ucid : av659
#Date : 02/22/23
#Summary : Performing subtraction while taking two different integers and then aseerting the values
#The latest answer is taken as one of a valid integer and performing aseertion.
#This checks in pytest if it passes.

def test_number_mult_number():
    calc = MyCalc()
    assert calc.multiply(5,6) == 30
    assert calc.multiply(4,-8) == -32
    assert calc.multiply(-18,1) == -18
#Ucid : av659
#Date : 02/22/23
#Summary : Performing multiplication while taking two different integers and then aseerting the values
#This checks in pytest if it passes.

def test_ans_mult_number():
    calc = MyCalc()
    assert calc.multiply(10,2) == 20
    assert calc.multiply(calc.ans,-12) == -240
    assert calc.multiply(1,calc.ans) == -240
#Ucid : av659
#Date : 02/22/23
#Summary : Performing multiplication while taking two different integers and then aseerting the values
#The latest answer is taken as one of a valid integer and performing aseertion.
#This checks in pytest if it passes.


def test_number_div_number():
    calc = MyCalc()
    assert calc.divide(14,2) == 7
    assert calc.divide(30,-1) == -30
    assert calc.divide(-54,-6) == 9
#Ucid : av659
#Date : 02/22/23
#Summary : Performing division while taking two different integers and then aseerting the values
#This checks in pytest if it passes.


def test_ans_div_number():
    calc = MyCalc()
    assert calc.divide(90,2) == 45
    assert calc.divide(calc.ans,-1) == -45
    assert calc.divide(-45,calc.ans) == 1
#Ucid : av659
#Date : 02/22/23
#Summary : Performing division while taking two different integers and then aseerting the values
#The latest answer is taken as one of a valid integer and performing aseertion.
#This checks in pytest if it passes.

