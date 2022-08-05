import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("E:\\IP-Project\\read.csv")
while True:
    print("------------------------------------------------")
    print("1. Read/Create CSV")
    print("2. Data Visualisation")
    print("3. Data Analysis")
    print("4. Data Manupulation")
    print("5. Exit Program")
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("------------------------------------------------")
        print("-->1. Read CSV")
        print("-->2. Create CSV")
        opt1=int(input("Enter your internal choice : "))
        if opt1==1:
            print("------------------------------------------------")
            print(df)
        elif opt1==2:
            print("------------------------------------------------")
            d=eval(input("Enter data : "))
            newdf=pd.DataFrame(d)
            newdf.to_csv("E:\\IP-Project\\created.csv")
            print("File created at : E:\IP-Project")
            print("------------------------------------------------")
        else:
            print("------------------------------------------------")
            print("Enter Valid Choice !!!")
            print("------------------------------------------------")
    elif choice==2:
        print("------------------------------------------------")
        print("-->1. Line Graph")
        print("-->2. Bar Graph")
        print("-->3. Histogram")
        opt2=int(input("--> Ener your internal choice : "))
        if opt2==1:
            df.plot.line()
            plt.show()
        elif opt2==2:
            df.plot.bar(x="Name")
            plt.show()
        elif opt2==3:
            df.plot.hist()
            plt.show()
        else:
            print("------------------------------------------------")
            print("Enter Valid Choice !!!")
            print("------------------------------------------------")
    elif choice==3:
        print("------------------------------------------------")
        print("-->1. Show all records")
        print("-->2. Show first and last 5 records")
        print("-->3. Show records in a selected range")
        print("-->4. show other attributes")
        opt3=int(input("--> Enter your internal choice : "))
        if opt3==1:
            print("------------------------------------------------")
            print(df)
        elif opt3==2:
            print("------------------------------------------------")
            print(df.head())
            print("------------------------------------------------")
            print(df.tail())
        elif opt3==3:
            print("------------------------------------------------")
            startVal,stopVal=input("Enter start and stop value : ").split(",")
            print(df[int(startVal):int(stopVal):])
        elif opt3==4:
            print("------------------------------------------------")
            print("---->1. Check dataframe is empty or not")
            print("---->2. Show names of columns")
            print("---->3. Check datatype of columns")
            print("---->4. Count number of rows and columns")
            print("---->5. Transpose the Dataframe")
            attCh=int(input("----> Enter internal choice : "))
            if attCh==1:
                print("------------------------------------------------")
                print("Dataframe is Empty" if df.empty == True else "Datafame is not empty")
            elif attCh==2:
                print("------------------------------------------------")
                print("Column names are : ")
                for colName in df.columns:
                    print("------------------------------------------------")
                    print(colName,end=' | ')
                print()
            elif attCh==3:
                print("------------------------------------------------")
                print("Datatype : ",df.dtypes)
            elif attCh==4:
                print("------------------------------------------------")
                print("Co-ordinates : \n",df.shape)
            elif attCh==5:
                print("------------------------------------------------")
                print(df)
                print("------------------------------------------------")
                print("Transpose : ",df.T)
            else:
                print("------------------------------------------------")
                print("Enter Valid Choice !!!")
                print("------------------------------------------------")
    elif choice==4:
        print("------------------------------------------------")
        print("-->1. Insert new data")
        print("-->2. Delete data")
        opt4=int(input("Enter your internal choice : "))
        if opt4==1:
            print("------------------------------------------------")
            print("---->1. Add new Row")
            print("---->2. Add new Column")
            interCh=int(input("----> Enter internal choice : "))
            if interCh==1:
                print("------------------------------------------------")
                print(df)
                l=eval(input("Enter new row data : "))
                index=int(input("Enter new row index : "))
                df.loc[index]=l
                df.to_csv('E:\\IP-Project\\read.csv')
                print(df)
            elif interCh==2:
                print("------------------------------------------------")
                print(df)
                colName=input("Enter new column name : ")
                l=eval(input("Enter new column data : "))
                df[colName]=l
                df.to_csv('E:\\IP-Project\\read.csv')
        elif opt4==2:
            print("------------------------------------------------")
            print("---->1. Delete Row")
            print("---->2. Delte Column")
            interCh1=int(input("----> Enter your internal choice : "))
            if interCh1==1:
                print("------------------------------------------------")
                print(df)
                delrow=int(input("Enter row index to delete : "))
                df.drop(delrow,inplace=True)
                print(df)
                df.to_csv('E:\\IP-Project\\read.csv')
            elif interCh1==2:
                print("------------------------------------------------")
                print(df)
                delcol=input("Enter cloumn index to delete : ")
                df.pop(delcol)
                print(df)
                df.to_csv('E:\\IP-Project\\read.csv')
            else:
                print("------------------------------------------------")
                print("Enter valid Choice !!!")
                print("------------------------------------------------")
    elif choice==5:
        print("------------------------------------------------")
        print("THANK YOU :)")
        print("------------------------------------------------")
        break;
    else:
        print("------------------------------------------------")
        print("Enter Valid Choice !!!")
        print("------------------------------------------------")
