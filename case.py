#!/usr/bin/env python
# coding: utf-8

# In[106]:


import numpy as np
traffic_data = np.array([100,400,340,12,53,4,8,68,12,45,10,40,23,675,34,12,53,4,8,68,12,45,10,40,23,65,34,12,53,4,8,68,12,45])

noise = np.arange(15)
def random_noise(traffic_data):
    for i in traffic_data:
        if i%10 == 0 :
            continue
        else:
            rand = 0
            prev = i
            while i%10!=0:
                i+=1
                rand+=1;
            #traffic_data[prev] = i     
            print("Random noise added of : ",rand)   
    
    return traffic_data

def vehicles_after_minute(traffic_data,val):
    s = traffic_data.size
    traffic_data[s-1] = val
    return

def average_num_vehicles_first_hour(traffic_data):
    min = 60
    avg = 0
    for i in traffic_data:
        if min>0 :
            avg+=i
            min-=1
        else:
            break
            
    return avg/min     

def average_num_vehicles_every_hour(traffic_data):
    min = 60
    avg = 0
    arr = list()
    for i in traffic_data:
        if min>0 :
            avg+=i
            min-=1
        else:
            min = 60
            arr.insert(avg/60)
            avg =0
    arr.append(avg/min)        
    return arr  

def traffic_exceeded(traffic_data):
    arr = []
    for i in traffic_data:
        if i>100 :
            arr.append(i)
        else:
            if len(arr) > 20:
                lst.append(arr)
            else:
                arr=list()
    return arr           
            


# In[95]:


vehicles_after_minute(traffic_data,10)


# In[96]:


traffic_data


# In[97]:


print(average_num_vehicles(traffic_data))


# In[98]:


average_num_vehicles_every_hour(traffic_data)


# In[113]:


import matplotlib.pyplot as plt

plt.hist(traffic_data,color='yellow')
plt.title("Traffic Data in every minute")
plt.show()


# In[90]:


arr = random_noise(traffic_data)
plt.hist(arr)
plt.title("Traffic Data after smoothing")


# In[112]:


arr = average_num_vehicles_every_hour(traffic_data)
plt.hist(arr,color='green')
plt.title("Traffic Data of hourly average") # 1 hr average is 91


# In[111]:


arr = traffic_exceeded(traffic_data)
plt.hist(arr,color='red')
plt.title("Traffic Data exceeding 100")


# In[ ]:




