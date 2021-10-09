import csv
import plotly.express as px
import numpy as np

def plotFigure(path):
    with open(path) as p:
        csv_reader = csv.DictReader(p)
        fig = px.scatter(csv_reader,x = "Days Present",y = "Marks In Percentage")
        fig.show()

def getData(path):
    Marks_In_Percentage = []
    Days_Present = []
    with open(path) as p:
        csv_reader = csv.DictReader(p)
        for row in csv_reader:
             Marks_In_Percentage.append(float(row["Marks In Percentage"]))
             Days_Present.append(float(row["Days Present"]))
    return{"x":Marks_In_Percentage,"y":Days_Present}
def findCorrelation(data):
    corel = np.corrcoef(data["x"],data["y"])
    print (corel[0,1])
def setup():
    path = "Student Marks vs Days Present.csv"
    a=getData(path)
    findCorrelation(a)
    plotFigure(path)

setup()
