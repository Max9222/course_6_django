from django.urls import path
from main.apps import MainConfig
from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, gen_password, verify, ProfileDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/gen_password/', gen_password, name='gen_password'),
    path('verify/<code>/', verify, name='verify_email'),
    path('profile/delete/<int:pk>', ProfileDeleteView.as_view(), name='profile_delete'),
]
