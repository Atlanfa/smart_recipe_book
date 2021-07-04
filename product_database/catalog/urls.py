from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('addtofavorite/<int:product_id>', views.add_to_favorite, name='add_to_favorite'),
    path('deletefromfavorite/<int:product_id>', views.delete_from_favorite, name='delete_from_favorite'),
    url(r'^products/$', views.ProductListView.as_view(), name='products'),
    url(r'^prices/$', views.PriceListView.as_view(), name='prices'),
    url(r'^dishes$', views.DishListView.as_view(), name='dishes'),
    url(r'^dish/(?P<pk>\d+)$', views.DishDetailView.as_view(), name='dish-detail'),
    url(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^stores/$', views.StoreListView.as_view(), name='stores'),
    url(r'^store/(?P<pk>\d+)$', views.StoreDetailView.as_view(), name='store-detail'),
    url(r'^myproducts/$', views.UsersProductsListView.as_view(), name='my-products'),
    url(r'^mystores/$', views.UsersStoresListView.as_view(), name='my-stores'),
    url(r'^myprices/$', views.UsersPricesListView.as_view(), name='my-prices'),
    url(r'^myfavorite/$', views.UsersFavoriteProductsListView.as_view(), name='my-favorite'),
    url(r'^product/(?P<pk>[-\w]+)/renew-product/$', views.renew_product, name='renew-product'),
    url(r'^store/(?P<pk>[-\w]+)/renew-store/$', views.renew_store, name='renew-satore'),
    url(r'^price/(?P<pk>[-\w]+)/renew-price/$', views.renew_price, name='renew-price'),
    url(r'^product/create/$', views.ProductCreate.as_view(), name='product_create'),
    url(r'^product/(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='product_delete'),
    url(r'^store/create/$', views.StoreCreate.as_view(), name='store_create'),
    url(r'^store/(?P<pk>\d+)/delete/$', views.StoreDelete.as_view(), name='store_delete'),
    url(r'^price/create/$', views.PriceCreate.as_view(), name='price_create'),
    url(r'^dish/create/$', views.create_dish, name='dish_create'),
    url(r'^price/(?P<pk>\d+)/delete/$', views.PriceDelete.as_view(), name='price_delete'),
]
