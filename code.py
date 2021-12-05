import csv
import random
import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv("score.csv")
data=df["Math_score"].tolist()

fig=ff.create_distplot([data],["mathScore"],show_hist=False)
# fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)
print("mean of population-",mean)
print("stdev of population-",std)

def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean
meanlist=[]
for i in range(0,1000):
    setOfmeans=randomSetOfMean(100)
    meanlist.append(setOfmeans)

std_deviation=statistics.stdev(meanlist)
mean=statistics.mean(meanlist)
print("std of sample-",std-std_deviation)
print("mean of sample-",mean)
fig=ff.create_distplot([meanlist],["mathScore"],show_hist=False)
# fig.show()

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

print("std1",first_std_deviation_start, first_std_deviation_end)
print("std1",second_std_deviation_start, second_std_deviation_end)
print("std1",third_std_deviation_start, third_std_deviation_end)

fig = ff.create_distplot([meanlist], ["student marks"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()