import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv('data.csv')
data = df['reading_time'].to_list()

mean = statistics.mean(data)
stdev = statistics.stdev(data)

print('Mean and Standard deviation are {}, {} respectively'.format(mean,stdev))

def mean(counter):
    data_set=[]
    for i in range (0,counter):
        rand_index = random.randint(0,len(data))
        value = data[rand_index]
        data_set.append(value)

    temp_mean = statistics.mean(data_set)
    return temp_mean


def show_fig(data,sampling_stdev):
    df = data
    sampling_mean = sum(df)/len(df)
    print('Sampling mean is {}'.format(sampling_mean))
    z_score = (sampling_mean-mean)/stdev
    print("Z-Score of the data is ",z_score)

    first_std_deviation_start,first_std_deviation_end=sampling_mean-sampling_stdev,sampling_mean+sampling_stdev
    second_std_deviation_start,second_std_deviation_end=sampling_mean-(2*sampling_stdev),sampling_mean+(sampling_stdev*2)
    third_std_deviation_start,third_std_deviation_end=sampling_mean-(3*sampling_stdev),sampling_mean+(sampling_stdev*3)
    fig=ff.create_distplot([df],['mean_list'],show_hist=False)
    fig.add_trace(go.Scatter(x=[sampling_mean,sampling_mean],y=[0,0.8],mode="lines",name="SAMPLING MEAN"))
    fig.add_trace(go.Scatter(x=[mean_t,mean_t],y=[0,0.8],mode="lines",name="MEAN"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="first_std_deviation_end"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="second_std_deviation_end"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="third_std_deviation_end"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="first_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="second_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="third_std_deviation_start"))
    fig.show()

def setup():
    mean_list=[]
    
    for i in range (0,100):
        set_of_means=mean(30)
        mean_list.append(set_of_means)
    
    sampling_stdev=statistics.stdev(mean_list)
    print("Stdev of the Sampling Distribution is ",sampling_stdev)
    
    show_fig(mean_list,sampling_stdev)

setup()
