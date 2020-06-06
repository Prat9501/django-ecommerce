![](Ecommerce.gif)

# Ecommerce Website

Ecommerce website built in Django using:
- django crispy forms
- django debug toolbar
- drf
- django allauth

Ecommerce website with simple UI interface where a user can view products on home page. Once a user is logged in, product can be added to the cart.
Product quantity can be updated in the cart and proceed to checkout. One can return to continue shopping from cart page.
A user can use a new billing address, or the default previously saved address for shipping. Similarly for billing purpose.
Has a feature to redeem coupons. Once coupon is applied desired amount will be deducted from the checkout price.

Provides a django admin panel where items, orders, order_items, refunds can be managed.


To run the project:
- Download or fork the project
- Create a virtual environment: `mkvirtualenv ecommerce`
- Go to project directory install the requirements: `pip -r install requirements.txt`
- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Finally run `python manage.py runserver`
- Go to localhost in browser and good to go.
- To access the django admin panel create a superuser first.
