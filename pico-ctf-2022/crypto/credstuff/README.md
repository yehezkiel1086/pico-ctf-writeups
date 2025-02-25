# Credstuff

## Description

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?
Download the leak [here](https://artifacts.picoctf.net/c/151/leak.tar).

The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

## Writeup

After analyzing the username `cultiris` it's at the line 378, then the password for the same line is `cvpbPGS{P7e1S_54I35_71Z3}`

From decrypting using Caesar cipher, The flag is: ``