from django.urls import path
from .views import CategoryListView
from .views import ExpenseCreateView

urlpatterns = [
    path(
        'categories/',
        CategoryListView.as_view(),
        name='category-list'
    ),

    path(
        'expenses/create/',
        ExpenseCreateView.as_view(),
        name='expense-create'
    ),
]