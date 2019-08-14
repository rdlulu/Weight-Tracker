import os
import pandas as pd
import numpy as np
import seaborn as sbn
import datetime 
import matplotlib.pyplot as plt

'''
this application is to track the daily weight change and visualize in a daily manner; 
the result can be shared and queried by more than one people

'''
class WeightTracker:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.datetime.today()
        self.weights = pd.DataFrame(columns = ['date','weight'])
        #self.autoupdater()
    
    def update(self):
        weights = self.weights
        date = input("enter today's date")
        weight = input("enter your weight")
        if date in weights['date'].unique():
            self.weights.loc[weights['date'] == date, 'weight'] = weight 
        else:
            #print('here!')
            self.weights = weights.append({'date': date, 'weight' : weight}, ignore_index = True)
        
    def autoupdater(self):
        while True:
            date = datetime.datetime.today()
            if date in self.weights:
                continue
            else:
                self.weights[date] = -1
            time.sleep(3600*24) #sleep for a day and check again
        raise RuntimeError('The auto time updator is stopped!!!')
    
    def plot(self):
        #dataset = sbn.load_dataset(self.weights)
        chart = sbn.lmplot(x = "date", y = "weight", data = self.weights)
        sbn.plot.show()
        

if __name__ == '__main__':
    user_id = input('tell me your name!!')
    tracker = WeightTracker(user_id)
    for i in range(3):
        tracker.update()
    tracker.plot()
