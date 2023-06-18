def test_single_element_negative():
    arr = [-1, 2, 3, -1, 2, 4, 3, 4]
    assert find_single_element(arr) == -5
