
# Honeybee Bakery

Honeybee Bakery is small bakery that sells three muffins. Customers shop from the bakery. They can create, edit, and delete their orders once logged in. This also can work as an order management system for the bakery to update order status of each customer.

## Technologies Used


* Python
* Django
* PostgreSQL
* Google Map API
* JavaScript
* HTML
* CSS
* Materialize CSS Framework


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
* About page has working Google Map
* Deployment to Heroku App

## Planned Features

* Category page so that user can shop various types of pastries, then redirect to pastry details prior to creating their order.
* Add Variety Box option with option to choose quantity and type of items in each box.
* Ability to filter through orders using database categories. 
* Media query edits for better screen adaptation of body and footer.
* Integrated payment system (Stripe)
* Phone number validator
* Mission statement added to About Me page
* Order update email auto-generated when status is updated. 

