from django.urls import path

from rest_framework.routers import DefaultRouter

from api import views

router=DefaultRouter()

urlpatterns=[
    path('register/',views.SignUpView.as_view()),
]+router.urls