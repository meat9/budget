from rest_framework import serializers
from .models import BudgetType, Budget, GlavBudgetClass
  

class BudgetTypeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = BudgetType 
        fields = ['id', 'author', 'pub_date', 'score', 'text'] 
     

class BudgetSerializer(serializers.ModelSerializer): 
    class Meta:         
        model = Budget 
        fields = ['code','name','parentcode', 'startdate','enddate','status','budgettype']


class GlavBudgetSerializer(serializers.ModelSerializer): 
    class Meta:         
        model = GlavBudgetClass 
        fields = ['code' , 'name' , 'startdate' ,'enddate' ,'budget']

            