# Forbidden Paths

it's a local file inclusion (LFI). from the problem description:

```
We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?
```

we know that we're currently in `/usr/share/nginx/html/` and we need to get to `/` to obtain the flag `/flag.txt` therefore we go back 3 times (just input the following to the HTML input) `../../../flag.txt` to get the flag

flag: `picoCTF{7h3_p47h_70_5ucc355_6db46514}`
