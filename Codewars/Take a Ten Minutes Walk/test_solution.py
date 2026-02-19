from solution import is_valid_walk

def test_should_return_true_for_a_valid_walk():
    assert is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) is True

def test_should_return_false_if_walk_is_too_long():
    assert is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) is False

def test_should_return_false_if_walk_is_too_short():
    assert is_valid_walk(['w']) is False

def test_should_return_false_if_walk_does_not_bring_you_back_to_start():
    assert is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) is False