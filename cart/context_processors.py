



# context_processors.py
from .models import CartItem
from django.db.models import Sum

def cart_quantity(request):
    if request.user.is_authenticated:
        total_quantity = CartItem.objects.filter(cart__user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    else:
        total_quantity = 0  # Default for anonymous users
    return {'cart_quantity': total_quantity}
