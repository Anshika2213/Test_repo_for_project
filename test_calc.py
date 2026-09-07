from calc import calculate_average, divide


def test_normal_average():
    assert calculate_average([2, 4, 6]) == 4


def test_average_empty_list_should_return_zero():
    # Currently raises ZeroDivisionError -- this is the bug to fix
    assert calculate_average([]) == 0.0


def test_normal_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_should_return_zero():
    # Currently raises ZeroDivisionError -- this is the bug to fix
    assert divide(10, 0) == 0.0
