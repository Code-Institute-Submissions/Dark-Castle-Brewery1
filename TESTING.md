
  

Design

  

## Table of Contents

  

*  [**Defensive Design and Predicted Error Points**](#defensive-design-and-predicted-error-points)

+  [Custom Error Webpages](#custom-error-webpages)

+  [Secured Admin Views](#secured-admin-views)

+  [Modals When Permanently Deleting Data](#modals-when-permanently-deleting-data)

+  [Search Queries Safe for Site Structure](#search-queries-safe-for-site-structure)

+  [Maximum Items per Order - 150](#maximum-items-per-order---150)

+  [Maximum Same Products per Order - 99](#maximum-same-products-per-order---99)

+  [User-Friendly Product Page Input](#user-frienly-product-page-input)

+  [Cart Adjustments](#cart-adjustments)

+  [Product and Blog Images](#product-and-blog-images)

+  [Manipulating Loyalty Points Donation](#manipulating-loyalty-points-donation)

*  [**Testing**](#testing)

+  [Testing the Features](#testing-the-features)

+  [User Testing Results](#user-testing-results)

+  [Bugs, Problems and Vulnerabilities](#bugs--problems-and-vulnerabilities)

  

## Defensive Design and Predicted Error Points

  

In this chapter, I will focus more on which steps I've taken to prevent predicted errors and complications. In the beginning, I focused

more on the actions that could break the site or site structure completely, and afterward more on restrictions that would make

sense for this project in general.

  
  
  

### Secured Admin Views

* Admin-related activities happening on the site, such as adding, editing, and deleting products or blog posts - are secured for superusers

* If a user still tries to access those pages, they are redirected to the homepage with a toast saying that only darkcastlebrewery team is allowed to do these actions

* This has achieved by:

* importing `@login_required` decorator in `views.py` files

* redirecting to the homepage

* displaying error toast message

  

### Search Queries Safe for Site Structure

* Firstly, if the query is an empty string, users are redirected to the webshop with a toast message

* long search queries without white spaces, or search queries that are simply too long, could break the site's responsiveness and structure so to prevent this the following actions have been taken:

* search box `<input>` is restricted to `maxlength="50"`

  

### User-Friendly Product Page Input

* Validation is in place to prevent a user from entering a number higher than 50 at a time. Previously it was possible to enter some infinite lengths.

* However there is currently no limit on the quantity amount one can add to the cart.

  

### Cart quantity updating

* A max number of 50 has been applied to the quantity field.

* This field is now also required to prevent a user from trying to update the cart with an empty field which resulted in Django error.

  
  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  

## Testing

  

The project's code was frequently validated through:

  

*  [W3 HTML validator](https://validator.w3.org/)

	* The validator found some mistakes that were easy to fix, such as:

	* Incorrect `<footer>` tag had <footer">

	* Had some nnecessary type attribute `<script type="text/javascript">`

  

	* The following were not fixed due to the pressure of time.

	*  `<a>`is not allowed as child of element < ul > in this context.

	*  `<li>`is not allowed as child of element < nav > in this context x2.

	* Duplicate **id="user-options"** occurred because of additional implementation of custom widget template code. The pages for this app are built using code from the various apps (cart, products, etc) so there is some overlap which could explain the duplicate id's

	* A stray `<a>` tag was found.

	* The **aria-labelledby** attribute must point to an element in the same document.

*  [W3 CSS validator](https://jigsaw.w3.org/css-validator/)

	* Base.css was tested. No errors were found.

	* Checkout.css was tested. No errors were found.

*  [JSHint](https://jshint.com/)

	* stripe_elements.js was tested. No errors were found. Two warnings about 'template literal syntax' only available in ES6.

	* countryfield.js was tested. No errors were found. One warning about 'let' is available in ES6.

	* The script in quantity_input_script.html was tested. No errors. Three warnings about 'template literal syntax' only available in ES6.

	* Note:1 ('$' was not defined by JSHint however)

*  [PEP8 validator](http://pep8online.com/)

	* All Python code was run through the PEP8 validator

	* Most of the errors were `line too long`, `blank line contains whitespace`, and `blank line at end of file errors`, which I plan to correct at a later point since this isn't technically an error and this task would be very time-consuming at this point

  

The web app was tested on the devices and browsers listed below. I loaded the page on each of the device and browser combinations and looked for any visual and functional errors. I've also tried to resize the web pages on a desktop in Chrome, Firefox, Opera, and Safari developer tools to look for hidden irregularities and finding out the solutions. More about the errors I've encountered can be found under the 'Bugs, Problems and Vulnerabilities' section.

  

Desktop:

  

* iMac

* Google Chrome

* Safari

* Opera

* Firefox

  

Mobile:

  

* iPhone 6

* Safari

* Various android mobile phones

* Google Chrome

  

### Testing the Features

  

**Navigation**

* Clicked on all links to see if they work properly:

* Clicking on social links opened new windows as intended.

* Clicking on 'Important Shipping & Returns' info opened the modal as intended.

* Clicking on the cart icon to see if it's linked properly. Opened the cart page as intended.

* Clicking on 'About - Contact' to see if it's linked properly. Opened 'About - Contact' page as intended.

* Clicking on the logo returns you to the home page. Works as intended.

* Clicking on a product opens a product detail page. Works as intended.

  

* Clicking on 'My Account' to test that the different operations were available depending on wheater a user was registered/logged in and if the user was a superuser:

##### Not registered / logged in

* Clicked on 'My Account' presented two options:

* Register: Clicking on this link opened the sign-up page as intended.

* Login: Clicking on this link opened the sign-in page as intended.

##### Logged in as superuser

* Clicked on 'My Account' presented three options:

* My Profile: Clicking on this link opened the profile page. The page contained my profile information in a form that could be edited as well as order history.

* Logout: Clicking on this link opened the sign-out page as intended.

* Product Management: Clicking on the link opened the product management page as intended.

##### Logged in as user

* Clicked on 'My Account' presented two options:

* My Profile: Clicking on this link opened the my profile page. The page contained my profile information in a form that could be edited as well as order history.

* Logout: Clicking on this link opened the sign-out page as intended.

  
  
  
  
  

* Added a product into the cart to see if the cart changes to color to illustrate that a product(s) are in the cart and that it displays the correct price. Works as intended.

Resized the browser to see if the navbar collapsed into the hamburger menu. Works as intended. Clicking on the hamburger menu presented two links. To the about page and home. Clicked on both. Worked as intended.

* Scrolled up and down to see if the navbar is fixed on the top. Worked as intended

  
  

**Search functionality**

* Searched for a relevant keyword (stout) to see if the search results are rendered properly on the page and the site structure is intact. Relevant products appeared as intended.

* Searched for an irrelevant keyword (dog) to see if the page without results is rendered properly and the site structure is intact. The result was an empty product page. Worked as intended.

* Tried to type an input longer than 50 characters to see if the search bar limits your input. Worked as intended.

* Searched by submitting an empty field to see if you get redirected to the webshop with a toast message that nothing was submitted. Error toast appeared as intended. Redirected to store/home page if on another page.

* Tried to manipulate the link in the browser by adding more than 50 characters at the end of and pressing enter key to see if the search results are rendered properly on the page and the site structure is intact. This resulted in an empty products page. Works as intended.

  
  

**Toasts**

* Completed various actions to see if the toast message appears in the top right corner.

* Submitted an empty search in the search bar. This resulted in an Error toast displaying.

* Adding a product to the cart resulted in a 'Success' toast displaying containing cart products, prices, and link to cart page

* Add more than 99 same items to the cart. Success toast appeared with an updated cost.

* Added more than 150 products to the cart. Success toast appeared with an updated cost.

* Updated the products in the cart. Success toast appeared with a notice confirming cart update.

* Removed an item from the cart. Success toast appeared with a notice confirming product removal from the cart.

* Completed a checkout. Success toast appeared confirming my order successfully processed along with order confirmation.

* Logged in. Success toast appeared confirming that I had signed as my user name.

* Logged out. Success toast appeared confirming that I had signed out.

* (As superuser) Edit product. A toast appeared with an alert regarding the editing of a product.

* These actions were also tested on mobile devices.

  

**Django-allauth feature**

* Clicked on 'My Account' > 'Register'.

* Entered incorrect email address x2 resulted in an alert when the 'Sign up' button was pressed.

* Entered correct email address x2.

* Entered a unique username.

* Entering two different passwords resulted in a message warning that the passwords must match.

* Entered a unique password x 2.

* Clicked on 'Sign Up'.

* Clicking 'Sign up' with the correct information provided resulted in a 'Verify your email address page' opening.

* Checked email account to see if a verification e-mail had been sent. It had done.

* Opening the email, it contained a link to verify my account. Clicking on it brought me to a page asking me to confirm that the email address I supplied was the address for the user name I had selected.

* Clicking on confirm brought me to the log-in page.

* Logging in using my details brought me to the home page. A 'success' toast appeared to tell me I was successfully logged in.

* Clicked on Logout.

* This brought me to a page asking me to confirm if I wanted to sign out.

* Clicking on cancel brought me to the home page.

* Clicking on sign out signed me out of the site and a toast appeared alerting me of that fact.

  

* Forgot password? feature.

* Opened the Sign In page and clicked on 'Forgot Password.

* Entered the email address I used to create an account.

* A notice telling me that an email had been sent.

* Opening the email it contained a message alerting me to the password request along with a link to click.

* Clicking the link resulted in a 'Change Password' page loading.

* Entered the following password 'Cat' x2 resulted in a notice telling me that the password is too short and that it is too common.

* Entered a legal password twice resulted in a 'Your password is now changed' notice.

* Logged in using new credentials brought was successful.

  
  

**Automatic e-mails**

* To test automatic emails, the following actions were completed:

* Made a test order. Received an email confirming the order along with order information.

* Registered for an account. Received an email with a link to confirm. Clicked on the link brought me to the confirm email address page as intended.

* Reset my password

* Each resulted in the receiving of an email from 'darkcastlebrewery@gmail.com'

  

**Homepage app**

* Clicked on the logo in the navigation and see if the page renders properly

* Products are displayed via bootstrap cards in order of 'title'.

* Clicked on various products. Each one brought me to the correct details page for that product.

* Clicked on shipping info button opened a modal. Clicking on 'close' closed it.

  

**About app**

* Clicked on the 'About' link in the navigation. Page rendered properly

* Completed the contact us with correct data. Alert displayed as intended.

* Tried to complete contact us form with missing information, alerts appeared informing that said data was missing.

* Resized the page to test that everything displayed as intended.

  
  

**Products app, i.e. Webshop**

  

**Cart app**

* Clicked on the cart icon in the navigation resulted in the cart page opening.

* If the cart was empty the text 'Your cart is empty' was displayed along with a button to keep shopping'. Clicking on that returned to the home/store page.

* If one or more items were in the cart the product(s) were displayed with an image(s), and product info.

* Tested adding and removing products from the cart:

* Removing all items from the cart resulted in the following:

* The text 'Your cart is empty' was displayed along with a button to keep shopping'. Clicking on that button returned to the home/store page.

* The cart icon on the header changed back to black and the value 0.00.

* Updating a product:

* Increased the qty of a product by 1 and clicked update. A success toast appeared with updated cart details.

* The value below the cart icon was updated to reflect the price change.

* Checked that the data per line item is correctly displayed the price and calculated.

* Tried to click on `+/-` input buttons in the input field to see if you can adjust the quantity of the product. Increased the quantity by 5 and clicked update. Cart updated as intended.

* Tried typing in a number within the range 1-50 and see if you can adjust the quantity of the product with a success toast displayed. Works as intended.

* Tried typing a number higher than 50 and see if you get an error toast message. Form validation currently prevents a user from inputting a number higher than 50

* Tried submitting an empty input and see if you get an error toast message. Form validation is in place to prevent submission with an empty field.

* Tried updating a product without adjusting the quantity and see if you get a toast message as a reminder. Toast appeared as intended.

* Resized the cart page and see if everything looks all right. Everything displayed as intended.

* Scrolled to the bottom of the page to see if the costs are displayed properly there should be order total, shipping costs and total costs were correctly calculated

* if the order is worth 100.00€ or more, the shipping costs are free

* if the order is worth less than 100.00€, the shipping costs are 20% of the overall cost of the product(s)

  

**Checkout app**

* Clicked on the 'Checkout' button at the bottom of the cart page.

* Checked to ensure that the correct order details were present and that the totals were correctly calculated.

* Resized the checkout page and see if everything looks all right at different sizes.

* Attempted to submit a form with some of the input fields empty. Error popups appeared as intended to alert that the various fields required the correct information.

* Filled in the form as an anonymous user and did a test transaction.

* Order was successful.

* The Thank you' page is loaded with the correct order details.

* A toast message also appeared telling me that my order was successful.

* Email had been sent containing the details of my order.

* Order was listed in admin/Orders

* Webhook attempts on the Stripe dashboard were successful.

*  **credit card:** 4242 4242 4242 4242

*  **expiration date:** 04 / 24

*  **CVC:** 424

*  **ZIP:** 42424

  

* Filled in the form as a logged-in user and checked the 'Save this delivery information to my profile' box

* Completed a successful test transaction and went to the 'my profile' page. Order details were present.

* Filled in the form as a logged-in user and unchecked the 'Save this delivery information to my profile' box

* Completed a successful test transaction and went to the 'my profile' page. Order details were present.

  
  

**Profiles app**

* Registered for an account and logged in by clicking on the 'Login' link in the 'My Account' dropdown in the top right of the navigation (in the hamburger menu on mobile devices)

* Checked to see if the page renders properly - you should be seeing 2 buttons linked to:

* Order history page ('My Profile' CTA)

* Loyalty status page ('Check Loyalty Status' CTA)

* Edit profile page ('My Profile' CTA)

* Product management (If superuser)

* Clicked on each CTA to see if the pages render properly.

* Resized each page and see if everything looks all right

* the order history page should display your orders - if you haven't made any orders yet, you should see a CTA to the webshop.

* The edit profile page should display your saved information such as delivery information and order history.

* Changed the information and saved it to see if everything gets saved properly.

* A toast appeared to inform that the change was successful.

* Tested the form with empty fields. A toast appeared to inform that the change was successful.

* Completed a test transaction to check if the new details were correctly displayed in the checkout form. Worked as intended.

  

**Product detail page**

* Clicked on a random product.

* Product page loaded with correct information.

* Edit / Delete options were available if signed in as superuser otherwise not present.

* Tested the quantity field.

* Clicking the - it was not possible to go lower than 1.

* Clicking the + it was not possible to go higher than 99.

* On the desktop is was possible to delete the figure which caused an error if add to cart was pressed. **See bugs**

*Added a quantity 1. The cart was updated. Worked as intended.

  

**Adding / deleting products**

* Signed as superuser I began with testing product add:

* Entered details for a new product without an image. 'No image' placeholder was loaded.

* Entered details for a new product with an image. Image loaded as intended.

*To delete the test product I clicked the delete button. The product was deleted. Toast appeared to alert me of this.

  

### User Testing Results

  

Apart from my efforts, the web app was tested by my friends and family members. The feedback was in general highly positive.

  

* Some small issues were discovered regarding UX.

* Products were displayed in random order. This was corrected by sorting the products by name.

* App was lacking shipping and return info. A modal popup was created to meet this need.

* Had an issue in which address 2 was outputting address 1 text and therefore repeating address 1. This was easily corrected. Address 1 and 2 now display the correct information.

* On mobile the cart information page was difficult to navigate. Adding some media queries addressed this issue.

  
  
  
  

I received some suggestions that I would have loved to implement but they would require more time, bigger code refactoring, or simply careful and detailed planning to achieve them.

  

Since none of these were bugs or errors and all my testers were able to navigate/use the app without the need for instruction I decided to leave them now to perhaps return to the app at a later date to finetune it further.

  

See the **README** for features I would like to add in the future.

  
  

### Bugs, Problems, and Vulnerabilities

  

## Bugs

  

### Cart

**Cart quantities**

* Had a bug in which a user could enter a possibly high number in the search field which could result in misuse

* The following code in cart.html was removed:

**// Update quantity on click

$('.update-link').click(function(e) {

var form = document.getElementById("form-update");

console.log(form);

if (form.reportValidity()){

form.submit();

}

});**

* In cart-quantity.html the - and + buttons were removed. The user can input an amount.

* The link to 'update' was replaced with an update button.

* HTML5 validation was placed on the input which had a min of 1 and a max of 50.

* An error occurred if you tried to update the card with an empty field. The solution used to prevent this was form validation. Trying to update with an empty field caused an alert to appear as did to try to enter a number greater than 50.

* It is still possible for a user to add an unlimited amount of a product(s). It might be a good idea to put some kind of limit to prevent this.

**Webhooks / emails**

  

* Had an issue that resulted in two emails being simultaneously being sent when a sale was completed. The email would be for the same order but the second email had a different order number and the pricing added various digits to the totals. Thanks to advice from a tutor I was able to discover what was happening.

* In **webhook_handler.py** I had two repeating lines of code which resulted in two emails being generated. Removing the second **self._send_confirmation_email(order)** resulted in just the one email sending. With the correct order information.

  

**Cross-Browser CSS Issues**

[Autoprefixer](https://autoprefixer.github.io/) was used to generate browser prefixes to ensure cross-browser compatibility.

  

**Login as superuser**

* Had an issue in which I could not log in as a superuser in Heroku.

* Solution was found on the slack group.

* I created a new Heroku-specific superuser and I was able to log in.

  

**iPhone specific cart details**

* When viewing the shopping cart on an i phone the credit card details field could get muddled making it impossible to read the text**

  
  

<div  align="right">

<a  href="#table-of-contents"> ⇧ Back To Top </a>

</div>

  
  

> Written with [StackEdit](https://stackedit.io/).