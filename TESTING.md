<h3 style="text-align: center">
    <a href="https://github.com/sherylg343/janeric">
        <img src="media/janeric-banner-logo.png" alt="JANERIC" />
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

 ### Caveat
 I fully acknowledge that the manual testing described below is not
 comprehensive enough for the website to be ready to launch.
 However, it represents a thorough general functional testing
 of the website features and additional testing to anticipate
 misuse of the site is planned for the future.

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

#### Part Two: Footer links
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

 #### Part Three: Search bar
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

 #### Part 4: Products template
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

 #### Part 5: Product Detail template
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

 #### Part 6: Product Detail template
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

 **Test #25:
 <p>
 Action Taken: From the Product Detail page, click on "Add to Cart" button
 for a Gallon size of Club Basics Body Wash and Shampoo Ocean Mist while
in Chrome Dev Tools with iPad screen selected. Quantity selected is 5.
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and pop up message
appears stating the product selected was added to cart.
* The product name in header is correctly
* The product count in cart (5) is stated correctly.
* The product image, product family name, size, case and quantity listed
in product detail section of message are all correct. 
* The individual unit cost is $21.20 so the Total of $106.00 is correct.
* The "View Cart" button in the pop-up window does take me to the 
Shopping Cart.
 <br>
Test Result: Successful
 </p>

 **Test #26:
 <p>
 Action Taken: From the Product Detail page, click on "Add to Cart" button
 for a Gallon size of Club Basics Body Wash and Shampoo Ocean Mist while
in Chrome Dev Tools with responsive screen with width of 1100 selected. 
Quantity selected is 5.
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and pop up message
appears stating the product selected was added to cart.
* The product name in header is correctly
* The product count in cart (5) is stated correctly.
* The product image, product family name, size, case and quantity listed
in product detail section of message are all correct. 
* The individual unit cost is $21.20 so the Total of $106.00 is correct.
* The "View Cart" button in the pop-up window does take me to the 
Shopping Cart.
 <br>
Test Result: Successful
 </p>

**Test #27:
 <p>
 Action Taken: From the Product Detail page, click on "Add to Cart" button
 for a KN-95 Respirator Mask while in Chrome Dev Tools with a responsive
screen width of 1300 selected. Quantity selected is 10.
 <br>
 "Before" State: View button is dark gray with white text
 <br>
"After" State: White text turns blue when click button and pop up message
appears stating the product selected was added to cart.
* The product name in header is correctly
* The product count in cart (10) is stated correctly.
* The product image, product family name, size, case of 10 and quantity 
of 10 listed in product detail section of message are all correct. 
* The individual unit cost is $99.80 so the Total of $998.00 is correct.
* The "View Cart" button in the pop-up window does take me to the 
Shopping Cart.
 <br>
Test Result: Successful
 </p>

#### Part 7: Cart template
 **Test #28:
 <p>
 Action Taken: On the Cart page while in Chrome Dev Tools with
Pixel 2 screen selected increase the quantity selected button from 2
to 3 and click "Update" link.
 <br>
 "Before" State: Quantity of 2, price per unit is $84.70 and Product Subtotal
 is $169.40.
 <br>
"After" State: 
* Message box pops up stating "Updated Club Basics Body Wash and Shampoo Ocean
Mist - Gallon Case of 4 quantity to 3."
* Total product count shows 3
* When close pop up the quantity in cart shows 3 and Product Subtotal is
now $254.10.
 <br>
Test Result: Successful
Secondary Test: 
Action Taken: Click "Remove From Cart" link.
 <br>
 "Before" State: Quantity of 3 as described above.
 <br>
"After" State: 
* Message box pops up stating "Removed Club Basics Body Wash and Shampoo Ocean
Mist - Gallon Case of 4 from your cart."
* When close pop up the message in the cart is "Your shopping cart is empty!"
 <br>
Test Result: Successful
 </p>

 **Test #29:
 <p>
 Action Taken: On the Cart page while in Chrome Dev Tools with
iPad screen selected have quantity of 5 Floor Markers in cart.  Click the 
- button and decrease the quantity selected button from 5 to 2 and 
click "Update" link.
 <br>
 "Before" State: Quantity of 5, price per unit is $149.00 and Product Subtotal
 is $175.00.
 <br>
