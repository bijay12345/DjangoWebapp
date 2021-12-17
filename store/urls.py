from django.urls import path,include
from .views import StoreListView,ItemDetailView,add_to_cart



urlpatterns = [
    path('', StoreListView.as_view(), name='store-home'),
    path('<slug>/', ItemDetailView.as_view(), name='item-detail'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),

]
