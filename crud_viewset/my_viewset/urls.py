from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewset

router = DefaultRouter()




router.register(r'product',ProductViewset,basename='product')
urlpatterns = [
    path('',include(router.urls))

]
