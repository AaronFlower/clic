import create as cli

def test_isValidName():
    assert cli.isValidName("abc")

def test_isInvalidName():
    assert not cli.isValidName("")
    assert not cli.isValidName("/a/")
    assert not cli.isValidName("/a/b/")
    assert not cli.isValidName("a/b/")
    assert not cli.isValidName("-b/")
