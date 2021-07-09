
# Honeybee Bakery
# About the Project

Honeybee Bakery is small bakery that sells three muffins. Customers shop from the bakery. They can create, edit, and delete their orders once logged in. This also can work as an order management system for the bakery to update order status of each customer.

![HoneyBee-Img1](https://user-images.githubusercontent.com/85468988/125085487-7b5b9500-e07f-11eb-88c0-7711fb29a7c1.png)
Click [here](https://honeybeebakery.herokuapp.com/) to go to the site, hosted on Heroku. 

## Login Instructions: 
To login as a user, log in using user123 with the password of aaaaqqqq1111, or create your own account. 



## Technologies Used


* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [JavaScript](https://www.javascript.com)
* HTML
* CSS



## Existing Features


* Home page with clickable image and logo.
* Clickable navigation bar for Home, About, Shop, Log In/Log Out, View My Orders
* Conditional view of View All Orders with validation/authorization and permissions.
* Full CRUD of the database entries.
* Pages fully link to each other.
* Create Order- Form for user to input their name, email, and phone number with email validator, and an optional portion for an extension on the phone number.
* Edit button -user can edit their entries.
* Delete button - user can delete their entries
* Drop down options from the model to choose quantities and types of muffins.
* Date picker for the calendar with a minimum date so that users cannot pick a backdate. 
* When submitting an order, the default option is "Scheduled"
* The order number displayed pulls the order number from the database. 
* Admin has ability to update order status from Scheduled to In Progress, Ready for Pickup, and Picked Up, and it will show up on the user's order. 
* When deleting an order, or a box, there is an alert, asking viewer to confirm they want deletion. 
* Shop page redirects to Create Order page when buttons are clicked. 
* Order detail card on Order Detail page can be edited, or deleted. User can also create a new order directly from that card. 
* About page has working Google Map API
* Deployment to Heroku App

## Usage
Once the customer logs in and creates their order, they are redirected to an order details page, in which they may choose their desired flavor, package size (4-pack, 6-pack, 12-pack), and date requested. Clicking on the calendar generates a date picker in which the default date is always today's date, to prevent users from accidentally back-dating their order.
![Order_Details_Page](https://user-images.githubusercontent.com/85468988/125088470-48ff6700-e082-11eb-841c-41518f3c325b.png)

## Admin Status Change Functionality
The admin has the ability to update the order status from the default "Scheduled," to "In Progress," "Ready for Pickup," and "Picked Up."

![Order_Status](https://user-images.githubusercontent.com/85468988/125088633-79470580-e082-11eb-8ddc-1f98bdc11919.png)

It will then reflect on the user's side with that new status:
![customer_order_status](https://user-images.githubusercontent.com/85468988/125089157-fb372e80-e082-11eb-97a1-65c1d9ed3275.png)


## Road Map

Planned Features: 
* Category page so that user can shop various types of pastries, then redirect to pastry details prior to creating their order.
* Add Variety Box option with option to choose quantity and type of items in each box.
* Ability to filter through orders using database categories. 
* Media query edits for better screen adaptation of body and footer.
* Integrated payment system (Stripe)
* Phone number validator
* Mission statement added to About Me page
* Order update email auto-generated when status is updated. 

## Contact
Amanda Lowry -email: amanda.lowry329@gmail.com
Project Link: https://honeybeebakery.herokuapp.com/

## Acknowledgements:
* Front Page Imagery: [Neighbor Bakehouse SF](https://neighborsf.com/)
* Shop Page Imagery: [Unsplash](https://unsplash.com)
* Google Maps API: [Google Maps API](https://developers.google.com/maps/gmp-get-started?authuser=1#enable-api-sdk)
* Materialize CSS: [Materialize CSS](https://https://materializecss.com/)
* Heroku App Deployment: [Heroku Cloud Application Platform](https://www.heroku.com)
* Google Fonts: [Google Fonts](https://fonts.google.com)
