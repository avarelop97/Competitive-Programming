from solution import first_non_repeating_letter

def test_simple_cases():
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'

def test_empty_strings():
    assert first_non_repeating_letter('') == ''

def test_without_unique_characters():
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('aa') == ''

def test_exotic_characters():
    assert first_non_repeating_letter('~><#~><') == '#'
    assert first_non_repeating_letter('hello world, eh?') == 'w'

def test_letter_case_correctly():
    assert first_non_repeating_letter('sTreSS') == 'T'
    assert first_non_repeating_letter("Go hang a salami, I'm a lasagna hog!") == ','
    assert first_non_repeating_letter("Who is my widdle silly mopy doggy then?") == 'p'