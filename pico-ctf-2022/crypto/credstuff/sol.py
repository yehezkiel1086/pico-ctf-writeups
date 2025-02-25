#!/bin/python3

def rot(text,s):
  result = ""

  # traverse text
  for i in range(len(text)):
    char = text[i]

    # Encrypt uppercase characters
    if str.isalpha(char):
      if (char.isupper()):
        result += chr((ord(char) + s-65) % 26 + 65)

      # Encrypt lowercase characters
      else:
        result += chr((ord(char) + s - 97) % 26 + 97)
    else:
      result += char

  return result

if __name__ == "__main__":
  enc = "cvpbPGS{P7e1S_54I35_71Z3}"
  flag = rot(enc, 13)
  print(flag)