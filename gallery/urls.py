from django.urls import path

from .views import index, signupUser, loginUser, logoutUser, upload

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupUser, name= 'signup' ),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('upload/', upload, name='upload' )
]