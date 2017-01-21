assert 5 == 5

try:
    assert 5 == 5
    print('Hello')
    # raise ValueError()
except AssertionError:
    print('We still run the program')
except ValueError:
    print('For value error')
finally:
    print('\nWe still alive!')
