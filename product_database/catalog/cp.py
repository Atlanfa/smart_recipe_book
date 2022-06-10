import decimal

from .models import Store, Price


def calculate_price(dish, user_data):
    price = 0
    stores = Store.objects.all().filter(city=user_data.city)
    for product_amount in dish.products.all():
        product_lowest_price = Price.objects.all().filter(product=product_amount.product, store__in=stores)
        for store in stores:
            sujested_price = Price.objects.all().filter(product=product_amount.product, store=store)
            if sujested_price.count() == 0:
                pass
            else:
                if sujested_price[0].price < product_lowest_price[0].price:
                    product_lowest_price = Price.objects.all().filter(product=product_amount.product, store=store)
        if product_amount.product.product_by_weight_in_packaging == 'Yes':
            price += product_lowest_price[0].price
        else:
            price += decimal.Decimal(((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount))/decimal.Decimal((product_amount.product.weight * 1000 if product_amount.product.unit == 'kg' or 'l' else product_amount.product.weight))) * decimal.Decimal(product_lowest_price[0].price)
    return price
