from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet ,LoanViewSet,PaymentViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'customers', CustomerViewSet )
router.register(r'payments',PaymentViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/',obtain_auth_token, name='api_token_auth'),
    

]
