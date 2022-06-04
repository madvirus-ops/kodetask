from multiprocessing import context
from .models import Product

new = Product(name='beans', price=100)
new.save()
# return all products
Product.objects.all()
#filter by name
Product.objects.filter(name='beans')
#get a single product
Product.objects.get(name='beans')
#update a product
Product.objects.filter(name='beans').update(price=200)