"After" State: 
* Message box pops up stating "Updated Mix and Match set of 5 12 ft. x 12 ft.
Floor Markers quantity to 2."
* Total product count shows 2
* When close pop up the quantity in cart shows 2 and Product Subtotal is
now $298.00.
 <br>
Test Result: Successful
Secondary Test: 
Action Taken: Click "Remove From Cart" link.
 <br>
 "Before" State: Quantity of 3 as described above.
 <br>
"After" State: 
* Message box pops up stating "Removed Mix and Match set of 5 12 ft. x 12 ft.
Floor Markers from your cart."
* When close pop up the message in the cart is "Your shopping cart is empty!"
 <br>
Test Result: Successful
 </p>

 **Test #30:
 <p>
 Action Taken: On the Cart page while in Chrome Dev Tools with
responsive screen with width of 1100, selected have quantity of 6 HS Pure - 
16 oz. - 24/case.  Click the - button and decrease the quantity selected button from 6 to 3 and click "Update" link.
 <br>
 "Before" State: Quantity of 6, price per unit is $179.52 and Product Subtotal
 is $1077.12.
 <br>
"After" State: 
* Message box pops up stating "Updated HS Pure - 16 oz. - 24/case 
quantity to 3."
* Total product count shows 3.
* When close pop up the quantity in cart shows 2 and Product Subtotal is
now $538.56.
 <br>
Test Result: Successful
Secondary Test: 
Action Taken: Click "Remove From Cart" link.
 <br>
 "Before" State: Quantity of 3 as described above.
 <br>
"After" State: 
* Message box pops up stating "Removed HS Pure - 16 oz. - 24.case from your
cart."
* When close pop up the message in the cart is "Your shopping cart is empty!"
 <br>
Test Result: Successful
 </p>

 **Test #31:
 <p>
 Action Taken: On the Cart page while in Chrome Dev Tools with
responsive screen with width of 1300, selected have quantity of 2 Open 
Back Level 2 CPE Gown (Set of 360).  Click the + button and increase the 
quantity selected button from 2 to 3 and click "Update" link.
 <br>
 "Before" State: Quantity of 2, price per unit is $1256.40 and Product Subtotal
 is $2512.80.
 <br>
"After" State: 
* Message box pops up stating "Updated Open Back Level 2 CPE Gown (Set of 360) 
quantity to 3."
* Total product count shows 3.
* When close pop up the quantity in cart shows 2 and Product Subtotal is
now $3769.20.
 <br>
Test Result: Successful
Secondary Test: 
Action Taken: Click "Remove From Cart" link.
 <br>
 "Before" State: Quantity of 3 as described above.
 <br>
"After" State: 
* Message box pops up stating "Removed Open Back Level 2 CPE Gown (Set of 360) 
from your cart."
* When close pop up the message in the cart is "Your shopping cart is empty!"
 <br>
Test Result: Successful
 </p>

 #### Part 8: Checkout template
 * The following tests were done while in Chrome Dev Tools with
screen size set to iPhoneX
 **Test #32:
 <p>
 Action Taken: typed email address in input box
 <br>
 "Before" State: gray placeholder states "Email Address *"
 <br>
"After" State: email address appears in input box in dark type
 <br>
Test Result: Successful
Secondary Test 1 (default shipping address stored): 
Action Taken: Click "Continue" button.
 <br>
 "Before" State: Dark gray button with white text.
 <br>
"After" State: 
* Step one closes and a dark gray circle with white check mark appears
in its place
* Shipping header with #2 in blue circle appears
* My default shipping address appears in the fields in dark text
* Those fields without text have a gray placeholder in field
 <br>
Test Result: Successful
<br>
Secondary Test 2 (no default shipping address stored): 
Action Taken: Click "Continue" button.
 <br>
 "Before" State: Dark gray button with white text.
 <br>
"After" State: 
* Step one closes and a dark gray circle with white check mark appears
in its place
* Shipping header with #2 in blue circle appears
* Shipping fields appear with gray placeholders in field
* When enter data into fields, text is dark colored
<br>
Test Result: Successful
 </p>

 **Test #33:
 <p>
 Action Taken: typed address information into input box
 as guest user
 <br>
 "Before" State: address input fields with gray placeholders stating
 information to be input into fields
 <br>
"After" State: address information appears in input boxes in dark type
 <br>
