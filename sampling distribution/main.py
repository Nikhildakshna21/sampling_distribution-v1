import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

data = pd.read_csv('medium_data copy.csv')['claps'].to_list()

population_mean = st.mean(data)

def sample_mean():
    samples=[]
    for a in range(0,29):
        rand_index = random.randint(0,len(data)-1)
        samples.append(data[rand_index])
    
    return st.mean(samples)

def setup():
    mean_list=[]
    for a in range(0,99):
        mean_list.append(sample_mean())

    return mean_list

mean_list = setup()
samples_mean = st.mean(mean_list)
samples_stdev = st.stdev(mean_list)

print(population_mean,samples_mean)

def plot():
    dist=ff.create_distplot([mean_list],['mean'],show_hist=False)
    
    #adding the traces
    dist.add_traces(data=[go.Scatter(x=[samples_mean-samples_stdev,samples_mean-samples_stdev],y=[0,0.005],name='stdev',mode='lines'),go.Scatter(x=[samples_mean+samples_stdev,samples_mean+samples_stdev],y=[0,0.005],name='stdev',mode='lines')])
    dist.add_trace(go.Scatter(x=[samples_mean,samples_mean],y=[0,0.005],mode='lines',name='mean of mean'))
    
    dist.show()

plot()

