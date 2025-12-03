#!/bin/python3

def caesar(enc, k = 1):
  flag = ""
  
  for x in enc:
    if x.isupper():
      flag += chr(((ord(x) - ord('A') + k) % 26) + ord('A'))
    elif x.islower():
      flag += chr(((ord(x) - ord('a') + k) % 26) + ord('a'))
    else:
      flag += x

  return flag

if __name__ == "__main__":
  enc = "bqnrrhmfsgdqtahbnmphkgrwqj"

  flag = ""

  for i in range(13):
    flag = caesar(enc, i+1)
    print(flag)

  flag = caesar(enc, 1)

  print("picoCTF{" + flag + "}")
