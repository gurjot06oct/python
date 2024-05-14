import random
import string
__all__ = ['random_password_generator']
def random_password_generator(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def random_color_generator():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
