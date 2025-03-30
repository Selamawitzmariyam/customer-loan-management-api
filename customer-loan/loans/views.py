from django.shortcuts import render
from django import forms

from django.shortcuts import get_object_or_404
from django.views.generic import ListView,FormView
from django.urls import reverse_lazy
from .models import Customer,Loan,Payment
class CustomerListView(ListView):
    model=Customer
    template_name= 'customers.html'
    context_object_name= 'customers'

# Payment Form
class PaymentForm(forms.Form):
    amount_paid = forms.DecimalField(max_digits=10, decimal_places=2)

class MakePaymentView(FormView):
    template_name = 'payment.html'
    form_class = PaymentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loan = get_object_or_404(Loan, id=self.kwargs['loan_id'])
        context['loan'] = loan 
        return context

    def form_valid(self, form):
        loan = get_object_or_404(Loan, id=self.kwargs['loan_id'])
        amount_paid = form.cleaned_data['amount_paid']
        
        if amount_paid > 0:
            Payment.objects.create(loan=loan, amount_paid=amount_paid)
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('customer-list') 


