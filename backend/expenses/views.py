from django.shortcuts import render
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer
from rest_framework import generics

# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ExpenseCreateView(
    generics.CreateAPIView
):

    queryset = Expense.objects.all()

    serializer_class = ExpenseSerializer