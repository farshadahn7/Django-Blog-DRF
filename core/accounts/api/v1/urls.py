from django.urls import path


from . import views

urlpatterns = [
    path('test/', views.RegistrationView.as_view(), name='test'),
]