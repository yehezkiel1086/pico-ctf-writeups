#!/bin/python3

from string import ascii_lowercase

flag = "picoCTF{"
content = ""
enc = []

# read file content
with open("message.txt") as f:
  content = f.read()

# modular inverse of mod 41
enc = [pow(int(x), -1, 41) for x in content.split()]

# mapping
for x in enc:
  if x in range(1, 27):
    flag += ascii_lowercase[x - 1]
  elif x in range(27, 37):
    flag += str(x - 27)
  else:
    flag += "_"

flag += "}"

# output flag
print(flag)