from evenodd import check_even_odd

def test_evennumbers():
    assert check_even_odd(4) == "even"
    assert check_even_odd(2) == "even"
    assert check_even_odd(8) == "even"

def test_odd_numbers():
    assert check_even_odd(3) == "odd"
    assert check_even_odd(9) == "odd"
    assert check_even_odd(13) == "odd"
