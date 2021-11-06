from django.urls import path
from . import views
app_name = 'test1'
urlpatterns = [
    
    path('',views.home,name="test1_view_home"),
    path('v2',views.second,name="test1_view2")
]