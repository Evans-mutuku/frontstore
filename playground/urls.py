from django.urls import path
from . import views

# Url Config
urlpatterns = [
    # path('playground/hello', views.say_hello),
    #  Change the above to =>
    path('hello/', views.say_hello) 
    
]
