import random

random.getrandbits(1) # Sensitive
random.randint(0,9) # Sensitive
random.random()  # Sensitive

# the following functions are sadly used to generate salt by selecting characters in a string ex: "abcdefghijk"...
random.sample(['a', 'b'], 1)  # Sensitive
random.choice(['a', 'b'])  # Sensitive
random.choices(['a', 'b'])  # Sensitive