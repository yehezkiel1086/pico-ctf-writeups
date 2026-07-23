# Search Source

Inspect the page as usual `view-source:http://saturn.picoctf.net:56754`

you can see that there are some files links:

```html
<!-- bootstrap css -->
<link rel="stylesheet" href="css/bootstrap.min.css">
<!-- owl css -->
<link rel="stylesheet" href="css/owl.carousel.min.css">
<!-- style css -->
<link rel="stylesheet" href="css/style.css">
<!-- responsive-->
<link rel="stylesheet" href="css/responsive.css">
<!-- awesome fontfamily -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
```

from the above, the only logical file to inspect is `css/style.css` bc it's the only file that's supposed to be touched by the developer directly.

when you inspect `css/style.css` you'll find the flag hidden in the comment:

```css
/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49} **/
 .carousel-indicators li {
     width: 20px;
     height: 20px;
     border-radius: 11px;
     background-color: #070000;
}
```

flag: `picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49}`
