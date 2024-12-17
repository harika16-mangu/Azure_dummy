
def add(a, b):
    """ A simple add function."""
    return a + b
def test_add_positive_numbers():
    """Test addition of two numbers."""
    assert add(2, 3) == 5
def test_add_negative_numbers ():
    """Test addition of two negative numbers."""
    assert add(-1, -1) == -2