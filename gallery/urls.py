from django.urls import path

from .views import index, signup_page, login_page

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup_page, name= 'signup' ),
    path('login/', login_page, name='login')
]