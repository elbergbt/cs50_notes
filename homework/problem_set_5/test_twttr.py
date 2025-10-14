from twttr import shorten

def test_arguments():
    assert shorten("twitter") == "twttr"
    assert shorten("Hello") == "hll"
