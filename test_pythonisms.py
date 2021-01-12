import pytest
from pythonisms import Pythonisms

def test_write_text():
    text = 'this text'
    actual = Pythonisms.write_text(text)
    expected = 'this text'
    assert actual == expected

def test_add_energy():
    text = 'this needs more energy'
    actual = Pythonisms.add_energy(text)
    expected = 'OH MY GOD YES this needs more energy AAAHAHHH!!!!!!!'
    assert actual == expected

def test_decorator():
    text = 'my alarm clock broke'
    actual = Pythonisms.write_lee_quote(text)
    expected = '"my alarm clock broke" - Lee'
    assert actual == expected

def test_fill_spaces():
    text = 'this has spaces'
    actual = Pythonisms.fill_spaces(text)
    expected = ['thisblaerphasblaerpspaces']
    assert actual == expected

def test_blaerp():
    text = ' '
    actual = Pythonisms.fill_spaces(text)
    expected = ['blaerp']
    assert actual == expected