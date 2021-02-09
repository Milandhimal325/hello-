from django.shortcuts import render , redirect


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from userdetail.models import patient
def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request,'predict.html')
def login(request):
    return render(request, 'login.html')

def register(request):
    # Username  =  request.POST["Username"]
    # email  =  request.POST["email"]
    # password  =  request.POST["psw"]
    # Phone_Number  =  request.POST["Phone_Number"]
    # patient(username=Username,email=email,phone_no=Phone_Number)
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')
def password(request):
    return render(request, 'password.html')
def Result(request):
    return render(request, 'Result.html')
def result(request):
    data=pd.read_csv(r'C:\Users\User\Desktop\DiabetesPrediction\diabetes.csv')

    from sklearn.model_selection import train_test_split
    x = data.drop('Outcome',axis=1)
    y = data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 42, stratify = data['Outcome'] )
    
    from sklearn.naive_bayes import GaussianNB
    nb = GaussianNB()
    nb.fit(x_train, y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

   
    pred = nb.predict([[val1, val2,val3,val4, val5,val6, val7 ,val8]])
    pred_prob = nb.predict_log_proba([[val1, val2,val3,val4, val5,val6, val7 ,val8]])
    result1=""
    print("Prob  of diab= {}".format(pred_prob))
    if pred==[1]:
        result1= "POSITIVE"
    else:
        result1="NEGATIVE"

    return render(request,'predict.html',{"result2":result1})

