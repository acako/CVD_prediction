CVD Prediction
--------------------------------------------------- Intro --------------------------------------------------------------

This project focuses on building a machine learning model to predict the risk of developing cardiovascular disease (CVD) for CP8318 (Machine Learning Course at Ryerson University for graduate students). The original dataset can be accessed from: https://www.kaggle.com/sulianova/cardiovascular-disease-dataset. In this project we trained and tested 7 different machine learning models.

------------------------------------------------- Extra Code -----------------------------------------------------------

In the 'Data Exploration, Training, Evaluation' directory the code used to do data exploration, feature selection and engineering, modelling and model tuning can be found. All the data files are included for your reference. Python 3.7 was used for the project.

---------------------------------------------------- APP ---------------------------------------------------------------

The 'app' directory holds the final model, as well as the deployed application. To deploy the app, please RUN the app.py code, and click the link displayed in the terminal. This will open up a browser window with the application running. Please keep the app.py code running while the application is in use.

The app is very self explanatory, but for use:

Please input all the patient's data, including Gender, Age, Height, Weight, Systolic BP, Cholesterol and Glucose ranking, and if the individual is active. After all the forms are correctly inputted (within the specified ranges), press 'Submit' and the probability will be displayed, and the form will be reset for another entry. If a value inputted into the numeric field (ie Age, height, etc) is erroneous, like a string input, the app inputs a value of 0 instead and outputs a 0.00% probability. If a value is inputted outside the necessary range, a 'red indicator' shows on screen, signifying the error. It will still output a probability, due to the physician possibly needing inputs outside the range for a certain patient. This red border signifies that the probability will be less accurate, but risk can still be provided.

For ease in readability, recognize the following colour coding for the probability: Green indicates a risk factor of below 50%. Yellow indicates a risk factor between 50% and 75%. Red indicates a risk factor above 75%.

The application uses a logistic regression model with a 72% accuracy and 66 % recall score. It is important to note that this application was build for the purpose of CP8318 final course project. It is not to be used to give or replace medical advice.

---------------------------------------------------- Presentation --------------------------------------------------------

A 5 minute pitch of the project is found at the file: CP8318 Final Project Presentation Recoding - Albina Cako and Jeffrey Rezazada.mp4. The presentation describes a quick overview of the project. The end of the presentation provides a guide on how to use the run and use the application.

---------------------------------------------------- Final Report -------------------------------------------------------- The final project report can be found under the filename: CP8318_Final_Report_CVD_Predicition_Albina_Cako_Jeffrey_Rezazada.pdf
