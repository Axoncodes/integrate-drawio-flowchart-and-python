def decision0(city=None):
    city = city or input("Which City? (t) or (f): ")
    if city == "f":
        loop0()
    elif city == "t":
        print("true")
        decision1()

def decision1(cat=None):
    cat = cat or input("Which Category? (t) or (f): ")
    if cat == "f":
        loop1()
        decision1()
    elif cat == "t":
        loop2()

def loop0():
    print("false")
    city = input("Which City Again? (t) or (f): ")
    decision0(city)

def loop1():
    print("Failed, Try Again!")
    loop0()

def loop2():
    print("Gotta, Will help you alright")
    name = input("What was your name btw? ")
    print("Nice to meet you "+name)
    loop2()

decision0()