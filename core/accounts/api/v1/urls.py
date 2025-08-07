from django.urls import path


from . import views

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('token/', views.TokenJwtView.as_view(), name='login'),
    path('refresh-token/', views.TokenRefreshJwtView.as_view(), name='refresh-token'),
]