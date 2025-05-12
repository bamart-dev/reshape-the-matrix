from main import reshape_matrix


def test_reshape_matrix_valid_case():
    nums = [[1, 2], [3, 4]]
    r, c = 1, 4
    expected = [[1, 2, 3, 4]]
    assert reshape_matrix(nums, r, c) == expected

def test_reshape_matrix_invalid_case():
    nums = [[1, 2], [3, 4]]
    r, c = 2, 3
    expected = [[1, 2], [3, 4]]  # Should return the original matrix
    assert reshape_matrix(nums, r, c) == expected

def test_reshape_matrix_single_row():
    nums = [[1, 2, 3, 4]]
    r, c = 2, 2
    expected = [[1, 2], [3, 4]]
    assert reshape_matrix(nums, r, c) == expected

def test_reshape_matrix_single_column():
    nums = [[1], [2], [3], [4]]
    r, c = 2, 2
    expected = [[1, 2], [3, 4]]
    assert reshape_matrix(nums, r, c) == expected

def test_reshape_matrix_no_change():
    nums = [[1, 2], [3, 4]]
    r, c = 2, 2
    expected = [[1, 2], [3, 4]]
    assert reshape_matrix(nums, r, c) == expected

def test_reshape_matrix_empty_matrix():
    nums = [[]]
    r, c = 0, 0
    expected = [[]]
    assert reshape_matrix(nums, r, c) == expected
