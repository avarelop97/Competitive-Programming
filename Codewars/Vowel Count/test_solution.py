from solution import get_count

def test_all_vowels():
    assert get_count("aeiou") == 5

def test_only_y():
    assert get_count("y") == 0

def test_no_vowels():
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0

def test_empty_string():
    assert get_count("") == 0

def test_abracadabra():
    assert get_count("abracadabra") == 5