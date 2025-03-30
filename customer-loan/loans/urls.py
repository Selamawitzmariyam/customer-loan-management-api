from django.urls import path
from .views import CustomerListView, MakePaymentView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('make-payment/<int:loan_id>/', MakePaymentView.as_view(), name='make-payment'),
]