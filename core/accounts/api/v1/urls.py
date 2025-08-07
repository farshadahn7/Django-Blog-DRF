from django.urls import path


from . import views

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('token/', views.TokenJwtView.as_view(), name='login'),
    path('refresh-token/', views.TokenRefreshJwtView.as_view(), name='refresh-token'),
    path('user-verification/<str:token>/', views.VerifyAccountView.as_view(), name='verify-user'),
    path('change-password/', views.ChangePasswordView.as_view(), name="change-password"),
    path('reset-password/<str:token>/', views.ForgetPasswordView.as_view(), name="reset-password"),
    path("forget-password/", views.ResetPasswordView.as_view(), name="reset-password-email")
]