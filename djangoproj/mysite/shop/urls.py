from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^cart/$', views.bought, name='bought'),
               url(r'^add_to_cart/$', views.add_to_cart, name= 'add_to_cart'),]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
