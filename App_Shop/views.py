from django.shortcuts import render

#importing a list
from django.views.generic import ListView,DetailView

#models
from App_Shop.models import Product

#mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#will create a classbased view
class Home(ListView):
    model = Product
    template_name='App_Shop/home.html'

#this also be a classbased view
class ProductDetail(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'
