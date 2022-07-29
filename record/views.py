from django.shortcuts import render
from django.http import JsonResponse
from .models import Details

# Create your views here.
def home(request):
   return render(request, "record/index.html")