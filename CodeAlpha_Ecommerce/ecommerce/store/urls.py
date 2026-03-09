from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # 👈 THIS WAS MISSING
    path("signup/", views.signup, name="signup"),
    path("buy/<int:product_id>/", views.buy, name="buy"),
    path("my-orders/", views.my_orders, name="my_orders"),

]
