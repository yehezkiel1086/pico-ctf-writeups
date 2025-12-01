# The Numbers POC

```py
#!/bin/python3

from string import ascii_uppercase

nums = [16, 9, 3, 15, 3, 20, 6, '{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

for i in nums:
  if type(i) == str:
    print(i, end="")
  else:
    print(ascii_uppercase[i - 1], end="")
```

Flag: `PICOCTF{THENUMBERSMASON}`
