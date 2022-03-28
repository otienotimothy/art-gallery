from django.urls import path

from .views import index, signupUser, loginUser, upload

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupUser, name= 'signup' ),
    path('login/', loginUser, name='login'),
    path('profile/', upload, name='upload' )
]