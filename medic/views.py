import random
from django.contrib import messages
from django.http import Http404
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Item, Category, ProductCategory
from .forms import InquiryForm
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.

def home(request, template='index.html'):
    items = Item.objects.all().order_by('?')[:6]

    context = {'title': 'asiapacificequipments',
               'items': items,
               }
    return render(request, template, context)


def about_us(request):
    template = 'about-us.html'
    context = {
        'title': 'Asiapacificequipment - About us',
    }
    return render(request, template, context)




def contactform(request):
    template = 'contact-us.html'
    print("now posting form")
    form = InquiryForm(request.POST or None)
    print(form)
    if form.is_valid():
        name = request.POST.get("name")
        print(name)
        email = request.POST.get("email")
        print(email)
        phonenumber = request.POST.get("phonenumber")
        print(phonenumber)
        message = request.POST.get("message")
        print(message)


        subject = "A Costumer's Inquiry"
        # if request.user.is_authenticated():
        #     subject= str(request.user) + "'s Comment"
        # else:
        #     subject= "A Visitor's Comment"
        #
        #
        # comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
        newmessage = "A New Inquiry was Made by NAME : {title} , \n Email:  {email} \n PHONE NUMBER : {phonenumber} \n ".format(
            title=name,
            email= email,
            phonenumber=phonenumber)
        email_from = settings.EMAIL_HOST_USER

        reciever =  "efiong.efimbukpa@gmail.com" # "info@asiapacificequipments.com"
        print("sending mail")

        send_mail(subject, newmessage, email_from, [reciever,], fail_silently=False)
    context= {
        'form': form,
        'title' : 'Asiapacificequipment - Contact Us'
    }
    return render(request, template, context)
#
#     else:
#         context= {'form': form}
#         return render(request, 'form.html', context)



class CategoryListView(ListView):
    model = Category
    items = Category.objects.all()
    template_name = 'product.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = "ventilator.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set = obj.item_set.all()
        default_products = obj.default_category.all()
        products = (product_set | default_products).distinct()
        context["products"] = products
        return context


class ProductCategoryListView(ListView):
    model = ProductCategory
    items = ProductCategory.objects.all()
    template_name = 'product.html'


class ProductCategoryDetailView(DetailView):
    model = ProductCategory
    template_name = "ventilator.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductCategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set = obj.item_set.all()
        default_products = obj.default_productcategorye.all()
        products = (product_set | default_products).distinct()
        context["products"] = products
        return context