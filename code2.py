import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd


df = pd.read_csv("StudentsPerformance.csv")
dice_result = df["reading score"].tolist()
#Calculating the mean and the standard deviation
mean = sum(dice_result) / len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)
#add_trace will trace the mean 
#go.scatter creates a line graph
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

#Printing the findings
#if a result is in the class interval of firstStd and second n third ...they are added to their respective list
list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))
#finding the length of the list and finding its percentage using {}%
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))
