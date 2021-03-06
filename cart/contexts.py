from django.shortcuts import get_object_or_404
from websites.models import Website


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    website_count = 0

    for id, quantity in cart.items():
        website = get_object_or_404(Website, pk=id)
        total += quantity * website.price
        website_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'website': website})

    return {
        'cart_items': cart_items,
        'total': total, 'website_count': website_count
        }
