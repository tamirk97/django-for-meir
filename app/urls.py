###app###
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router=DefaultRouter()

router.register(r'students',views.StudentViewSet)
router.register(r'cars',views.CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]



