from rest_framework import serializers
from .models import Loan,Customer,Payment
class LoanSerializer(serializers.ModelSerializer):
     class Meta:
         model = Loan
         fields = '__all__'
     def validate_loan(self,value):
         if value < 200 :
          raise serializers.ValidationError("Loan amount must be at least $300.")
         
class CustomSerializer(serializers.ModelSerializer):
   loans = LoanSerializer(many=True, read_only=True)
   class Meta:
       model = Customer
       fields = '__all__'

   def validat_name(self,value):
        if len(value)<3:
            raise serializers.ValidationError("name must be atleast 3 character ")
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("name can't contain number")

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'