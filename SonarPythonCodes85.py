#Python 2 and Python 3
import sys
from sys import stdin, __stdin__

# Any reference to sys.stdin or sys.__stdin__ without a method call is Sensitive
sys.stdin  # Sensitive

for line in sys.stdin:  # Sensitive
    print(line)

it = iter(sys.stdin)  # Sensitive
line = next(it)

# Calling the following methods on stdin or __stdin__ is sensitive
sys.stdin.read()  # Sensitive
sys.stdin.readline()  # Sensitive
sys.stdin.readlines()  # Sensitive

# Calling other methods on stdin or __stdin__ does not require a review, thus it is not Sensitive
sys.stdin.seekable()  # Ok
# ...
