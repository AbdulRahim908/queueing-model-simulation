import math
import pandas as pd
import random
import streamlit as st
st.title("Simulation of M/M/1")
#importing required libraries
import math
import pandas as pd
import random
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#Graph plot Section
def entVsWT(s_no,WT):
    plt.bar(s_no, WT, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Wait Time')
    plt.title('Wait Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    st.pyplot()

def entVsTA(s_no,TA):
    plt.bar(s_no, TA, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Turn Around Time')
    plt.title('Turn Around Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    # plt.show()
    st.pyplot()

def entVsArrival(s_no,arrival):
    plt.bar(s_no, arrival, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Arrival Time')
    plt.title('Arrival Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    st.pyplot()

def entVsService(s_no,service):
    plt.bar(s_no, service, align='center', alpha=0.7)
    plt.xlabel('Customers')
    plt.ylabel('Service Time')
    plt.title('Service Time in Queue for Each Customer')
    plt.xticks(s_no)
    plt.tight_layout()
    st.pyplot()
    return s_no,service
def ServerUtilization(Server_util):
    idleTime=1-Server_util
    #print(idleTime,Server_util)
    y = np.array([Server_util,idleTime])
    mylabels = ["Utilized Server", "Idle time"]

    plt.pie(y, labels = mylabels,autopct='%1.1f%%')
    st.pyplot() 

def mm1(lembda,meu,ran_no):
    #initializing required lists
    s_no=[]
    cp=[]
    cpl=[0]
    int_arrival=[]
    arrival=[]
    service=[]
    TA=[]
    WT=[]
    RT=[]
    value=0

    #Generating values for serial number, cummulative probability and cummulative probability lookup
    for x in range(0,ran_no):
        s_no.append(x)
        value=value+(((math.exp(-lembda))*lembda**x)/math.factorial(x))
        cp.append(float("%.4f"%value))
        cpl.append(cp[-1])
    cpl.pop(-1)

    #Generating values for inter-arrival time 
    for i in range(ran_no):
        ran_var=float("%.4f"%random.uniform(0,1))
        #print(ran_var)
        for j in range(ran_no):
            if cpl[j]<ran_var and ran_var<cp[j]:
                #print(cpl[j],ran_var,cp[j])
                int_arrival.append(j)

    #Generating values for arrival time
    arrival.append(int_arrival[0])
    for i in range(1,ran_no):
        arrival.append(int_arrival[i]+arrival[i-1])

    #Generating values for service time
    for i in range(ran_no):
        service.append(math.ceil(-meu*math.log(random.uniform(0,1))))
    #Initializing Servers
    S=[]
    E=[]
    S.append(arrival[0])
    E.append(S[0]+service[0])
    
    #Assigning customers to server
    for i in range(1,ran_no):
        if arrival[i]>=E[-1]:
            S.append(arrival[i])
            E.append(S[-1]+service[i])
            
        elif arrival[i]<E[-1]:
            S.append(E[-1])
            E.append(S[-1]+service[i])

    #Generating values for TurnAround time,Wait time and Response Time     
    for i in range(ran_no):
        TA.append(E[i]-arrival[i])
        WT.append(TA[i]-service[i])
        RT.append(S[i]-arrival[i])

    #Server utilization calculation
    if lembda>=meu:
        Server_util=meu/lembda
    elif meu>=lembda:
        Server_util=lembda/meu

    #Avg values of the time given
    avg_interarrival=(np.sum(int_arrival))/ran_no
    avg_service=(np.sum(service))/ran_no
    avg_TA=(np.sum(TA))/ran_no
    avg_WT=(np.sum(WT))/ran_no
    avg_RT=(np.sum(RT))/ran_no
    #printing simulation table and generating list for gantt chart
    result=[cp,cpl,int_arrival,arrival,service,S,E,TA,WT,RT]
    df=pd.DataFrame(result,index=["CP","CPL","Inter-arrival","Arrival","Service","Start","End","TurnAround","WaitTime","ResponseTime"])
    df=df.transpose()
    pd.set_option('display.max_columns', None)
    return df,s_no,arrival,service,WT,RT,TA,Server_util,avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT
lembda=st.number_input("Mean arrival rate",step=1.,format="%.2f")
meu=st.number_input("Mean service rate",step=1.,format="%.2f")
ran_no=st.number_input('random numbers', 1,50)

df,s_no,arrival,service,WT,RT,TA,Server_util,avg_interarrival,avg_service,avg_TA,avg_WT,avg_RT=mm1(lembda,meu,ran_no)

st.write(df)
st.write("Average Inter-Arrival Time=",avg_interarrival,"\nAverage Service Time=",avg_service,"\nAverage Turn-Around Time=",avg_TA,"\nAverage Wait Time=",avg_WT,"\nAverage Response Time=",avg_RT)
if st.button('Generate Plot'):
     st.set_option('deprecation.showPyplotGlobalUse', False)
     entVsWT(s_no,WT)
     entVsTA(s_no,TA)
     entVsArrival(s_no,arrival)
     entVsService(s_no,service)
     ServerUtilization(Server_util)
# st.set_option('deprecation.showPyplotGlobalUse', False)
