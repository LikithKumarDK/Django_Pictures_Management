# frontend/views.py
from django.shortcuts import render

# View to render index page
def index(request):
    return render(request, 'base.html')