Test Result: Successful
 </p>

 **Test #34:
 <p>
 Action Taken: click "Continue" button at bottom of shipping address
 input fields
 <br>
 "Before" State: gray "Continue" button
 <br>
"After" State: 
* Step 2 section with shipping address collapses
* Step 3 appears in dark blue circle
* Billing address fields appear with gray placeholders 
 <br>
Test Result: Successful
 </p>

 **Test #35:
 <p>
 Action Taken: click checkbox next to "Same as shipping address"
 <br>
 "Before" State: empty checkbox
 <br>
"After" State: 
* blue checkmark appears next to "Same as shipping address"
* billing address fields are filled with shipping address information
* state field text does not change from gray to black
 <br>
Test Result: Successful except for State field text color
 </p>

 **Test #36:
 <p>
 Action Taken: click checkbox next to "Same as shipping address"
 <br>
 "Before" State: empty checkbox
 <br>
"After" State: 
* blue checkmark appears next to "Same as shipping address"
* billing address fields are filled with shipping address information
 <br>
Test Result: Successful
 </p>

 **Test #37:
 <p>
 Action Taken: enter test credit card number in payment field
 <br>
 "Before" State: empty field with gray placeholders
 <br>
"After" State: 
* dark text fills field
* as completed one section automatically tabbed over to next
section of the field
 <br>
Test Result: Successful
 </p>

  **Test #38:
 <p>
 Action Taken: Click on "Pay Now" button
 <br>
 "Before" State: dark gray button says "Pay Now"
 <br>
"After" State: 
* overlay appears with circling icon
* pop up box appears stating "Order successfully proccessed. Your
order number is ... A confirmation email will be sent to {email address}."
* When close pop up box, see "Thank You" page with summary of order.
 <br>
Test Result: Successful
 </p>

 * The following tests were done while in Chrome Dev Tools with
screen size set to iPad
 **Test #39:
 <p>
 Action Taken: typed email address in input box
 <br>
 "Before" State: gray placeholder states "Email Address *"
 <br>
"After" State: email address appears in input box in dark type
 <br>
Test Result: Successful
Secondary Test 1 (default shipping address stored): 
Action Taken: Click "Continue" button.
 <br>
 "Before" State: Dark gray button with white text.
 <br>
"After" State: 
* Step one closes and a dark gray circle with white check mark appears
in its place
* Shipping header with #2 in blue circle appears
* My default shipping address appears in the fields in dark text
* Those fields without text have a gray placeholder in field
 <br>
Test Result: Successful
<br>
Secondary Test 2 (no default shipping address stored): 
Action Taken: Click "Continue" button.
 <br>
 "Before" State: Dark gray button with white text.
 <br>
"After" State: 
* Step one closes and a dark gray circle with white check mark appears
in its place
* Shipping header with #2 in blue circle appears
* Shipping fields appear with gray placeholders in field
* When enter data into fields, text is dark colored
<br>
Test Result: Successful
 </p>

 **Test #40:
 <p>
 Action Taken: typed address information into input box
 as guest user
 <br>
 "Before" State: address input fields with gray placeholders stating
 information to be input into fields
 <br>
"After" State: address information appears in input boxes in dark type
 <br>
Test Result: Successful
 </p>

 **Test #41:
 <p>
 Action Taken: click "Continue" button at bottom of shipping address
 input fields
 <br>
 "Before" State: gray "Continue" button
 <br>
"After" State: 
* Step 2 section with shipping address collapses
* Step 3 appears in dark blue circle
* Billing address fields appear with gray placeholders 
 <br>
Test Result: Successful
 </p>

 **Test #42:
 <p>
 Action Taken: click checkbox next to "Same as shipping address"
 <br>
 "Before" State: empty checkbox
 <br>
"After" State: 
* blue checkmark appears next to "Same as shipping address"
* billing address fields are filled with shipping address information
* state field text does not change from gray to black
 <br>
Test Result: Successful except for State field text color
 </p>

 **Test #43:
 <p>
 Action Taken: click checkbox next to "Same as shipping address"
 <br>
 "Before" State: empty checkbox
 <br>
"After" State: 
* blue checkmark appears next to "Same as shipping address"
* billing address fields are filled with shipping address information
 <br>
Test Result: Successful
 </p>

 **Test #44:
 <p>
 Action Taken: enter test credit card number in payment field
 <br>
 "Before" State: empty field with gray placeholders
 <br>
