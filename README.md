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

## Table of Contents <a name="table-of-contents"></a> 

1. [Project Purpose](#purpose)

2. [UX](#ux)

3. [Features](#features)

4. [Future_Goals](#future)

5. [Technology Used](#technology-used)

6. [Testing](#testing) - text in another document [TESTING](TESTING.md)

7. [Deployment](#deployment)

8. [Credits](#credits)

9. [Disclaimer](#disclaimer)

[Back to Top](#table-of-contents)


## Project Purpose <a name="purpose"></a> 
Janeric LLC was formed during the beginning of the coronavirus pandemic, with 
the goal of selling personal protective equipment in volume to organizations. 
As an established business owner, Eric Parsells approached is wife and children
about starting the business as a learning opportunity and a way to help 
frontline workers.

Management intended to develop a website using BigCommerce, but accepted the 
developer's offer to build the site for free as a final school project. The 
purpose of the website is provide a channel to sell products to all users of 
personal protective equipment within the United States.

### Project Goals
The primary goal of the website is to generate sales so the site needs to be 
user-friendly and enable both established account users and guest users to 
easily select and purchase products.

A secondary goal for the second phase of the project is to add information 
about the UV equipment that kills cornoviruses and other micro-organisms.  
Since this is a product that requires a more consultative sales approach,
the purpose of that product section on the site will be to educate and generate
sales leads.

### Target Audience
The client states that their target audience is not segmented, it is all users
and purchasers of personal protective equipment within the contiguous United
States.

<p>

[Back to Top](#Table-of-Contents)
</p>
---

## UX <a name="ux"></a>

### Targeted Visitors
The client's targeted visitors are users and purchasers of personal protective
equipment, with a focus on those buying for organizations. 

### User Stories
The following was based upon the user stories for the Boutique Ado project, but
revised to fit the needs of the Janeric website.

<h9 style="text-align: center">
        <img src="{{ MEDIA_URL }}user-stories.png" alt="JANERIC" />
</h9>

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Features <a name="features"></a>

### Use of Five Planes of UX in Project Design
#### Strategy Plane
The client's business is new and didn't have an established Unique Selling
Proposition initially. They developed the following phrase and specified
its use on the home page: "Clean and effective solutions to help keep
those you care about safe." 

An evaluation was conducted to determine which customer needs the website 
should address first. These customer needs are listed and reviewed in the 
[Strategy Trade-Off Analysis](). 

The UV Lighting sales process and materials were not yet developed, so
they were rated lower in importance and will be added in the second phase.

Prior to developing this analysis, the following ecommerce websites were viewed and
evaluated based on client's preferences: Amazon, acacia.co for cart and checkout
system, aman, goop for functionality, jennikayne, ashleykane and singlethreadfarms.

#### Scope Plane
Below is a summary of the analysis done for this website during the Scope Plane.
1. Objective: The user wants a resource to quickly and easily purchase the
personal protective equipment, in the product and pack sizes needed, to operate 
their business, practice or other type of organization. The user is looking for
one vendor that can provide the equipment needed in a timely manner.
2. Functional: The users need to easily find the products of interest, as well
as checkout in an efficient, error-free manner.
3. Non-functional: The scientific research and educational material for 
UV Lighting will provide necessary content to support lead generation and
sales process, but those resources are not yet ready or available so will
be done in the second phase or sprint. Regarding security, allauth provides
verification for account creation and use, and additional packages need
to be obtained to help with shipping address verification. Given the limited
initial traffic anticipated, using a state select field and verifying format
of zip code will be adequate at this time, but full address verification
will be re-visited when traffic or shipping errors merit the effort to add it.
4. Business Rules: As this is a new business, sales materials and processes are
not fully established and human resources are a constraint, so not all product 
profiles are complete and UV Lighting is tabled for second phase.

#### Structure Plane
Below are the key considerations relative to the Structure Plane.
1. Consistency: 
* All links on the page are the same color of gray/blue and the hover/
active color is the bright blue that matches the logo color.
* All page headings use the same font as the logo (per client's request)
* search bar is at center and above page content for all pages and 
screen sizes
* Information is positioned to provide most important near the top of 
the page, particularly for mobile versions.
* The navigation is a side menu for all large and extra-large screens
as requested by client, set-off by the blush background. The only exception
is the home page so that menu doesn't interfere with hero image impact.
* Long pages all have "back to top" button in same color and position
2. Predictable: 
* placeholders for all input fields are same color and left-aligned.
* "Keep Shopping" link is in same location on all non-product pages and
appears in same color and typeface.
* Buttons are all same color and size, as well as clearly labeled
* Top nav bar is sticky so logo, account options and cart total appears
on each page wherever you are when scrolling.
3. Learnable:
* toast messages provide feedback to user about actions taken, color-coded
for type of message
* Nav dropdown menus are intuitive and easy to read
* Checkout page uses a stepper, collapsing each completed step to keep focus
on current step and minimizing clutter without changing pages
* Page headlines are in same location on each page, identifying page
user is visiting and its purpose
4. Visible
* Account menu items visible based upon whether user is signed in or not
* Product management pages and action buttons are only visible to store owner
signed in as superuser
* Product content is prioritized and stacked for mobile viewers
5. User Feedback:
* Spinner overlay is initiated when checkout button is clicked to let user
know order is being processed
* Error messages provide feedback regarding form submission problems
* Input field text color is different than placeholder text color providing
feedback that input is occurring.
* On checkout page, the icon for completed steps is gray and active step is
blue.

#### Skeleton Plane
Usability: the following design elements are designed the same to provide
consistency and improve usability throughout the site.
* quantity selector
* size and pack selector
* state input select widget - easier to use and improves accuracy
Also, on product profile page, the quantity and size/pack selector are placed
above the product description - ordering them in terms of importance.

Product cards used for search results, utlize the product family name and
minimize white space to keep the product information simple, uncluttered and
easy to view.

#### Wireframe Mock-Ups:
After reviewing the User Stories and evaluating the Features, the following
mockups were designed for the 3 primary screen sizes using 
[Balsamiq software](https://balsamiq.com/). 
The website was created using a mobile-first design philosophy.

<div style="text-align:center;">

[Mobile]()
</div>

<div style="text-align:center;">

[Tablet]()
</div>

<div style="text-align:center;">

[Desktop]()
</div>

#### Surface Plane
1. Background: 
* a hero image of personal protective equipment in use was selected to
create an impactful first impression in tandem with the company's USP and
a "Shop Now" button providing an immediate call-to-action.
* the color palette was based on the blue and white logo and then the 
client selected 
[Color Palette #4147](https://colorpalettes.net/color-palette-4147/) 
as accent colors.
2. Fonts:
* the client provided the Caslon 3 Roman font used in their logo, 
for page headlines. Barlow was used in cart and checkout for sub-headings
and Roboto is used for body text. Barlow and Roboto were selected for
being simple and clean.
* use of Barlow in subheads, all in caps and with increased letter spacing 
was modeled after Jenni Kayne website's shopping cart column headers.
3. Images/Icons:
* all product images supplied by client but used at significant size
as images are believed to be key element of product sales.
* client requested simple, clean look so icon use was minimal.
Controls:
* buttons and links are consistently colored and text chosen
to aptly describe actions to be taken.

### More on Features
Navigation: A sticky navigation bar with a dropdown menu for account links
provides easy access to all sections of the website wherever the user is.
A mobile version has a menu icon and side-slide navbar for ease of use.
The side-menu for larger screens in not as conventional, however, it was
specifically requested by the client.

Defensive Design: as mentioned previously, this was a key concept considered
in designing the website and to facilitate ease and pleasure of use.

NEEDS More

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Future Goals <a name="future-goals"></a>

### Direct the deployed site to purchased domain
Client has purchased domain name of www.janericllc.com and website
needs to be redirected to that domain prior to launching

### Select and implement a U.S. tax package
Given the complexity of US sales tax, a software package needs to be
selected and installed to calculate the correct sales tax. TaxJar
is currently being considered.

### Add UV Lighting products, educational information and contact form
This sales process is not yet well-defined so once it is, additional
pages will be added to help educate user and gain qualified sales leads.

### Address verification
When traffic and sales increase, if there are issues with accuracy of
shipping addresses, django-address with Google API's could be added to
reduce shipping errors.

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Technology Used <a name="technology-used"></a>

## Languages, Frameworks, Editors & Version Control:
* HTML & CSS programming languages
* [MD Bootstrap](https://mdbootstrap.com/) - used to make the website
visually appealing with pre-made components
* [Python](https://www.python.org/) - used with Django to operate website
* [Django](https://www.djangoproject.com/) - framework used in 
conjunction with Python to create and operate the website
* [jQuery](https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js) 
* JavaScript - used with jQuery for functionality of website
* [GIT](https://git-scm.com/) - Version Control
* [GITHUB](https://github.com) - to host the repositories for this project and 
the live website preview

## Tools Used:
* [PstgreSQL](https://www.postgresql.org/) - used with Heroku to manage data for
the website
* [AWS-S3](https://s3.console.aws.amazon.com/s3/home?region=us-east-1#) - storage
for static and media files for the website
* [Heroku](https://www.heroku.com/home) - used to deploy nonproduction version of
website
* [Stripe](https://stripe.com/) - used to process payments on website
* [GoogleChromeDevTools](https://developers.google.com/web/tools/chrome-devtools) -
used to test and troubleshoot the functionality of the website and assist in
visual styling decisions, especially relative to screen sizes
* [GoogleFonts](https://fonts.google.com/) - Noto Sans JP and Hind Siliguri 
Font Styles
* [tinyjpg](https://tinyjpg.com/) - used to reduce image file sizes
* [Nu_html_checker] (https://validator.w3.org/) - html validator
* [JSHint](https://jshint.com/) - JavaScript validator that recognizes jQuery
* [JSDoc](https://jsdoc.app/) - for comments in JavaScript file
* [stackOverflow](https://stackoverflow.com/) - questions forum helped with
troubleshooting code

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Testing <a name="testing"></a>
Testing can be found in a separate file - [TESTING.md](TESTING.md)

<p>

[Back to Top](#Table-of-Contents)
</p>
---


## Deployment <a name="deployment"></a>
The following steps were taken to deploy my GitHub repository using Heroku.

### On Heroku website do the following:
1. Create an account or sign into an existing account
2. Click on "New" button and create a new app with a unique name
3. Click on Resources tab and then click on "Add-ons" and select
"Heroku Postgress" (free)

### In GitHub Repository do the following:
1. Install all required modules using "pip3" and additionally install the 
following modules for deployment: dj_dataabase_url, psycopg2-binary, gunicorn

4. Set up the postgress database in project level settings.py file:
* at top of file add "import dj_database_url"
* under "Database", comment out the existing Database settings
* add the following setting:
DATABASES = {
    'default': dj_database_url.parse('postgres://.....')
}
* save settings.py file with database changes
5. Connect to the new Heroku database by running migrations:
$python3 manage.py showmigrations
$python3 manage.py migrate
6. Import all product data into new database using fixtures files. For 
this website, three files were loaded:
$python3 manage.py loaddata categories
$python3 manage.py loaddata product-family
$python3 manage.py loaddata products
7. Create a superuser to log in to new database:
$python3 manage.py createsuperuser
and supply a username, email address and password
8. Before committing changes, change the database configuration so
database name is not in version control. Go to project level settings.py:
* add:
if 'DATABASE_URL' in os.env:
    DATABASES = {
        'default
: dj_database_url.parse(ps.environ.get('DATABASE_URL'))    
    }
else:
    DATABASES = {
        'default': {
            'ENGINE':  . . . .,
            'NAME':  . . . .
        }
    }
* add:
DEBUG = 'DEVELOPMENT' in os.environ
Development will be changed to False before moving site to production
9. Commit and push changes to repo
10. Review env.py file and make sure it is complete and listed in your 
.gitignore file:
* Format of entries should follow this example:
after listing "import os" at the top of the file:
os.environ.setdefault("DATABASE_URL_JANERIC", "postgres://mugoqqsebccccc:xxxxxxx")
* Ensure all important project variables are included, such as Secret Key, 
Stripe keys, and database url
* For each environmental variable, check to make sure the variable 
(such as API_KEY) is defined as follows in the project level settings.py 
file: API_KEY = os.environ.get('API_KEY').
11. Once all necessary modules are installed in repository and env.py file is
complete, create a Requirements.txt file listing all installed modules by 
typing the following into the terminal after the $ prompt: 
pip3 freeze --local > requirements.txt
12. Create Procfile at top level of repo and add the following text
at top of file: 
web: gunicorn {app name}.wsgi:application
13. Confirm both files have been added to the directory of the repository.
14. Temporarily disable collectstatic
$heroku login -i
provide heroku login email and password
$heroku config:set DISABLE_COLLECTSTATIC=1 --app {heroku app name}
15. Go to project level settings.py file and add host name of Heroku
app
ALLOWED_HOSTS = ['janeric.herokuapp.com', 'localhost']
16. Commit and push changes

### On Heroku website do the following:
3. Click on app name and then click on Settings in menu bar at top
of page
4. In middle of page, in "Config Vars" section, click on box that reads, 
"Reveal Config Vars"
5. Go to a django key generator website and obtain a django secret key
5. Go back to the Config Vars section with be "key" and "value" input boxes. 
For all applicable variables, such as Secret Key, database url, and Stripe 
secret keys, and Development(True): input key and value and click "add".
6. Once all variables have been input, click on "Deploy" in menu bar.
7. In "Deployment Method" section, click on "GitHub"
8. Under section heading "Search for a repository to connect to,"
type in repository name following GitHub display name and hit return
or the "Search" button.
9. The name of the repo found in GitHub will be printed below,
click on the "Connect" button across from it, if it is correct.
10. The app is now connected to the specified GitHub repository.
11. To enable automatic deployment, scroll down to "Automatic Deploys"
section and click on button "Enable Automatic Deploys."
12. In menu button, click on "Settings" and scroll down to section
titled "Domains" and you will find your domain address:
Your app can be found at 
[https://janeric.herokuapp.com/](https://janeric.herokuapp.com/)
13. After instigating automatic deployment, all changes committed
to the GitHub repository will be reflected in the deployed site on
Heroku.



### How to Run this Project Locally
To run the project locally, make a clone of it from GitHub:

1. Working from the GitHub repository page, find the green button on right 
labeled **Clone or download** and click it to open a dropdown menu.
2. Below the headline **Clone with HTTPS** is a web address, click on the 
button to the right of it to copy the link.
3. In your local IDE open Git Bash.
4. Change the current working directory to the location where you want to 
place the cloned directory.
5. Type ```git clone```, then paste the clone URL address copied in step 2 
as follows:
```console git clone https://sherylg343.github.io/thriller-books2/```
6. Press enter to finish creating the local clone.

<p>

[Back to Top](#Table-of-Contents)
</p>
---