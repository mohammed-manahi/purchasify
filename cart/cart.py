from django.conf import settings
from decimal import Decimal
from shop.models import Product
from coupon.models import Coupon


class Cart():
    """
    Create cart functionalities with the help of django sessions
    """

    def __init__(self, request):
        """
        Initialize the cart using django session
        :param request:
        :return cart:
        """
        self.session = request.session
        # Get the cart from the session if it exists
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Create new empty cart id if it does not exist
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # Get the coupon id from session
        self.coupon_id = self.session.get('coupon_id')

    def add(self, product, quantity=1, override_quantity=False):
        """
        Create cart addition functionality
        :param product:
        :param quantity:
        :param override_quantity:
        :return cart:
        """
        # Convert to string because django serialize session to json data
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Mark session as modified to make sure to save the changes
        :return modified cart session:
        """
        self.session.modified = True

    def remove(self, product):
        """
        Remove product from the cart in the session
        :param product:
        :return :
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        :return cart item:
        """
        product_ids = self.cart.keys()
        # Get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count the items in the cart
        :return total items in the cart:
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculate the total price of items in the cart
        :return total price:
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Delete the cart session
        :return:
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    @property
    def coupon(self):
        """
        Define coupon property
        :return coupon id:
        """
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None

    def get_discount(self):
        """
        Apply coupon discount
        :return discount value:
        """
        if self.coupon:
            return (self.coupon.discount / Decimal(100)) * self.get_total_price()
        return Decimal(0)

    def get_total_price_after_discount(self):
        """
        Calculate the price after the discount
        :return total price after discount:
        """
        return self.get_total_price() - self.get_discount()
