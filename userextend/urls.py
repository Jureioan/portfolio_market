from django.urls import path

from userextend import views

urlpatterns = [
    path('create_user/', views.UserExtentCreateView.as_view(), name="create-user"),
]