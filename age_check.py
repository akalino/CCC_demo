
def check_age(_age):
    """
    Checks if the age is 21 or over.
    :param _age: The input age.
    :return: Boolean: true if age is over 21, otherwise false.
    """
    _check = None
    if _age >= 21:
        print('True, age over 21.')
        _check = True
    else:
        print('False, age under 21.')
        _check = False
    return _check

if __name__ == "__main__":
    check_age(17)
