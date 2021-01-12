from functools import wraps

class Pythonisms:

    def __init__(self, values):
        self.values = values

    def quote_generator_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            orig_val = func(*args, **kwargs)
            return f'"{orig_val}" - Lee'
        
        return wrapper

    def write_text(text):
        return text

    @quote_generator_decorator
    def write_lee_quote(text):
        return text

    def add_energy(txt):
        return f'OH MY GOD YES {txt} AAAHAHHH!!!!!!!'

    def fill_spaces(text):
        new_string = []
        new_text = text.replace(' ', 'blaerp')
        new_string.append(new_text)
        return new_string


print(Pythonisms.fill_spaces('wow    all    these    spaces    are    useless!'))
print(Pythonisms.write_text('This text is great!'))
print(Pythonisms.write_lee_quote('my god these pythonsims are revolutionary!'))
print(Pythonisms.add_energy('dishes'))
print(Pythonisms.add_energy('laundry'))