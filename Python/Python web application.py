import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

def main():
    st.title("Binary Classification Web Application")
    st.sidebar.title("Binary Classification Web Application")
    st.markdown("Are your mushrooms edible or poisonous 🤔")
    st.sidebar.markdown("Are your mushrooms edible or poisonous 🤔")

    @st.cache(persist=True)
    def load_data():
        data = pd.read_csv('/home/rhyme/Desktop/Project/mushrooms.csv')
        label = LabelEncoder()
        for col in data.columns:
            data[col] = label.fit_transform(data[col])
        return data

    @st.cache(persist=True)
    def split(df):
        y = df.type
        x = df.drop(columns = ['type'])

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state=0)
        return x_train, x_test, y_train, y_test

    def plot_metrics(metrics_list):
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(model, x_test, y_test, display_labels=class_names)
            st.pyplot()

        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            plot_roc_curve(model, x_test, y_test)
            st.pyplot()

        if 'Precision - Recall Curve' in metrics_list:
            st.subheader("Precision - Recall Curve")
            plot_precision_recall_curve(model, x_test, y_test)
            st.pyplot()
        
        
          
    df = load_data()
    x_train, x_test, y_train, y_test = split(df)

    class_names = ['edible', 'poisonous']

    st.sidebar.subheader("Choose Classfier")
    classifier = st.sidebar.selectbox("Choose Classifier", ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest Classification"))
    
    if classifier == 'Support Vector Machine (SVM)':
        st.sidebar.subheader("Choose Model Hyperparameters:")

        C = st.sidebar.number_input("C (Strength of Regularization)", 0.01, 100.0, step  = 0.01, key ="C")
        kernel = st.sidebar.radio("Kernel for SVM Classification", ("rbf", "linear"), key = "kernel")
        gamma = st.sidebar.radio("Kernel Coefficient (Gamma)", ("scale", "auto"), key = 'gamma')
       
        metrics = st.sidebar.multiselect("Choose the Metrics to be plotted", ("Precision - Recall Curve", "ROC Curve", "Confusion Matrix"))
    
        if st.sidebar.button("Classify, Get Results!"):
            st.subheader("Support Vector Machine (SVM) Classifier Results: ")

            model = SVC(C=C, kernel=kernel, gamma=gamma)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_predicted = model.predict(x_test)
            st.write("Accuracy", accuracy.round(2))
            st.write("Precision: ", precision_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("Recall: ", recall_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("f1 score: ", f1_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("ROC: Area Under the Curve: ", roc_auc_score(y_test, y_predicted, labels = class_names).round(2))


            plot_metrics(metrics)


    if classifier == 'Logistic Regression':

        st.sidebar.subheader("Choose Model Hyperparameters:")

        C = st.sidebar.number_input("C (Strength of Regularization)", 0.01, 100.0, step  = 0.01, key ="C_log")
        max_iter = st.sidebar.slider("Maximum Number of Iterations: ", 100, 500, key = 'max_iter')
            
        metrics = st.sidebar.multiselect("Choose the Metrics to be plotted", ("Precision - Recall Curve", "ROC Curve", "Confusion Matrix"))
    
        if st.sidebar.button("Classify, Get Results!"):            
            st.subheader("Logistic Regression Classifier Results: ")

            model = LogisticRegression(C=C, max_iter=max_iter)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_predicted = model.predict(x_test)
            st.write("Accuracy", accuracy.round(2))
            st.write("Precision: ", precision_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("Recall: ", recall_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("f1 score: ", f1_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("ROC: Area Under the Curve: ", roc_auc_score(y_test, y_predicted, labels = class_names).round(2))


            plot_metrics(metrics)

    if classifier == 'Random Forest Classification':

        st.sidebar.subheader("Choose Model Hyperparameters:")

        n_estimators = st.sidebar.number_input("The number of trees in the forest:", 1, 20,  step =1, key = 'n_estimators')
        max_depth = st.sidebar.number_input("The maximum Depth of Each Tree: ", 1, 20, step = 1, key = 'max_depth')     
        bootstrap = st.sidebar.radio("Bootstrap Samples when building Trees", ('True', 'False'), key = 'bootstrap')
        
        metrics = st.sidebar.multiselect("Choose the Metrics to be plotted", ("Precision - Recall Curve", "ROC Curve", "Confusion Matrix"))
    
        if st.sidebar.button("Classify, Get Results!"):            
            st.subheader("Random Forest Classifier Results: ")

            model = RandomForestClassifier(n_estimators = n_estimators, max_depth=max_depth, bootstrap = bootstrap, n_jobs=-1)
            model.fit(x_train, y_train)
            accuracy = model.score(x_test, y_test)
            y_predicted = model.predict(x_test)
            st.write("Accuracy", accuracy.round(2))
            st.write("Precision: ", precision_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("Recall: ", recall_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("f1 score: ", f1_score(y_test, y_predicted, labels = class_names).round(2))
            st.write("ROC: Area Under the Curve: ", roc_auc_score(y_test, y_predicted, labels = class_names).round(2))


            plot_metrics(metrics)



    if st.sidebar.checkbox("Display raw data", False):
        st.subheader("Dataset used for Classification:")
        st.markdown("Transformed dataset (Label Encoded)")

        st.write(df)

    

if __name__ == '__main__':
    main()


