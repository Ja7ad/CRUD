from django.urls import path
from core import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.Root.as_view(), name='root'),
    path('accounts/signup', views.Signup.as_view(), name='signup'),
    path('accounts/signin', obtain_auth_token, name='signin'),

    path('ads', views.AdList.as_view(), name='ad_list'),
    path('ad/<int:pk>', views.AdDetail.as_view(), name='ad_detail'),

    path('categories', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/ads', views.AdsByCategory.as_view(), name='ads_by_category'),

    path('users/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/ads', views.AdsByUser.as_view(), name='ads_by_user'),
]