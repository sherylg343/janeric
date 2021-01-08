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

 #### Search bar
 **Test #15:
 <p>
 Action Taken: Click in search bar and type Sanitizer
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: bottom border turns to blue with light blue background
while typing
* All gel and dispense products appear in search results
* Side menu stays in place while scrolling
* Product cards are centered with margin on all sides
* Footer is where it should be, all copy readable and centered
* Back to top button is consistently located and functions as expected
<br>
Test Result: Successful
NOTE: when first conducted this test, only dispensers appeared so added
product family to the query and now functions fully
 </p>

  **Test #16:
 <p>
 Action Taken: Click in search bar and type Gowns
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: bottom border turns to blue with light blue background
while typing
* Both gown and KN-95 mask products appear in search results
* Side menu stays in place while scrolling
* Product cards are centered with margin on all sides
* Footer is where it should be, all copy readable and centered
* Back to top button is consistently located and functions as expected
<br>
Test Result: Successful
NOTE: I checked to make sure the category for KN-95 mask was correctly
and it was, but the reason it appeared is that its description states that
it is compatible with other protective equipment such as Face Shields and
Gowns - so it was appropriate for it to appear
 </p>

 #### Products template
 **Test #17:
 <p>
 Action Taken: Click on "PPE" link in mobile side nav and then click on 
 "All PPE" while in Chrome Dev Tools with iPhone 6/7/8 screen selected
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Screen jumps to Products page 
* headline is clear
* badges showing PPE categories are readable, though Thermometer is overlapping
two of them, but they are all readable
* All badge links work correctly - taking me to new page containing that
category of products
* Product cards are centered with margin on all sides
* Footer is where it should be, all copy readable and centered
* Back to top button is consistently located and functions as expected
<br>
Test Result: Successful
 </p>

 **Test #18:
 <p>
 Action Taken: Click on "PPE" link in mobile side nav and then click on 
 "All PPE" while in Chrome Dev Tools with iPhone 6/7/8 screen selected
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Screen jumps to Products page 
* headline is clear
* badges showing PPE categories fill row across and they are all readable
* All badge links work correctly - taking me to new page containing that
category of products
* There are 2 columns of product cards with space all around them
* Footer is where it should be, all copy readable and centered
* Back to top button is consistently located and functions as expected
<br>
Test Result: Successful
 </p>

 **Test #19:
 <p>
 Action Taken: Click on "PPE" link in side menu and then click on 
 "All PPE" while in Chrome Dev Tools with Response screen size 1000 
 width selected
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Screen jumps to Products page 
* headline is clear
* badges showing PPE categories are readable, though Thermometer is overlapping
two of them, but they are all readable
* All badge links work correctly - taking me to new page containing that
category of products
* Product cards are in 2 columns centered with margin on all sides
* Main content scrolls but side menu is fixed
* Footer is where it should be, all copy readable and centered
* Back to top button is sticking to bottom of screen and only appears once
scroll down - this seems to be the planned action for desktop screens
<br>
Test Result: Successful
 </p>

 **Test #20:
 <p>
 Action Taken: Click on "PPE" link in side menu and then click on 
 "All PPE" while in Chrome Dev Tools with Response screen size 1300 
 width selected
 <br>
 "Before" State: Link is gray/blue
 <br>
"After" State: Screen jumps to Products page 
* headline is clear
* badges showing PPE categories are readable, though Thermometer is overlapping
two of them, but they are all readable
* All badge links work correctly - taking me to new page containing that
category of products
* Product cards are in three columns, centered with appropriate margin 
on all sides
* Main content scrolls but side menu is fixed
* Footer is where it should be, all copy readable and centered
* Back to top button is sticking to bottom of screen and only appears once
scroll down - this seems to be the planned action for desktop screens
<br>
Test Result: Successful
NOTE: the Floor Markers image with arrows bleeds to the edges of
the card, but doesn't overflow. This is a horizontal image and I decided
it was more important to show as much of product as possible rather than
crop the image to fit space better.
 </p>

 #### Product Detail template
 **Test #21:
 <p>
 Action Taken: From the Products page, click on "View" button for a
 dispenser stand while in Chrome Dev Tools with iPhone 6/7/8 screen selected
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and screen jumps to Products Detail page. 
* Headline is clear and brand name is visible, as is "Keep Shopping" link
* Product image is centered
* Price is clear - select button doesn't work for this product as there
is only one option in product family
* The quantity + and - buttons work appropriately 
* Description centered under "Add to Cart" button
* Footer is where it should be, all copy readable and centered
<br>
Test Result: Successful
Secondary Tests:
Delete link successfully deleted button (wnat to add confirmation before
deletion as future feature) and message confirmed product was deleted

Update link took me to template to Edit the product and received Alert
message stating the product to be edited. I clicked "Cancel" link and
was sent back to Product page with all products listed.
 </p>

 **Test #22:
 <p>
 Action Taken: From the Products page, click on "View" button for a
 dispenser stand while in Chrome Dev Tools with iPad screen selected
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and screen jumps to Products Detail page. 
* Headline is clear and brand name is visible, as is "Keep Shopping" link
* Product image is in left column with ample margin around it
* Price is clear - select button doesn't work for this product as there
is only one option in product family
* Description centered below the image and "Add to Cart" button
* Footer is where it should be, all copy readable and centered
<br>
Test Result: Successful
Secondary Test: Clicked on quantity + and - buttons to verify the minimum
and maximum ranges. The - button would not decrease the value below 1 and
the + would not increase the value past 99.
Test Result: Successful

**Test #23:
 <p>
 Action Taken: From the Products page, click on "View" button for a
 dispenser stand while in Chrome Dev Tools with responsive screen 
 with width of 1000 selected
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and screen jumps to Products Detail page. 
* Headline is clear and brand name is visible, as is "Keep Shopping" link
* Main content scrolls but side menu is fixed
* Product image is in left column with ample margin around it
* Price is clear - select button doesn't work for this product as there
is only one option in product family
* Description centered below the image and "Add to Cart" button
* Footer is where it should be, all copy readable and centered
<br>
Test Result: Successful

**Test #23:
 <p>
 Action Taken: From the Products page, click on "View" button for a
HP Pure Hand Sanitizer, Size: Gallon, Case of 4 while in Chrome Dev Tools with responsive screen with width of 1300 selected
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and screen jumps to Products Detail page. 
* Headline is clear and brand name is visible, as is "Keep Shopping" link
* Main content scrolls but side menu is fixed
* Product image is way too big, taller than the buttons on the right
* Price is clear - select button provides size and case options and when
click on a different option, the page reloads to that page and that
product's size, case and price is selected under "Price" label
* Description centered below the image and "Add to Cart" button
* Footer is where it should be, all copy readable and centered
<br>
Test Result: Fails
CSS change: #detail-image-img gains a max-height attribute and value of
250px. 
Second Test Result: Successful

 #### Product Detail template
 **Test #24:
 <p>
 Action Taken: From the Product Detail page, click on "Add to Cart" button
 for a 8 oz., Case of 24, Hand Sanitizer gel while in Chrome Dev Tools with
iPhone 6/7/8 screen selected. Quantity selected is 2.
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and pop up message
appears station the product selected was added to cart.
* The product name in header is correctly
* The product count in cart (2) is stated correctly.
* The product image, product family name, size, case and quantity listed
in product detail section of message are all correct. 
* The individual unit cost is $95.76 so the Total of $191.52 is correct.
* The "View Cart" button in the pop-up window does take me to the 
Shopping Cart.
 <br>
Test Result: Successful
 </p>