from django.contrib import admin
from django.urls import path, include
from user.views import UserLogarView, UserRegisterView, LogoutView

# Endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
    path('payments/', include('payments.urls')),
    path('tenants/', include('tenants.urls')),
    path('contracts/', include('contracts.urls')),
    path('login/', UserLogarView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
