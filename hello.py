try:
    int("abs")
    print("This is the statement in the try")
except ValueError as e:
    print("Issue : ", e)
    print("This is the statement in the except")
finally:
    print("This is the statement in the finally")