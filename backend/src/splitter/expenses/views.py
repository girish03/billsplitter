from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_expense(request):
    try:
        return HttpResponse(content="Expense added successfully")
    except Exception as e:
        print(str(e))

def delete_expense(request):
    try:
        return HttpResponse(content="Expense deleted successfully")
    except Exception as e:
        print(str(e))

def divide_expense(request):
    try:
        return HttpResponse(content="Expense divided successfully")
    except Exception as e:
        print(str(e))