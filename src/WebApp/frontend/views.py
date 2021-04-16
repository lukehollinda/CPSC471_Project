from django.shortcuts import render

import os
#from WebApp.frontend import
# Create your views here.

def index(request):
    #print(os.listdir("frontend/src/templates/index.html"))
    return render(request, 'index.html')

