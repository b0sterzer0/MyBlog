from django.urls import path
from .views import user_registration_view, profile_view, login_view, MyLogoutView
from .api import APIGetProfileData


urlpatterns = [
    path('registration/', user_registration_view, name='registration'),
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('api/profiles/', APIGetProfileData.as_view(), name='api profile data'),
]
