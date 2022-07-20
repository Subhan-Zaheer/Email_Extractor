"""
This code will extract emails from given string.
"""
import re
str = """
subhanzaheer2003@gmail.com
Subhan 
hassaan@gmail.com
"""
pattern = re.compile(r"\w+@\S\w+[.\w]+")
pattern1 = re.findall(r"[a-z0-9A-Z._%]+@[a-z0-9A-Z_]+[.][a-zA-Z0-9.]+", str)
pattern2 = re.findall(r"\w+@\S\w+[.\w]+", str)
print(pattern1)
for pat in pattern1:
    print(pat)
matches = pattern.finditer(str)
for match in matches:
    print(match)