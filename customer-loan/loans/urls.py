from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet ,LoanViewSet,PaymentViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet )
router.register(r'payments',PaymentViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
]
