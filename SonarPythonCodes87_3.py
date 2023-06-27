#re module

import re
from re import compile, match, search, fullmatch, split, findall, finditer, sub, subn


input = 'input string'
replacement = 'replacement'

re.compile('(a*)*b')  # Sensitive
re.match('(a*)*b', input)  # Sensitive
re.search('(a*)*b', input)  # Sensitive
re.fullmatch('(a*)*b', input)  # Sensitive
re.split('(a*)*b', input)  # Sensitive
re.findall('(a*)*b', input)  # Sensitive
re.finditer('(a*)*b',input)  # Sensitive
re.sub('(a*)*b', replacement, input)  # Sensitive
re.subn('(a*)*b', replacement, input)  # Sensitive