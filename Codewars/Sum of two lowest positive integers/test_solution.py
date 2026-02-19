from solution import sum_two_smallest_numbers

def test_fixed_1():
    assert sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]) == 3453455

def test_fixed_2():
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13

def test_fixed_3():
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19

def test_fixed_4():
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30