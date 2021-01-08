<h3 style="text-align: center">
    <a href="https://github.com/sherylg343/janeric">
        <img src="{{ MEDIA_URL }}janeric-banner-logo.png" alt="JANERIC" />
    </a>
</h3>

<h1 style="text-align: center">
Janeric LLC Website
</h1>

<div style="text-align: center">

[View website deployed through Heroku](https://janeric.herokuapp.com/)
</div>

## Testing

### Ongoing Testing
* Throughout development of the website, Google Chrome Developer Tools were used
to track changes and troubleshoot problems. The terminal proved invaluable in
troubleshoot Python code.
* As a troubleshooting tool and at the end of the development process, 
[W3C CSS Validation](https://jigsaw.w3.org/css-validator/),
[Nu Html Checker](https://validator.w3.org/) and
[Beautify Tools Javascript Validator](http://beautifytools.com/javascript-validator.php).
were used. 
 - CSS: 3 errors were found and numerous warnings. The errors and a number
 of the warnings are from code obtained from MD Bootstrap, so I didn't
 change it. Also, many of the warnings referred to the variables I used
 and webkit or other browser specific prefixes.
 - HTML:  Again, a number of errors/warnings are due to MD Bootstrap code.
 For example, they have me putting an header tags in a div in the footer.
 Additionally, the validator did not like the data-item-id I have in an
 input in the product details template - but that id is critical to the
 reloading the page for a new product when it is selected. It was also
 mentioned that there is no placeholder on the State field - that's 
 because it is a widget and I tried to add an additional option that
 said choose or was blank, but I wasn't able to alter it. The best I
 could do is use jQuery to change colors from gray to dark blue as
 the other fields do, though the jQuery script for that action works
 inconsistently.
 - JS Validator: code passed
 - Lighthouse: The Performance of the site is the main issue, especially
 with mobile screens where the score was as low as 8. Text compression
 should help which can be done prior to production. Also, there are 
 numerous CSS and JS files associated with MD Bootstrap and as great
 a package it is to work with, it is a drag on performance. A number of
 files which were not being used or were duplicates, were deleted.
 Accessibility and SEO were in the 80s in general, and best practices
 were 90-100.

 ### Remaining Issues
 1. As mentioned earlier, the jQuery code to change the State field
 from gray to dark blue does not consistently work, particularly 
 when the data is preloaded.
 2. Tied to #1, checkout.js was created to hold the non-stripe
 jQuery code and it was loaded at top of file so that the 
 linear stepper component used works correctly.
 2. The hero image ONLY works as specified by MD Bootstrap, which
 requires inline CSS styling and I was unable to use the main
 tags around the code. It's not best practices, but was the ONLY
 way it worked.
