from lecture_5.hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Ron", "Hermione", "Harry"]:
        assert hello(name) == f"hello, {name}"