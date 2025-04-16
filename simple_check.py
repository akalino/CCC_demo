
def variable_check(_x):
    """
    Checks if a variable has value greater than 10.
    :param _x: The input variable.
    :return: Boolean, True if variable greater than 10.
    """
    _bool = False
    if _x > 10:
        _bool = True
    return _bool

if __name__ == "__main__":
    check_nine = variable_check(9)
    print(check_nine)
    check_twenty = variable_check(20)
    print(check_twenty)
    check_ten = variable_check(10)
    print(check_ten)