"After" State: 
* dark text fills field
* as completed one section automatically tabbed over to next
section of the field
 <br>
Test Result: Successful
 </p>

  **Test #45:
 <p>
 Action Taken: Click on "Pay Now" button
 <br>
 "Before" State: dark gray button says "Pay Now"
 <br>
"After" State: 
* overlay appears with circling icon
* pop up box appears stating "Order successfully proccessed. Your
order number is ... A confirmation email will be sent to {email address}."
* When close pop up box, see "Thank You" page with summary of order.
 <br>
Test Result: Successful
 </p>

 * The following tests were done while in Chrome Dev Tools with
screen size set to responsive and width of 1100
 **Test #46:
 <p>
 Action Taken: typed email address in input box
 <br>
 "Before" State: gray placeholder states "Email Address *"
 <br>
"After" State: email address appears in input box in dark type
 <br>
Test Result: Successful
Secondary Test 1 (default shipping address stored): 
Action Taken: Click "Continue" button.
 <br>
 "Before" State: Dark gray button with white text.
 <br>
"After" State: 
* Step one closes and a dark gray circle with white check mark appears
in its place
* Shipping header with #2 in blue circle appears
* My default shipping address appears in the fields in dark text
* Those fields without text have a gray placeholder in field
 <br>
Test Result: Successful
<br>
Secondary Test 2 (no default shipping address stored): 
Action Taken: Click "Continue" button.
 <br>
 "Before" State: Dark gray button with white text.
 <br>
"After" State: 
* Step one closes and a dark gray circle with white check mark appears
in its place
* Shipping header with #2 in blue circle appears
* Shipping fields appear with gray placeholders in field
* When enter data into fields, text is dark colored
<br>
Test Result: Successful
 </p>

 **Test #47:
 <p>
 Action Taken: typed address information into input box
 as guest user
 <br>
 "Before" State: address input fields with gray placeholders stating
 information to be input into fields
 <br>
"After" State: address information appears in input boxes in dark type
 <br>
Test Result: Successful
 </p>

 **Test #48:
 <p>
 Action Taken: click "Continue" button at bottom of shipping address
 input fields
 <br>
 "Before" State: gray "Continue" button
 <br>
"After" State: 
* Step 2 section with shipping address collapses
* Step 3 appears in dark blue circle
* Billing address fields appear with gray placeholders 
 <br>
Test Result: Successful
 </p>

 **Test #49:
 <p>
 Action Taken: click checkbox next to "Same as shipping address"
 <br>
 "Before" State: empty checkbox
 <br>
"After" State: 
* blue checkmark appears next to "Same as shipping address"
* billing address fields are filled with shipping address information
* state field text does not change from gray to black
 <br>
Test Result: Successful except for State field text color
 </p>

 **Test #50:
 <p>
 Action Taken: click checkbox next to "Same as shipping address"
 <br>
 "Before" State: empty checkbox
 <br>
"After" State: 
* blue checkmark appears next to "Same as shipping address"
* billing address fields are filled with shipping address information
 <br>
Test Result: Successful
 </p>

 **Test #51:
 <p>
 Action Taken: enter test credit card number in payment field
 <br>
 "Before" State: empty field with gray placeholders
 <br>
"After" State: 
* dark text fills field
* as completed one section automatically tabbed over to next
section of the field
 <br>
Test Result: Successful
 </p>

  **Test #52:
 <p>
 Action Taken: Click on "Pay Now" button
 <br>
 "Before" State: dark gray button says "Pay Now"
 <br>
"After" State: 
* overlay appears with circling icon
* pop up box appears stating "Order successfully proccessed. Your
order number is ... A confirmation email will be sent to {email address}."
* When close pop up box, see "Thank You" page with summary of order.
 <br>
Test Result: Successful
 </p>

 skipped doing the checkout tests in screen size 1300 as layout was the same

#### Part 9: Profile template
 **Test #53:
 <p>
 Action Taken: In Profile template in Pixel 2 screen size in Chrome
 Dev Tools, changed state from NY to NM and clicked "Update 
 Information" button
 <br>
 "Before" State: State field says New York in dark text
 <br>
"After" State: 
* New Mexico appears in state field in dark text
* pop up box appears stating "Profile updated successfully."
 <br>
