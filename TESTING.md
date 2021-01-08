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
 linear stepper component used works correctly. However, the State
 field color change code and the shipping to billing address code
 were not working together so the shipping to billing address code
 is in the Stripe js file. Working with tutors, it appears it many
 be a timing/loading issue. With some additional time, it likely
 can be resolved.
 3. The hero image ONLY works as specified by MD Bootstrap, which
 requires inline CSS styling and I was unable to use the main
 tags around the code. It's not best practices, but was the ONLY
 way it worked.
 4. The client gave me a no-reply email address which is part of
 their gmail group. I obtained the password for django, but it
 is not working so I'm waiting to hear back in case there is
 a typo in the gmail address of which I'm not aware. So additional
 testing and troubleshooting is needed for email addresses.

 #### Part One: Initial Navigation

 ##### Mobile Screen Version (side slide navigation menu)
**Test #1:
 <p>
 Action Taken: Click on Janeric logo 
 <br>
 "Before" State: Logo
 <br>
"After" State: Logo is same and screen jumps to home page
<br>
Test Result: Successful
 </p>

 **Test #2:
 <p>
 Action Taken: Click on "Shop All" 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to "Products" 
page with all products displayed
<br>
Test Result: Successful
 </p>

 **Test #3:
 <p>
 Action Taken: Click on "PPE" and then click on "Gowns"
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to "Products - Gowns" 
page with corresponding products displayed
<br>
Test Result: Successful
 </p>

Additional tests: this test was also conducted for all of the 
additional navigation links in the side slide navigation menu:
PPE-Masks, PPE-Social Distancing Signage, 
PPE-Thermometers, PPE-All PPE, Hand Sanitizer-Gel, Hand 
Sanitizer-Dispenser, Hand Sanitizer-All Hand Sanitizer, 
Personal-Body Wash and Shampoo, My Account-Product Management,
My Account-My Profile, My Account-Log In, My Account-Register,
My Account-Log Out, About Us.

For all of the links mentioned above, the before state was
identical to the state described above, in the "After" State
the link changed color and I was directed to the appropriate
page. Several of the links required two clicks (as indicated in
Test #3 and all of the dropdown menus were functioning 
appropriately.

**Test #4: 
<p>
Action Taken: Click on "Contact Us" 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to a new
email draft directed to customerservice@janericllc.com
<br>
Test Result: Successful
</p>

##### Large Screen Version (top navigation on home page)
**Test #5:
 <p>
 Action Taken: Click on Janeric logo 
 <br>
 "Before" State: Logo
 <br>
"After" State: Logo is same and screen jumps to home page
<br>
Test Result: Successful
 </p>

 **Test #6:
 <p>
 Action Taken: Click on "Shop All" 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to "Products" 
page with all products displayed
<br>
Test Result: Successful
 </p>

Additional tests: this test was also conducted for all of the 
additional navigation links in the side slide navigation menu:
PPE-Gowns, PPE-Masks, PPE-Social Distancing Signage, 
PPE-Thermometers, PPE-All PPE, Hand Sanitizer-Gel, Hand 
Sanitizer-Dispenser, Hand Sanitizer-All Hand Sanitizer, 
Personal-Body Wash and Shampoo, My Account-Product Management,
My Account-My Profile, My Account-Log In, My Account-Register,
My Account-Log Out, About Us. 

For all of the links mentioned above, the before state was
identical to the state described above, in the "After" State
the link changed color and I was directed to the appropriate
page. Several of the links required two clicks and all of the
dropdown menus were functioning appropriately.

**Test #7: 
<p>
Action Taken: Click on "Contact Us" 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to a new
email draft directed to customerservice@janericllc.com
<br>
Test Result: Successful
</p>

**Test #8: 
<p>
Action Taken: Click on shopping cart icon 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to cart
page
<br>
Test Result: Successful
</p>

##### Large Screen Version (side menu on Cart page)
**Test #9:
 <p>
 Action Taken: Click on "Shop All" 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to "Products" 
page with all products displayed
<br>
Test Result: Successful
 </p>

**Test #10:
 <p>
 Action Taken: Click on "PPE" and then click on "Gowns"
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to "Products - Gowns" 
page with corresponding products displayed
<br>
Test Result: Successful
 </p>

 Additional tests: this test was also conducted for all of the 
additional navigation links in the side slide navigation menu:
PPE-Gowns, PPE-Masks, PPE-Social Distancing Signage, 
PPE-Thermometers, PPE-All PPE, Hand Sanitizer-Gel, Hand 
Sanitizer-Dispenser, Hand Sanitizer-All Hand Sanitizer, 
Personal-Body Wash and Shampoo, My Account-Product Management,
My Account-My Profile, My Account-Log In, My Account-Register,
My Account-Log Out, About Us. 

For all of the links mentioned above, the before state was
identical to the state described above, in the "After" State
the link changed color and I was directed to the appropriate
page. Several of the links required two clicks and all of the
dropdown menus were functioning appropriately.

**Test 11: 
<p>
Action Taken: Click on "Contact Us" 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Link turns bright blue and screen jumps to a new
email draft directed to customerservice@janericllc.com
<br>
Test Result: Successful
</p>

#### Footer links
**Test 12: 
<p>
Action Taken: Click on email address in footer 
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Screen jumps to a new email draft directed to customerservice@janericllc.com
<br>
Test Result: Successful
</p>

**Test #13:
 <p>
 Action Taken: Click on "Shipping" link in footer
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Screen jumps to Shipping page 
<br>
Test Result: Successful
 </p>

 **Test #14:
 <p>
 Action Taken: Click on "Terms and Conditions" link in footer
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Screen jumps to Terms and Conditions page 
<br>
Test Result: Successful
 </p>

 