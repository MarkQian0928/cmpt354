from django.shortcuts import render
from shoes.models import Shoes
from . models import Cart, CartItems

def _cart_id(request):
	cart = request.seesion.session_key
	if not cart:
		cart = request.session.create()
	return cart

def add_cart(request,shoe_id):
	shoe = Shoes.objects.get(id = shoe_id)
	try:
		cart = Cart.objects.get(CartID = _cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
				CartID = _cart_id(request)
			)
		cart.save()

	try:
		cart_item = CartItem.objects.get(shoe = shoe, cart = cart)
		cart_item.quanity += 1
		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(
					shoe  = shoe,
					quanity = 1,
					cart = cart
			)
		cart_item.save()
	return redirect('cart:cart_detail')

def cart_detail(request,total = 0,counter = 0,cart_items = None):
	try:
		cart = Cart.objects.get(CartID = _cart_id(request))
		cart_items = CartItem.objects.filter(cart = cart,active = True)
		for cart_item in cart_items:
			total += (cart_item.shoe.price * cart_item.quanity)
			counter += cart_item.quanity
	except ObjectDoesNotExist:
		pass

	return render(request,'cart.html',dict(cart_items = cart_items, total = total, counter = counter ))
















