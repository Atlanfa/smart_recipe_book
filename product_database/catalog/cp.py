from .models import Store, Price


def calculate_price(dish, user_data):
    price = 0
    stores = Store.objects.all().filter(city=user_data.city)
    for product_amount in dish.products:
        product_lowest_price = Price.objects.all().filter(product=product_amount.product, store=stores[0])[0]
        for store in stores:
            if Price.objects.all().filter(product=product_amount.product, store=store)[0] < product_lowest_price:
                product_lowest_price = Price.objects.all().filter(product=product_amount.product, store=store)[0]
        if product_amount.product.product_by_weight_in_packaging == 'Yes':
            price += product_lowest_price.price
        else:
            price += ((product_amount.amount * 1000 if product_amount.unit == 'kg' or 'l' else product_amount.amount)/(product_amount.product.weight * 1000 if product_amount.product.unit == 'kg' or 'l' else product_amount.product.weight)) * product_lowest_price.price
    return price
