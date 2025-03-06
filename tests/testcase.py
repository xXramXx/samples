from cod.calc import add, sub

def test_add():
    assert add(3,3) == 6
    assert add(22,-11) == 11

def test_sub():
    assert sub(3, +3) == 0
    assert sub(22, 11) == 11