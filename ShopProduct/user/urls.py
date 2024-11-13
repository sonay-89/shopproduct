from django.urls import path

from shopproduct.user.views import UserInfoView

urlpatterns = [
    path("", UserInfoView.as_view(), name="user_register"),
]
