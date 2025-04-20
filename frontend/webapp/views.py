from django.shortcuts import render

from .models import predict
from django.shortcuts import render
import requests
import numpy as np
import pandas as pd



# Create your views here.
def home(request):
	return render(request,'index.html')

def input(request):
	return render(request,'input.html')

def output(request):
	algo=request.POST.get('algo')
	row=int(request.POST.get('row'))
	out=predict(algo,row)
	#classes = class_names[int(out)]
	print(out)
	if out == 0:
		class_name = 'not affected'
	else:
		class_name = 'affected'

	print(class_name)
	return render(request,'output.html',{'out':class_name})
