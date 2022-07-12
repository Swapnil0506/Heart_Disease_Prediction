from django.http import HttpResponse
from django.shortcuts import render

import pickle
import numpy as np
import pandas as pd

def index(request):
    return render(request,'index.html')

def results(request):
    if request.method == 'POST':
        smokerBinary = 0
        genderBinary = -1
        BPMedsBinary = -1
        PreStrokeBinary = -1
        PreHyperBinary = -1
        DiabiBinary = -1

        userGender = request.POST['gender']
        userAge = int(request.POST['age'])

        checkBox = request.POST.get('Box')
        userCigrattes = 0
        if checkBox is not None:
            userCigrattes = int(request.POST.get('Cigarettes'))
            print(type(userCigrattes))
            smokerBinary = 1
        
        userBPMed = request.POST['BPMed']
        userPreStroke = request.POST['PreStroke']
        userPreHyper = request.POST['PreHyper']
        userDiabi = request.POST['Diabi']

        userTotalCho = int(request.POST['TotalCho'])
        userSysBP = int(request.POST['SysBP'])
        userDiaBP = int(request.POST['DiaBP'])
        userBMI = int(request.POST['BMI'])
        userHeartRate = int(request.POST['HeartRate'])
        userGlucose = int(request.POST['Glucose'])

        if userGender == 'Male':
            genderBinary = 1
        else:
            genderBinary = 0
        
        if userBPMed == 'Yes':
            BPMedsBinary = 1
        else:
            BPMedsBinary = 0
        
        if userPreStroke == 'Yes':
            PreStrokeBinary = 1
        else:
            PreStrokeBinary = 0
        
        if userPreHyper == 'Yes':
            PreHyperBinary = 1
        else:
            PreHyperBinary = 0
        
        if userDiabi == 'Yes':
            DiabiBinary = 1
        else:
            DiabiBinary = 0

        predictionModel = pickle.load(open('D:\Extra files\Heart_Disease_Prediction\HeartDiseasePrediction\AnotherPickleFile','rb'))
        userInputList = [[genderBinary,userAge,smokerBinary,userCigrattes,BPMedsBinary,PreStrokeBinary,PreHyperBinary,DiabiBinary,userTotalCho,userSysBP,userDiaBP,userBMI,userHeartRate,userGlucose]]
        print(userInputList)
        numpyAray = np.array(userInputList)
        df = pd.DataFrame(numpyAray, columns = ['Sex_male','age','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])
        predictionValue = predictionModel.predict(df)
        print(predictionValue)
        return render(request, 'result.html',{'value':predictionValue[0]})
    else:
        return render(request,'index.html')