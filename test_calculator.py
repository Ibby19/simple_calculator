from calculator import add, multiply

def test_addition():
    result = add(0,0)
    assert result == 0

    result = add(-1,-1)
    assert result == -2

    result = add(4,5)
    assert result == 9

def test_multiple_nums_addition():
    result = add(1,2,3,4)
    assert result == 10

def test_multiplication():
    result = multiply(1,2)
    assert result == 2

    result = multiply(3,2)
    assert result == 6

    result = multiply(5,2)
    assert result == 10

def test_multiply_multiple_nums():
    result = multiply(1,2,3,4)
    assert result == 24

    result = multiply(1,3,5,7,9)
    assert result == 945

    result = multiply(1,1,3,3,4,4)
    assert result == 144