from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        # Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if both fields are filled
        if username and password:

            request.session['username'] = username
            return redirect('index')
        else:
            # Show an error if either username or password is missing
            messages.error(request, 'Both username and password are required')

    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')

def credit_card(request):
    return render(request, 'credit_card.html',{'range': range(1, 29)})

import numpy as np
import joblib  # For loading the trained model

# Load your trained XGBoos
loaded_model = joblib.load("C:/Users/nigad/Downloads/creditcardproject/credit/static/assets/xgboost_model.pkl")

def predict_fraud(request):
    if request.method == 'POST':
        try:
            # Extract all required inputs from the form
            time = float(request.POST['time'])
            v1 = float(request.POST['v1'])
            v2 = float(request.POST['v2'])
            v3 = float(request.POST['v3'])
            v4 = float(request.POST['v4'])
            v5 = float(request.POST['v5'])
            v6 = float(request.POST['v6'])
            v7 = float(request.POST['v7'])
            v8 = float(request.POST['v8'])
            v9 = float(request.POST['v9'])
            v10 = float(request.POST['v10'])
            v11 = float(request.POST['v11'])
            v12 = float(request.POST['v12'])
            v13 = float(request.POST['v13'])
            v14 = float(request.POST['v14'])
            v15 = float(request.POST['v15'])
            v16 = float(request.POST['v16'])
            v17 = float(request.POST['v17'])
            v18 = float(request.POST['v18'])
            v19 = float(request.POST['v19'])
            v20 = float(request.POST['v20'])
            v21 = float(request.POST['v21'])
            v22 = float(request.POST['v22'])
            v23 = float(request.POST['v23'])
            v24 = float(request.POST['v24'])
            v25 = float(request.POST['v25'])
            v26 = float(request.POST['v26'])
            v27 = float(request.POST['v27'])
            v28 = float(request.POST['v28'])
            amount = float(request.POST['amount'])

            # Create a feature array for prediction
            your_new_data = np.array([
                time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15,
                v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount
            ]).reshape(1, -1)

            # Call the XGBoost model to predict
            prediction = loaded_model.predict(your_new_data)

            # Map prediction to a meaningful output (e.g., fraud or not fraud)
            prediction_label = "Fraudulent" if prediction == 1 else "Legitimate"

            # Render the result in the 'result.html' template
            return render(request, 'result.html', {'prediction': prediction_label})

        except Exception as e:
            # Handle errors (e.g., invalid inputs)
            error_message = f"An error occurred: {e}"
            return render(request, 'result.html', {'prediction': error_message})

    return render(request, 'credit_card.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('index')
