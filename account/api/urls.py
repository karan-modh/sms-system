from django.urls import path
from account.api.views import (
    registration_view,
    ObtainAuthTokenView,
    account_details_view,
    update_account_view,
    does_account_exist_view,
    ChangePasswordView,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
    path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    path('user-data', account_details_view, name="properties"),
    path('user-data/update', update_account_view, name="update"),
    path('login', ObtainAuthTokenView.as_view(), name="login"),
    path('register', registration_view, name="register"),

]
