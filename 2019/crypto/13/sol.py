#!/bin/python3

def rot13(enc):
  flag = ""
  
  for x in enc:
    if x.isupper():
      flag += chr(((ord(x) - ord('A') + 13) % 26) + ord('A'))
    elif x.islower():
      flag += chr(((ord(x) - ord('a') + 13) % 26) + ord('a'))
    else:
      flag += x

  return flag

if __name__ == "__main__":
  enc = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

  flag = rot13(enc)

  print(flag)
