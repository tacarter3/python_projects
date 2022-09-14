from pickle import NONE


def hello():
    print("Hello")


def pack(element1, element2, element3):
    pack_list = [element1, element2, element3]
    return (pack_list)



def eat_lunch(list):
    if list != 0:
        for x in list:
            print("First I eat" + x)
    elif list == 0:
        print("My lunchbox is empty!")
    




eat_lunch(["hamburger", "chips"])



# hello()

# pack("toothbrush", "socks", "hat")
