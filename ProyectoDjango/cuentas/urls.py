from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'), name='Logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile', ShowProfileView.as_view(), name='show_profile_page'),
    path('<int:pk>/', ShowProfileView.as_view(), name='show_profile_page'),
    

]