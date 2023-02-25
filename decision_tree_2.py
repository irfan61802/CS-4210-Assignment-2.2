#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here

    for row in dbTraining:
        xRow=[]
        for i,x in enumerate(row):
            if i==4: continue
            if x=="Young" or x=="Myope" or x=="Yes" or x=="Normal":
                xRow.append(1)
            elif x=="Prepresbyopic":
                xRow.append(3)
            else:
                xRow.append(2)
        X.append(xRow)
    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    for row in dbTraining:
        if row[-1]=="Yes":
            Y.append(1)
        else:
            Y.append(2)

    accuracy = []
    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest=[]
       with open('contact_lens_test.csv', 'r') as testfile:
           reader = csv.reader(testfile)
           for i, row in enumerate(reader):
               if i > 0:  # skipping the header
                   dbTest.append(row)


       numTrue=0
       X_test=[]
       Y_test=0
       for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here

           xRow = []
           for i, x in enumerate(data):
               if i == 4: continue
               if x == "Young" or x == "Myope" or x == "Yes" or x == "Normal":
                   xRow.append(1)
               elif x == "Prepresbyopic":
                   xRow.append(3)
               else:
                   xRow.append(2)
           X_test.append(xRow)

           if row[-1] == "Yes":
               Y_test=1
           else:
               Y_test=2

           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here

           if clf.predict(X_test)[-1]==Y_test:
               numTrue+=1
           accuracy.append(numTrue/len(data))

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    avg=0
    for a in accuracy:
        avg+=a
    avg/=len(accuracy)

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here

    print("Final Accuracy when training on "+ ds+": "+str(round(avg*100,2))+"%")




