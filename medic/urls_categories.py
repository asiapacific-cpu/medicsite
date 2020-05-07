from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from .views import *
from . import views




urlpatterns = [

    path('', CategoryListView.as_view(), name='products'),
    # path('<slug:slug>/', ProductCategoryListView.as_view(), name='items'),
    # path('<slug:slug>/', ProductCategoryDetailView.as_view(), name='item_detail'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='products_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
