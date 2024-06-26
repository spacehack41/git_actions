from testingci.my_math import add,mult,sub

def test_add():
    assert add(2,3) == 5
    assert add(2,2) == 4


def test_mult():
    assert mult(5,5) == 25
    assert mult(2,10) == 20

def test_sub():
    assert sub(10,10) == 0
    assert sub(30,25) == 5
    assert sub(25,30) == -5
