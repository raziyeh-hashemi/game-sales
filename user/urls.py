from django.urls import path
from user.views.create_user import CreateUserView

urlpatterns = [
    path('sign_in/', CreateUserView.as_view(), name='sign in')
]

