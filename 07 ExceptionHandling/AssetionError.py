try:
    x = 10
    assert x == 5, "x should be 5"
except AssertionError as e:
    print("Assertion Error occurred:", e)
    # Handle the error gracefully
    # For example, you can log the error, notify the user, or take corrective action
