


def outer():
    print('enter outer.')

    def inner():
        print('enter inner.')
        print('exit inner.')
    print('exit outer.')
    return inner
