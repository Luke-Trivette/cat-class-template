from cat import Cat

def test_cat():
    c1 = Cat.garfield
    assert c1.name == "Garfield"

def test_cat2():
    c1 = Cat.garfield
    assert c1.age == 50

def test_cat3():
    c1 = Cat.garfield
    assert c1.speak() == "Meow"