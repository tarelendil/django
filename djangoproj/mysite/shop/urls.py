from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static
# urlpatterns = [
#     # ex: /shop/
#     url(r'^$', views.index, name='index'),
#     # ex: /shop/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /shop/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /shop/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),]

app_name = 'shop'
urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^cart/$', views.bought, name='bought'),
               url(r'^add_to_cart/$', views.add_to_cart, name= 'add_to_cart'),]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]