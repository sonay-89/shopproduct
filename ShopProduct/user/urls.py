from django.urls import path

from ShopProduct.user.views import UserInfoView

urlpatterns = [
    path('', UserInfoView.as_view(), name='user_register'),
]
