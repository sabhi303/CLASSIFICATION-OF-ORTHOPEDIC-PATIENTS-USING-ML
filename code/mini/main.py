

import pandas as pd
import numpy as np


def data_preprocessing():
    
    from sklearn.preprocessing import LabelEncoder
    from sklearn import model_selection

    # Import csv data and split into independent (X) and dependent (y) for normal / abnormal classification
    data_2c = pd.read_csv('column_2C_weka.csv')
    X_2c = data_2c.iloc[:, 0:6].values
    y_2c = data_2c.iloc[:, -1].values
    labelencoder_2c = LabelEncoder()
    y_2c = labelencoder_2c.fit_transform(y_2c)

    # Import csv data and split into independent (X) and dependent (y) for normal / DH / Sp classification
    data_3c = pd.read_csv('column_3C_weka.csv')
    X_3c = data_3c.iloc[:, 0:6].values
    y_3c = data_3c.iloc[:, -1].values
    labelencoder_3c = LabelEncoder()
    y_3c = labelencoder_3c.fit_transform(y_3c)
    print()

    # Split data into training and testing sets
    # print(X_2c)
    X_2c_train, X_2c_test, y_2c_train, y_2c_test = model_selection.train_test_split(X_2c, y_2c, test_size=0.2,random_state=42)
    train_test_2c = [X_2c_train, X_2c_test, y_2c_train, y_2c_test]

    X_3c_train, X_3c_test, y_3c_train, y_3c_test = model_selection.train_test_split(X_3c, y_3c, test_size=0.2,random_state=42)
    train_test_3c = [X_3c_train, X_3c_test, y_3c_train, y_3c_test]

    return train_test_2c, train_test_3c


    
def knn(train_test_2c, train_test_3c,c2,c3):
    # Selects and fits the k-nearest neighbors classifier
    from sklearn.neighbors import KNeighborsClassifier
    classifer_2c = KNeighborsClassifier(n_neighbors=5)
    classifer_2c.fit(train_test_2c[0], train_test_2c[2])
    classifer_3c = KNeighborsClassifier(n_neighbors=5)
    classifer_3c.fit(train_test_3c[0], train_test_3c[2])
    # Predict test data
    y_pred_2c = classifer_2c.predict(train_test_2c[1])
    y_pred_3c = classifer_3c.predict(train_test_3c[1])
    ans2=int(classifer_2c.predict(c2))
    ans3=int(classifer_3c.predict(c3))
    # Calculate confusion matrix and normalized accuracy
    from sklearn import metrics
    acc_2c = metrics.accuracy_score(train_test_2c[3], y_pred_2c, normalize=True)

    acc_3c = metrics.accuracy_score(train_test_3c[3], y_pred_3c, normalize=True)

    # Perform k-fold cross validation for improved accuracy score
    # print(ans2,ans3)
    evaluation_results = [acc_2c, acc_3c, ans2, ans3]

    return evaluation_results
def naive_bayes(train_test_2c, train_test_3c,c2,c3):
    # Selects and fits the k-nearest neighbors classifier
    from sklearn.naive_bayes import GaussianNB
    classifer_2c = GaussianNB()
    classifer_2c.fit(train_test_2c[0], train_test_2c[2])
    classifer_3c = GaussianNB()
    classifer_3c.fit(train_test_3c[0], train_test_3c[2])
    # Predict test data
    y_pred_2c = classifer_2c.predict(train_test_2c[1])
    y_pred_3c = classifer_3c.predict(train_test_3c[1])
    ans2=int(classifer_2c.predict(c2))
    ans3=int(classifer_3c.predict(c3))
    # Calculate confusion matrix and normalized accuracy
    from sklearn import metrics
    acc_2c = metrics.accuracy_score(train_test_2c[3], y_pred_2c, normalize=True)

    acc_3c = metrics.accuracy_score(train_test_3c[3], y_pred_3c, normalize=True)

    # Perform k-fold cross validation for improved accuracy score
    # print(ans2,ans3)
    evaluation_results = [acc_2c, acc_3c, ans2, ans3]

    return evaluation_results
        # Selects and fits the naive Bayes neighbors classifier
        


def results_comparison(knn_results, nb_results):
    

    print(f'The accuracy rates for normal / abnormal are: KNN: {knn_results[0]*100:.2f}%, '
          f' Naive Bayes: {nb_results[0]*100:.2f}%')
    print('Knn Predictions:')
    if(knn_results[2]==0):
        print('Abnormal')
    elif(knn_results[2]==1):
        print('Normal')
    if(knn_results[3]==0):
        print('Hernia')
    elif(knn_results[3]==1):
        print('Normal')
    elif(knn_results[3]==2):
        print('Spon')
    print('Naive Predictions:')
    if(nb_results[2]==0):
        print('Abnormal')
    elif(nb_results[2]==1):
        print('Normal')
    if(nb_results[3]==0):
        print('Hernia')
    elif(nb_results[3]==1):
        print('Normal')
    elif(nb_results[3]==2):
        print('Spon')
    print()
    print(f'The accuracy rates for normal / disk hernia / spondylolisthesis are: KNN: {knn_results[1]*100:.2f}%, '
          f' Naive Bayes: {nb_results[1]*100:.2f}%')
    


def main():
    c2=[[67.28971201,16.7175142,50.99999999,50.5721978,137.5917777,4.960343813]]
    c3=[[81.05661087,20.80149217,91.78449512,60.2551187,125.430176,38.18178176]]
    train_test_2c, train_test_3c = data_preprocessing()
    knn_results = knn(train_test_2c, train_test_3c, c2, c3)  # k-nearest neighbors
    nb_results = naive_bayes(train_test_2c, train_test_3c,c2, c3)  # naive Bayes
    results_comparison(knn_results, nb_results)


if __name__ == '__main__':
    main()



   