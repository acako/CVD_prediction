# CVD_prediction
This project focuses on building a machine learning model to predict the risk of developing cardiovascular disease (CVD)
The original dataset can be accessed from: https://www.kaggle.com/sulianova/cardiovascular-disease-dataset
In this project we deployed and tested 7 different models.

In the 'Data Exploration, Training, Evaluation' directory can be found the code used to condition the data, feature
select, as well as code to allow for a better understanding of the data. These are for your reference.

The 'app' directory holds the final model, as well as the deployed application. 
To deploy the app, please RUN the app.py code, and click the link displayed in the terminal. This will open up a 
browser window with the application running. 
Please keep the app.py code running while the application is in use.
The app is very self explanatory, but for use:
Please input all the patient's data, including Gender, Age, Height, Weight, Systolic BP, Cholesterol and Glucose
ranking, and if the individual is active. After all the forms are correctly inputted (within the specified ranges),
press 'Submit' and the probability will be displayed, and the form will be reset for another entry.
For ease in readability, recognize the following colour coding for the probability:
Green indicates a risk factor of below 50%
Yellow indicates a risk factor between 50% and 75%
Red indicates a risk factor above 75%
Disclaimer: The application was made for the purpose of the CP8318 Final Project. The application is 72 % accurate and has a 66% recall. The application does not replace medical advice. 
