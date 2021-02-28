
  

# Dark Castle Brewery - E-Commerce Web App With Craft Beer

  

![Showcase](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/img-intro.png)
  

Code Institute - Final Milestone Project (4) - Full Stack Frameworks With Django

 
Dark Castle Brewery is a multi-page e-commerce web application with a simple aim, the sale of artisan craft beer.

The application is aimed at lovers of craft beer, the overall styling and the name itself may appeal to fans of the fantasy genre.

  

The primary aim of this application is to purchase products which led to the decision to keep things simple. The store is currently small but has the potential to grow and the app has functions that make that easy to achieve including the ability to add products via the admin.  Although the majority of the admin activities is done through [the Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/), 
the web app also provides a more pleasant environment for common tasks such as adding, editing, and deleting products using the web app's UI.

  

Live at [https://darkcastlebrewery.herokuapp.com/](https://darkcastlebrewery.herokuapp.com/)

  

Test transaction details:

*  **credit card:** 4242 4242 4242 4242

*  **expiration date:** 04 / 24

*  **CVC:** 424

*  **ZIP:** 42424

  

A demo and/or admin credentials available upon request.

  

## Table of Contents

  

*  [**UX - research and goals**](#ux---research-and-goals)

+  [Conclusion of the Research](#conclusion-of-the-research)

+  [Business Goals](#business-goals)

+  [Customer Goals](#customer-goals)

*  [**Features and App Sections**](#features-and-app-sections)

+  [Web App Sections](#web-app-sections)

+  [Features and Django Apps](#features-and-django-apps)

+  [Features Left to Implement](#features-left-to-implement)

+  [Wireframes](#wireframes)

*  [**Information Architecture**](#information-architecture)

+  [Data Models](#data-models)

*  [**Graphic Design and Brand Elements**](#graphic-design-and-brand-elements)

+  [Fonts](#fonts)

+  [Colours](#colours)

+  [Icons](#icons)

+  [Images](#images)

+  [Visual Style](#visual-style)

*  [**Technologies Used**](#technologies-used)

*  [**Testing and Defensive Design**](#testing-and-defensive-design)

*  [**Deployment**](#deployment)

+  [Local Deployment](#local-deployment)

+  [Heroku Deployment](#heroku-deployment)

+  [Hosting Files with AWS](#hosting-files-with-aws)

+  [Sending E-mails through Gmail](#sending-e-mails-through-gmail)

*  [**Credits**](#credits)

+  [Content](#content)

+  [Media](#media)

+  [Inspiration Sources](#inspiration-sources)

+  [Coding Sources](#coding-sources)

+  [Acknowledgments](#acknowledgments)

  

## UX - research and goals

  

In 2012 we had only 15 breweries in Ireland, now we have over 70 and the range of beers being produced is growing constantly.

In 2019 we saw sales of Irish craft beer grow by approximately 18%, while we saw beer sales rise by only 2% (driven largely by low alcohol). The craft Beer market share has increased from 2.6% in 2017 to 3.4% in 2019.
Source: **https://www.bordbia.ie/industry/news/food-alerts/2020/the-irish-craft-beer-industry/**

Just go into any pub or off-license and you will see that there are many varieties of beers from breweries all over the world. To try and stand out from the crowd many companies will adopt clever packaging and names to get your attention.


The fantasy genre is also a massive industry thanks to the likes of The Lord of the Rings and Harry Potter. This is what inspired the design for the products. The marriage of craft beer fans with a love of the fantasy genre.

  
  

### Business Goals

As an e-commerce site owner...

  * I want the users to be comfortable with the brand identity so that they will want to buy products through my platform.

* I want to offer a shopping journey that is straightforward and gives the user the option of signing up to enable a speedier shopping experience on return visits.

* I want to be able to make changes to the inventory myself so that I don't have to rely on external support when it comes to that.


  
  

### Customer Goals

  

As a customer...

  

* I want to buy from a brand I can relate to in a simple straightforward way.

* I want to be able to read about the brewery to learn about the history. 
* I want to be able to contact the brewery if I had any questions regarding the products. 

* I want to be able to store my shipping details so that it’s easier for me to check out.

* I want to be able to see my orders so that I can track what I buy and spend money on.

  

As a loyal customer...

 * I want an opportunity to get to know the team behind this brand I buy so much from and other like-minded people so that I can see if my loyalty to the brand is a good investment.

  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Features and App Sections

  

Based on the user stories and UX research, I've created an overview of the most important features and information the web app should consist of. Darkcastlebrewery is a small e-commerce store selling one type of product therefore the decision was to keep things simple which is why the home page brings you directly to the product's page. 

  


  

In the next few sections, I will focus more on the most important sections and features, as well as additional features left to be implemented. The next step, described after this chapter, was choosing a database suitable to the project's needs and defining models.

  

### Web App Sections

  
1.  **Navigation at the top** - Fixed on the top so that the users can navigate themselves anytime. It consists of two HTML code snippets for better responsiveness handling.

1.  **Homepage** - The store is directly on the front page. This was done to keep things simple. The user is visiting the site intending to buy a certain kind of product and therefore is brought directly to the store.

1.  **Webshop** - Standard e-commerce feed of products with the ability to search for a particular product. Each product links to a product detail page where the user can read more about it.

1.  **Product page** - A page dedicated to an individual product. Consists of a product description. The product descriptions are written in a style that would fit into the fantasy theme. 

1.  **About Contact us page** - The about us / contact page includes some information regarding the history of the brewery and it also contains a form enabling users to send quires. 

  

1.  **User account** - Available to registered/logged-in users, it contains an order history and safely stores shipping details for a smooth checkout.

1.  **Admin account** - Available users with admin rights to have access to the orders, user profiles, as well as product inventory. The majority of the information is stored in [the Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/) but the users can also do common tasks such as adding, editing, and deleting products through darkcastlebrewery's UI.

1.  **Footer** - A button to view the shipping and returns detail is available on the footer. Clicking on it opens a modal. The footer also contains links to social media profiles, clicking on an icon causes a page to open in a new window.

  

### Features and Django Apps

  

darkcastlebrewery, [a Django project](https://docs.djangoproject.com/en/3.1/ref/applications/), consists of 6 Django applications listed below.

As explained in Django's documentation - a Django application describes a Python package that provides some set of features. Applications may be reused in various projects.

  
*  `homepage`

* `about``

*  `products`

*  `cart`

*  `checkout`

*  `profiles`

  

Some features I've worked on are available across the Django project, while others are tied to a specific Django application. The following list of features is structured in a way that should help with understanding how the features are spread throughout the project.

  

**Navigation**

* Always present on the top so that the users can navigate themselves anytime. It consists of **the top navigation** (a combination of a brand logo, search box, account-related activities, and the cart functionality) and **the main navigation** below it (for navigating throughout the main app sections).

* Navigation links are compressed into a hamburger menu on mobile and tablet devices so that the main focus of the user is the shopping cart in the top right corner at all times, and not the navigation links.

  

**Search functionality**

* The search box is part of the top navigation and is, therefore, accessible on all pages.

* it is collapsed under the hamburger menu on tablet and mobile devices as shown in the image above.

* It allows customers to enter keywords associated with the products they wish to purchase for example 'IPA', 'savage' etc.

* The search results are displayed as a feed of products by using the page templates prepared for the `products` Django app (i.e. webshop).

* The search results show the number of products found for the search query, if the item searched for is not available then the page will be blank.

  


**Toasts**

* 'Toasts' are small snippets of messages divided into 4 main categories: `toast_success`, `toast_info`, `toast_warning` and `toast_error`.

* They appear in the top right on every page whenever a certain action has been done by the user.

* The purpose is to give feedback on the action a user has just performed, such as logging in, logging out, adding a product to the cart, updating the cart, finishing the checkout process.

* It generally consists of the title based on the toast category with a matching text about the action. The `toast_success` toast additionally has cart information, that is hidden on `profiles` pages and for some other activities if nothing is added to the cart.

  



  

**Django-allauth feature**

*  `Django-allauth` is a Python package. As written in the [django-allauth docs](https://django-allauth.readthedocs.io/en/latest/), it is an "integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication."

* It provides a set of features such as **signup**, **login**, **logout**, and **password change**.

* After signing up, a verification e-mail is sent to the registered e-mail to confirm it. Once confirmed, the user can log in with their credentials and access the `profiles` app explained later below.

* Links to these features can be found in the navigation, under the **My Account** dropdown menu, as well as on the pages and throughout the web app (for example, registration prompt window on the `homepage`).

  


**Automatic e-mails**

* A Gmail account **darkcastlebrewery@gmail.com** has been created specifically for this project and used as a sender for all verification, reset, and confirmation e-mails.

* For example, users receive an **order confirmation e-mail** after a purchase, **account verification e-mail** after the registration, **password reset e-mail** after requesting a password reset, etc.

  



**Homepage app**

*  `homepage` Django app brings the customer directly to the store simplifying the process of purchasing products. The store sells one kind of product, the aim was to keep this simple.

  
  

**About app**

*  `about` Django app is one of the apps that are mostly relying on textual content.

* It features a piece on the history of the brewery.

* It also features a form to allow a user to contact the brewery with any questions or queries they may have.

  


  

**Products app, i.e. Webshop**

*  `products` Django app is where all the logic and templates connected to the product feed and individual products are.

* It can be divided into three main sections: **shop**, **product pages**, and **admin product management activities**.

*  **Shop** is the main feed of products and this is where the majority of shopping journeys are expected to start.

*  **Product pages** are pages dedicated to each product. On these pages, the users can **read the product description**

Users can also filter the products based on these tags in the **shop**.

*  **Admin product management activities** include adding, editing, and deleting products. Users with admin rights can do that directly in the UI through forms. In case of deleting a product, a **modal** will open to double-check if the user wants to do this irreversible action.

  



**Cart app**

*  `cart` Django app is a standard e-commerce functionality that aids the checkout process.

* A cart is always present in the top right corner of the web app. **It turns blueish-green if it's full and shows the number of items added to the cart and turns black when empty**.

*  **Adding products to the cart works differently on the product pages**. The users can define the exact amount of products they want to put into the cart as long as it's within the range (1 to 50). 


* Clicking on the cart in the top right corner, the user gets an overview of all the products put into the cart. The user can also modify the quantity of the added products as well as remove the products from the cart. Since removing products from the cart is not an irreversible action, I have decided not to have a modal here so that the focus remains on the checkout process.



* The information provided on this page includes **usual product information, quantity per product, costs per product, order costs** **shipping costs** (free for orders worth 100.00€ and above and **total order costs**.



  


  

**Checkout app**

*  `checkout` Django app is another standard e-commerce functionality that enables users to buy the products online from the webshop.

* To check out, the user is presented with a **form asking for the shipping and payment details** and with the **overview of the order**.

* Users can easily go back to the cart and adjust it by clicking on the cart in the top right corner or breadcrumbs in the top left corner.

* Both registered and anonymous users can shop at Dark Castle Brewery. Logged-in users will have an option to **save their information** to the profile which should populate the form with relevant details for the next purchase.

* A webhook is implemented to the `checkout` so that the order is successfully processed in case the checkout process gets interrupted. Some reasons might be closing the browser too soon or losing an internet connection.

* "payments" are handled through `stripe`. A test purchase can be made with the following details:

*  **credit card:** 4242 4242 4242 4242

*  **expiration date:** 04 / 24

*  **CVC:** 424

*  **ZIP:** 42424

* After the payment has been processed, the user is presented with the order summary on the **order confirmation page**.

* Logged in buyers can also see their **order history** on the `profiles` pages.

  


  

**Profiles app**

*  `profiles` Django app is available to register, authenticated users.

* it offers 2 features: **order history** and **saving shipping information**.

*  **order history** displays all previous orders per user account.

*  **saving shipping information** is done through a form that can be edited anytime. This information is what populates the checkout form for the next orders and where shipping information saved during the checkout process is stored.

  
  



### Features Left to Implement

  

Working on this project has been an incredible learning experience and I truly wish I had more time to implement many other features. Here are some I had in mind while working on the project:



**Contact page**

* The contact page features a form. Currently, the data is not sent anywhere. It would be helpful to have this form sent directly to the admin(s).

  



**Cart keeps items after logging out**

* A simple feature that would store what the user had in the cart before logging out.

* In combination with `toasts`, it would act as a reminder of what the user's last shopping-related action was. This would help to increase the conversion rate. 

 **Include a blog**

* A blog would be a great way to keep up to date with the day-to-day activities of the brewery and allow the customer to interact. 

 **Discounts for loyal customers**
 * Implement discounts for loyal customers. This could be possibly a points system in which a customer earns a certain amount of points depending on how much they have spent.  
  

**Product reviews**

* Another standard e-commerce feature that helps users with buying decisions. The idea would be to implement ratings and product reviews on product pages.

  
**Email newsletter**

* When a user signs up give them the option of receiving a newsletter weekly newsletter with personalized product recommendations.

  

### Wireframes

  

The wireframes linked below are only some that I've made for this project. They were created with [balsamiq](Balsamiq.cloud).

  

Desktop wireframes:

*  [Homepage / webshop](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Desktop%20products.png)

*  [About page](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Desktop%20About%20us.png)

*  [Product detail page](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Product%20detail%20page.png)

*  [Cart](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Desktop%20Shopping%20Cart.png)



*  [Folder with all desktop wireframes](https://github.com/Jammerref2015/Dark-Castle-Brewery1/tree/master/readme_files/wireframes)



Mobile wireframes:

*  [homepage /webshop](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Mobile%20home%20page%202.png)

*  [about page](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Mobile%20about%20us.png)

*  [product detail page](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Mobile%20product%20detail.png)

*  [cart](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/wireframes/Mobile%20product%20detail.png)



*  [Folder with all mobile wireframes](https://github.com/Jammerref2015/Dark-Castle-Brewery1/tree/master/readme_files/wireframes)
  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Information Architecture

  

As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment.

  

### Data Models

  

**User Model**

  

Django `User` model is a part of Django’s authentication system `Django.contrib.auth.models`. You can read more about its fields, attributes,

methods, etc. [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

  

**Profiles App**

  

`UserProfile` model

  

| **Name** | **Database Key** | **Field Type** | **Type Validation** |

| ---------- | ------------------ | ---------------- | --------------------- |

| User | user | OneToOneField 'User' | on_delete=models.CASCADE |

| Default Phone Number | default_phone_number | CharField | max_length=20, null=True, blank=True |

| Default Country | default_country | CountryField | blank_label='country', null=True, blank=True |

| Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True |

| Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True |

| Default Street Address | default_street_address | CharField | max_length=80, null=True, blank=True |

  
  

**Products App**

  

`Category` model

  

| **Name** | **Database Key** | **Field Type** | **Type Validation** |

| ---------- | ------------------ | ---------------- | --------------------- |

| Name | name | CharField | max_length=254 |

| Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True |



`Product` model

  

| **Name** | **Database Key** | **Field Type** | **Type Validation** |

| ---------- | ------------------ | ---------------- | --------------------- |

| SKU | sku | CharField | max_length=254, null=True, blank=True |

| Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL |

| Name | name | CharField | max_length=55 |

| Description | description | TextField | max_length=375 |

| Price | price | DecimalField | max_digits=6, decimal_places=2 |

| Rating | price | DecimalField | max_digits=6, decimal_places=2 |  null=True|blank=True
  

**Checkout App**

`Order` model


| **Name** | **Database Key** | **Field Type** | **Type Validation** |

| ---------- | ------------------ | ---------------- | --------------------- |

| Order Number | order_number | CharField | max_length=32, null=False, editable=False |

| User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |

| Full Name | full_name | CharField | max_length=50, null=False, blank=False |

| E-mail | email | EmailField | max_length=254, null=False, blank=False |

| Phone Number | phone_number | CharField | max_length=20, null=False, blank=False |

| Country | country | CountryField | blank_label='(select your country)', null=False, blank=False |

| Town or City | town_or_city | CharField | (max_length=40, null=False, blank=False |

| Postcode | postcode | CharField | max_length=20, null=False, blank=False |

| Street Address | street_address | CharField | max_length=80, null=False, blank=False |

| Date | date | DateTimeField | auto_now_add=True |

| Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |

| Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |

| Order Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |

| Original Cart | original_cart | TextField | null=False, blank=False, default='' |

| Stripe PID | stripe_pid | CharField | max_length=254, null=False, blank=False |

| Loyalty Points | loyalty_points | DecimalField | max_digits=10, decimal_places=0, null=False, default=0 |

 

`OrderLineItem` model


| **Name** | **Database Key** | **Field Type** | **Type Validation** |

| ---------- | ------------------ | ---------------- | --------------------- |

| Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |

| Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE |

| Quantity | quantity | IntegerField | null=False, blank=False, default=0 |

| Line Item Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |

  
 

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Graphic Design and Brand Elements

  

The target audience identifies both craft beer and the fantasy genre.

As a lover of craft beers myself I was aware of the many fantastical design elements some craft beer breweries employ to grab potential customers when on the shelf such as bright colours, loud graphics along with an attention-grabbing product name. I had to be aware of what kind of product packaging and web design guidelines competitors and cosmetic companies are following. Since my marketplace is going to have those products, my design had to match them


Two brands/breweries were a huge inspiration for my design - the fantasy theme used by [wychwood brewery](https://www.wychwood.co.uk/) and the colourful products [Brasserie Goudale](http://brasserie-goudale.com/) sell.

I decided on four product types and each one would need to be very different in terms of styling. They all use the same frame styling which helps tie the brand together but the images used are very different. I also wanted the cans to be very different in colour.

  
  
  



  

### Fonts

I have come across [Cinzel](https://fonts.google.com/specimen/Cinzel?preview.text_type=custom) by browsing through Google fonts. I was looking for a font that would fit the fantasy theme of the store. 
  

### Colours

My colour selection for this project was very simple. I've chosen a dark shade of blue (#2D4059) for the background. In a contrast to it, a darker shade of yellow (#FFB400) has been chosen for the header and footer.

The text uses a very slightly off-white color (#F6F6F6) which contrasts nicely with the colour used for the background.

Red is used on the important shipping and returns the button to enable it to stand out against the colour of the footer.

  



### Icons
The icons used in the app are from font awesome and they are used to make it clear as to what their functions are. I.E shopping cart uses a 'cart' icon.

  

### Images

 As the products for sale in this store do not exist I had to create them myself in Photoshop using a variety of sources. Each of the different products having a different colour scheme and image style based on the name and the type of beer that would allow them to stand out on the shelves.
 
![Products](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/readme_files/Cans_multi.jpg)


### Visual Style

  

The goal of this store is to provide a straightforward shopping experience for the target audience who are craft beer aficionados and also have a liking for the fantasy genre.

  

The colour palette was brought to my attention via a post on Instagram and I felt that it would suit the theme of this store. The colours being designed to work together. The font choice is inspired again by the fantasy theme.

  

The store needs to be clutter-free and easy to navigate. The product cards incorporate shadows to give a 3D effect that 'lifts ' them off the page.

  

The 'about' page features a photo of two pets. The idea is that the artwork on the labels features fantasy cats and dogs and they were inspired by the store owner's pets! It also provides customers with a little history of the brewery.

  
  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Technologies Used

  

This project mostly focuses on the following technologies:

  

1.  [HTML](https://en.wikipedia.org/wiki/HTML) - for creating the layout and the structure of the website

1.  [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - for styling the website’s HTML code

1.  [Bootstrap](https://getbootstrap.com/) - for additional styling and adding responsiveness to the website

1.  [JavaScript](https://en.wikipedia.org/wiki/JavaScript) and [jQuery](https://jquery.com/) - for frontend interactivity

1.  [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - for backed logic and structure

1.  [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - for displaying backend information in frontend

1.  [Django](https://www.djangoproject.com/) - high-level Python web framework

1.  [Heroku](https://www.heroku.com/) - cloud platform where the web app is deployed

1.  [SQLite](https://www.sqlite.org/index.html) - default Django's database used in development

1.  [PostgreSQL](https://www.postgresql.org/) - production database through Heroku

1.  [AWS S3](https://aws.amazon.com/) - for hosting media and static files to the cloud

1.  [Git](https://git-scm.com/) - for version control

1.  [Stripe](https://stripe.com/en-gb-de) - for managing (test) transactions

  

[Bootstrap](https://getbootstrap.com/) uses the following components to function properly:

  

1.  [jQuery](https://jquery.com/)

1.  [Popper.js](https://popper.js.org/)

1.  [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

  

Additionally, I have also used the following platforms to help me shape the website and the brand:

  

1.  [Gitpod](https://gitpod.io/) - for writing, editing, and live to preview the code during the creation process

2.  [GitHub](https://github.com/) - for hosting the project's repository

3.  [TinyJPG](https://tinyjpg.com/)- for compressing the images so that the website can load faster

4.  [Google Fonts](https://fonts.google.com/) - for selecting the fonts

5.  [Favicon](https://favicon.io/) - for creating browser tab icons

6.  [Autoprefixer](https://autoprefixer.github.io/) - for solving cross-browser CSS issues
7. [Grammarly](https://www.grammarly.com/) - for spell checking and grammar for MD files.

  
  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Testing and Defensive Design

  

More about **Testing and Defensive Design** can be found in the [TESTING.md](https://github.com/Jammerref2015/Dark-Castle-Brewery1/blob/master/TESTING.md)file.

  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Deployment

  

darkcastlebrewery was developed with [Gitpod](https://gitpod.io/) IDE. [Git](https://git-scm.com/) was used for version control and [GitHub](https://github.com/) for hosting the project's repository. The project is hosted on [Heroku](https://www.heroku.com/) while [AWS S3](https://aws.amazon.com/) is hosting static files and images.

  

### Local Deployment

  

To run this project locally (on your IDE), make sure you:

* have an IDE of your choice ready (such as [Gitpod](https://gitpod.io/))

* have the following installed:

*  [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

*  [Python3](https://www.python.org/downloads/)

*  [pip](https://pip.pypa.io/en/stable/installing/)

  

Additionally, you will need (free) accounts of the following services:

*  [Gmail](https://www.google.com/gmail/)

*  [Stripe](https://stripe.com/en-gb-de)

*  [AWS S3](https://aws.amazon.com/)

  

**Instructions**

  

1. Clone this repository

* After installing the requirements mentioned earlier, clone the project by pasting the following command into the terminal:

*  `git clone https://github.com/Jammerref2015/Dark-Castle-Brewery1`

* alternatively, you can go to [darkcastlebrewery](https://github.com/Jammerref2015/Dark-Castle-Brewery1), repository then click the green 'Code' button and 'Download ZIP option in the dropdown menu to save the files on your machine, for more information please visit [GitHub's help pages](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

  

2. Set up environment variables

* create `.env` file in the root directory

* add `.env` to `.gitignore` file in the root directory

* add the following environment variables to `.env`:

```bash

import os

os.environ["DEVELOPMENT"] = "True"

os.environ["SECRET_KEY"] = "<Your Key>"

os.environ["STRIPE_PUBLIC_KEY"] = "<Your Key>"

os.environ["STRIPE_SECRET_KEY"] = "<Your Key>"

os.environ["STRIPE_WH_SECRET"] = "<Your Key>"

```

* if you're working with GitPod, you can set these variables in the 'Settings'

* click your profile icon in the top right corner in Gitpod

* click 'Open Workspaces'

* again click your profile icon in the top right corner

* click 'Settings' option in the dropdown menu

* click 'Add Variable' button to add a variable

  

3. Install requirements from the `requirements.txt` file

* paste the following command into the terminal:

*  `pip3 install -r requirements.txt`

  

4. Migrate the models to create a database

* paste the following commands into the terminal:

*  `python3 manage.py makemigrations`

*  `python3 manage.py migrate`

  

5. Load the data fixtures in this exact order

* paste the following commands into the terminal:

*  `python3 manage.py loaddata products`

  

6. Create a superuser (user with admin rights)

* paste the following command into the terminal:

*  `python3 manage.py createsuperuser`

* enter an e-mail, username, and password for the superuser

  

7. Run the web app

* paste the following command into the terminal:

*  `python3 manage.py runserver`

  

8. Log into Django admin

* after running the web app, add `/admin` at the end of the URL and log in with the superuser credentials from the previous step

  

### Heroku Deployment

  

1. Create a `requirements.txt` file

* paste the following command into the terminal:

*  `pip freeze > requirements.txt`

  

2. Create a `Procfile`

* create a `Procfile` in the root directory

* add the following code into it:

*  `web: gunicorn dark_castle.wsgi:application`

  

3. Push the code to GitHub

* paste the following commands into the terminal:

*  `git add .`

*  `git commit -m "<your commit note>"`

*  `git push`

  

4. Create a new app on Heroku

* create a new app (click on 'New' > 'Create new app')

* give it a unique name

* set region closest to you

  

5. Set Heroku Postgres

* go to 'Resources' tab

* search for 'Heroku Postgres'

* Select the 'Hobby Dev' free plan

  

6. Set config variables in Heroku

  

| **Key** | **Value** |

| --------- | ----------- |

| AWS_ACCESS_KEY_ID | < your AWS access key ID > |

| AWS_SECRET_ACCESS_KEY | < your AWS secret access key > |

| DATABASE_URL | < your postgres database URL > |

| EMAIL_HOST_PASS | < 16-character password from Gmail > |

| EMAIL_HOST_USER | < your Gmail > |

| SECRET_KEY | < your secret key > |

| STRIPE_PUBLIC_KEY | < your stripe public key > |

| STRIPE_SECRET_KEY | < your stripe secret key > |

| STRIPE_WH_SECRET | < your stripe webhook key > |

| USE_AWS | True |

  

7. Set up a new database

* in `settings.py`:

* import dj_database_url

* comment out `DATABASES` (temporarily, **do not commit/push this code to GitHub until instructed so**)

* add the following code:

```bash

DATABASES = {

'default': dj_database_url.parse("<your Postrgres database URL>")

}

```

  

8. Migrate the models to the Postgres database

* paste the following commands into the terminal:

*  `python3 manage.py makemigrations`

*  `python3 manage.py migrate`

  

9. Load the data fixtures in this exact order

* paste the following commands into the terminal:

*  `python3 manage.py loaddata categories`

*  `python3 manage.py loaddata brands`

*  `python3 manage.py loaddata products`

*  `python3 manage.py loaddata blogs`

  

10. Create a superuser (user with admin rights)

* paste the following command into the terminal:

*  `python3 manage.py createsuperuser`

* enter an e-mail, username, and password for the superuser

  

11. Correct the `settings.py` database from step 7.

* uncomment the `DATABASES`

*, remove the code added in step 7.

  

12. Add the hostname of Heroku app to allowed EMAIL_HOST_USER

* in `settings.py`:

* add the following code:

```bash

ALLOWED_HOSTS = ['<your Heroku app URL>', 'localhost]

```

  

13. Push the code to GitHub

* paste the following commands into the terminal:

*  `git add .`

*  `git commit -m "<your commit note>"`

*  `git push`

  

14. Set up automatic deployment to Heroku (**optional**)

* in Heroku go to 'Deploy' > 'Deployment method' > 'Connect to GitHub'

* search for your repository and click on it

* go to 'Automatic Deployment' > click 'Enable Automatic Deploys'

  

15. Test automatic deployment

* your code should be automatically deployed to Heroku after pushing your code

  

### Hosting Files with AWS

  

To host static files and images with AWS, you will need to create an [AWS account](https://aws.amazon.com/).

Additionally, you have to create:

* an AWS S3 Bucket

* a Bucket Policy

* a Group

* an Access Policy

* a User

  

It is a lengthy process but you can learn more about Amazon Simple Storage Service [here](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html).

After that, you will need to [connect Django to S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

  

### Sending E-mails through Gmail

  

To send automatic e-mails with Django, you need a Gmail account.

* go to the account settings

* go to the 'Other Google Account Settings'

* go to the 'Security' tab

* turn on 2-step verification

* go back to the 'Security' tab and click on 'App passwords'

* select 'Mail' in the app dropdown

* select 'Other' in the device dropdown

* Copy the 16-character password

* go to Heroku and put it under `EMAIL_HOST_PASS` config variable

* put the Gmail e-mail under the `EMAIL_HOST_USER` config var

  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Credits

  

### Content

  

* Product specifications were taken from various sources and adapted to better fit the theme of the products.

* Textual content for the About page is original, written by myself.

* Shipping and returns information adapted from other sources.

  

### Media

  

* The images for the products were created in photoshop using the following sources:

* Beer bottle and beer can mockups from [Smarty mockups](https://smartymockups.com/).

* Fantasy images are from the [realmsofpugmire](https://www.realmsofpugmire.com/) role-playing game.

* Labels created using label created in [beerlabelizer](https://www.beerlabelizer.com/).

* Social media icons in the header and footer are from [ Font Awesome](https://fontawesome.com/).

* README hero image was taken with the help of [Ami.ResponsiveDesign](http://ami.responsivedesign.is/).

  

### Inspiration Sources

  

* The biggest three inspiration sources were [Supply](https://www.wychwood.co.uk/) , [ [beerofbelgium]](https://www.beerofbelgium.com/en/) and [Brasserie Goudale](http://brasserie-goudale.com/).

* An important part of my design and research was also [Amazon](https://www.amazon.com/).

  * The following page helped me understand [webhooks](https://zapier.com/blog/what-are-webhooks/).

 

### Acknowledgments

* Thank you [CodeInstitute's](https://codeinstitute.net/) Tutors and Slack community for being there and helping with the many bug-related questions. I look forward to continuing being a member of the Slack community as alumni and hopefully being able to help others as well as being part of the growing band of coders on there!

* A huge thank you to Cat for the detailed feedback as well as the name suggestions for the products.

* Last but not least, a huge and warm thank you to my mentor [Caleb Mbakwe](https://github.com/caleboau2012)- for being such an incredible source of encouragement and advice on this project but for being there throughout all of my projects and coding journey at CodeInstitute. Thank you for all your support and kind words and for reassuring me when I felt that something wasn't clicking for me. 

   

<div align="right">

<a href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

> Written with [StackEdit](https://stackedit.io/).
