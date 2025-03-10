# Matching a string against a regular expresion with matches().
import re
s = input()
pattern = input()
match = re.match(pattern, s)
print(bool(match))