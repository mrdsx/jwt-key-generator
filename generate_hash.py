import random

def generate_hash():
    return "%032x" % random.getrandbits(256)
