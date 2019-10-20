from datetime import datetime


def is_weekend():
    today = datetime.today()
    return today.weekday() >= 5


def is_it_the_weekend():
    if is_weekend():
        print("Hooray it's the weekend!")
    else:
        print("Unfortunately it's not the weekend yet :(")


if __name__ == '__main__':
    is_it_the_weekend()
