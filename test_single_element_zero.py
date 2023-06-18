def test_single_element_zero():
    arr = [0, 1, 2, 3, 4, 2, 3, 1, 0]
    assert find_single_element(arr) == 4
