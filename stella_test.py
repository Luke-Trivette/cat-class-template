from cat import Cat

def test_cat():
    c1 = Cat.stella
    assert c1.name == "Stella"

def test_cat2():
    c1 = Cat.stella
    assert c1.age == 7

def test_cat3():
    c1 = Cat.stella
    assert c1.speak() == "Meow"