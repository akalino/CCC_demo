
def credit_application(_age, _score):
    """
    Checks an application for a credit card.

    :param _age: The applicant's age.
    :param _score: The applicant's credit score.
    :return: Boolean, True if approved for card, otherwise False.
    """
    _approved = False
    if _age >= 18 and _score >= 660:
        print("Good news, you're approved!")
        _approved = True
    elif _age >= 18 and _score < 660:
        print("Sorry, existing score too low.")
    elif _age < 18:
        print("Sorry, you don't meet our age criteria.")
    return _approved

if __name__ == "__main__":
    credit_application(19, 670)
    credit_application(17, 670)