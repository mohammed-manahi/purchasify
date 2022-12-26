from cart.cart import Cart


def cart(request):
    """
    Create a context processor for the cart to make it available for the templates as a variable named cart.
    :param request:
    :return cart:
    """
    return {'cart': Cart(request)}
