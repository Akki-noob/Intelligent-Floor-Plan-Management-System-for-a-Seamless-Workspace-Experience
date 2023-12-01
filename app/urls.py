from  django.urls  import  path
from . import views 

urlpatterns = [
path('', views.home, name='home'),
path('floor', views.floor, name='floor'),
path('addPlan', views.addPlan, name='addPlan'),
path('change', views.change, name='change'),
]