Test Result: Successful
 </p>

 **Test #54:
 <p>
 Action Taken: In Profile template in Pixel 2 screen size in Chrome
 Dev Tools, changed street address1 and clicked "Update 
 Information" button
 <br>
 "Before" State: address field said "41 Placid Ter"
 <br>
"After" State: 
* address1 field said "21 Eastlake Rd." in dark text
* pop up box appears stating "Profile updated successfully."
 <br>
Test Result: Successful
 </p>

 **Test #55:
 <p>
 Action Taken: In Profile template in Pixel 2 screen size in Chrome
 Dev Tools, changed street address1 and clicked "Update 
 Information" button
 <br>
 "Before" State: address field said "41 Placid Ter"
 <br>
"After" State: 
* address1 field said "21 Eastlake Rd." in dark text
* pop up box appears stating "Profile updated successfully."
 <br>
Test Result: Successful
 </p>

 **Test #56:
 <p>
 Action Taken: In Profile template in responsive screen 
 in width size of 1100 in Chrome Dev Tools, changed city and clicked 
 "Update Information" button
 <br>
 "Before" State: address field said "Ithaca"
 <br>
"After" State: 
* address1 field said "Durango" in dark text
* pop up box appears stating "Profile updated successfully."
 <br>
Test Result: Successful
 </p>

 #### Part 10: Add a Product Family
 **Test #57:
 <p>
 Action Taken: On Product Families page, click "Add a Product Family"
 <br>
 "Before" State: Dark gray button with white text stating "Add a 
 Product Family"
 <br>
"After" State: 
* White button text turns bright blue
* Page changes to "Add a Product Family" page
 <br>
Test Result: Successful
 </p>

 **Test #58:
 <p>
 Action Taken: On Add a Product Family page, add test text in 
 Name and Brand Name input fields and click "Add Product Family" 
 button
 <br>
 "Before" State: empty fields with labels above them
 <br>
"After" State: 
* Text in input fields
* page switches to "Product Families" page
* Success pop up message does not appear
 <br>
Test Result: Successful save, but message NOT appearing
 </p>

 #### Part 10: Edit a Product Family
**Test #59:
 <p>
 Action Taken: On Product Families page, click "Edit" link below
 the new Test Product Family
 <br>
 "Before" State: Gray link that says "Edit"
 <br>
"After" State: Page changes to "Edit a Product Family" page
 <br>
Test Result: Successful
 </p>

 **Test #60:
 <p>
 Action Taken: On Edit a Product Family page, revise test text in 
 Name and Brand Name input fields and click "Update Product Family" 
 button
 <br>
 "Before" State: Name and Brand Name fields with test text
 in them
 <br>
"After" State: 
* Revised text in Brand Name field
* Dark gray button text turns bright blue
* Page returns to "Product Families" page
* Success message does NOT appear
 <br>
Test Result: Successful update, but success message not appearing
 </p>

#### Part 12: Add a Product 
 **Test #61:
 <p>
 Action Taken: In nav bar, clicked on "Add a Product"
 <br>
 "Before" State: Gray "Add a Product" link
 <br>
"After" State: 
* Link turns bright blue
* Page changes to "Add a Product" page
 <br>
Test Result: Successful
 </p>

 **Test #62:
 <p>
 Action Taken: On Add a Product page, add test text in 
 all input fields and click "Add Product" 
 button
 <br>
 "Before" State: empty fields with labels above them
 <br>
"After" State: 
* Text in input fields
* Pop up message appears stating "Successfully added product"
* Page changes to product detail page for the new product
 <br>
Test Result: Successful
 </p>

 #### Part 13: Edit a Product
**Test #63:
 <p>
 Action Taken: On product detail page for new product, click "Edit" 
 link 
 <br>
 "Before" State: Gray link that says "Edit"
 <br>
"After" State: 
* Edit link turns bright blue
* Page changes to "Edit Product" page
 <br>
Test Result: Successful
 </p>

 **Test #64:
 <p>
Action Taken: On "Edit Product" page, revise test text in 
input fields and click "Update Product" button 
button
 <br>
 "Before" State: Fields complete with text text
 in them
 <br>
"After" State: 
* Revised text in description field, removed image and changed size
* Dark gray button text turns bright blue in button
* Pop up box displays message stating "Successfully updated product!"
* Screen changes to product detail page where product is displayed
so you can verify changes - and they were all made.
 <br>
Test Result: Successful
 </p>