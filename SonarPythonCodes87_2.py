#regex module

import regex
from regex import compile, match, search, fullmatch, split, findall, finditer, sub, subn, subf, subfn, splititer

input = 'input string'
replacement = 'replacement'

regex.subf('(a*)*b', replacement, input)  # Sensitive
regex.subfn('(a*)*b', replacement, input)  # Sensitive
regex.splititer('(a*)*b', input)  # Sensitive

regex.compile('(a*)*b')  # Sensitive
regex.match('(a*)*b', input)  # Sensitive
regex.search('(a*)*b', input)  # Sensitive
regex.fullmatch('(a*)*b', input)  # Sensitive
regex.split('(a*)*b', input)  # Sensitive
regex.findall('(a*)*b', input)  # Sensitive
regex.finditer('(a*)*b',input)  # Sensitive
regex.sub('(a*)*b', replacement, input)  # Sensitive
regex.subn('(a*)*b', replacement, input)  # Sensitive