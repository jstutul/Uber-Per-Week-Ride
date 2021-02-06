from django.shortcuts import render
import numpy as np
import pickle
import math

from MLR import model


def Home(request):
    if request.method=="POST":
        Priceperweek =int(request.POST['Priceperweek'])
        Population   =int(request.POST['Population'])
        Monthlyincome =int(request.POST['Monthlyincome'])
        Averageparkingpermonth =int(request.POST['Averageparkingpermonth'])
        model = pickle.load(open('taxi.pkl', 'rb'))
        output= model.predict([[Priceperweek, Population, Monthlyincome, Averageparkingpermonth]])
        result =int(output)

        return render(request, 'index.html',{'result':result})
    else:
        return render(request,'index.html')


