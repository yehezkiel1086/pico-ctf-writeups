# Local Authority

There's username and password input once you access the first page.

Inspect the source code `view-source:http://saturn.picoctf.net:63643/login.php` and you'll find the following:

```php
if ( usernameFilterPassed && passwordFilterPassed ) {

  loggedIn = checkPassword(window.username, window.password);
  
  if(loggedIn)
  {
    document.getElementById('msg').innerHTML = "Log In Successful";
    document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
    document.getElementById('hiddenAdminForm').submit();
  }
  else
  {
    document.getElementById('msg').innerHTML = "Log In Failed";
  }
}
```

notice that there's a suspicious `checkPassword(...)` function (it's a javascript function). However nowhere in the current file script could we find anything else that's interesting other than it includes another javascript file `secure.js`.

go to `secure.js` and you'll see the username and password:

```js
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

Just enter the username and password to the login page and you'll get the flag `picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}`
