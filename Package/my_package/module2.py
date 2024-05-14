import random
import numpy as np
def random_sentence_generator(words, length=5):
    return ' '.join(random.choices(words, k=length))

def random_matrix_generator(rows, cols, min_val=0, max_val=100):
    return np.random.randint(min_val, max_val, size=(rows, cols))
