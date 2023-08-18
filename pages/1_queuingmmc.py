import math
import numpy as np
import streamlit as st
import pandas as pd

st.title("M/M/C queuing Model")

def MMC(Arrival_Mean,Service_Mean,No_of_server):
    lembda=1/Arrival_Mean
    meu=1/Service_Mean
    c=No_of_server
    p=lembda/(c*meu) #utlization factor
    
    value=0
    for m in range(c):
        value=value+(((c*p)**m)/(math.factorial(m)))+(((c*p)**c)/(math.factorial(c)*(1-p)))
        
    Pnot=1/value
    Lq=(Pnot*p*(lembda/meu)**c)/(math.factorial(c)*((1-p)**2))
    Wq=Lq/lembda
    Ws=Wq+(1/meu)
    Ls=Ws*lembda
    return Lq,Wq,Ws,Ls,Pnot
    # print("Utilizatin Factor",p,"\n","Length of Queue:",Lq,"\n","Length of system:",Ls,"\n","Wait in Queue:",Wq,"\n","Wait in system",Ws,"\n","Propotion of the time of server in idle",1-p,)
    
Arrival_Mean=st.number_input("Mean arrival rate",step=1.,format="%.2f")
Service_Mean=st.number_input("Mean service rate",step=1.,format="%.2f")
No_of_server=st.number_input('number of servers', 1, 50)

Lq,Wq,Ws,Ls,Pnot=MMC(Arrival_Mean,Service_Mean,No_of_server)
st.write("wq=",Wq)
st.write("ws=",Ws)
st.write("p=",Pnot)
st.write("lq=",Lq)
st.write("ls=",Ls)
#M/M/C
# def multi_server_exponential_queue(mean_service_time, mean_arrival_time, num_servers):
#     arrival_rate = 1 / mean_arrival_time
#     service_rate = 1 / mean_service_time
#     utilization = arrival_rate / (service_rate * num_servers)
#     wait_in_queue = utilization / (service_rate * num_servers * (1 - utilization))
#     wait_in_system = wait_in_queue + (1 / (service_rate * num_servers))
#     probability_of_server = 1 - utilization
#     length_of_queue = (utilization ** 2) / (1 - utilization)
#     length_of_system = length_of_queue + utilization
    
#     return wait_in_queue, wait_in_system, probability_of_server, length_of_queue, length_of_system

# # # Take input from the user
# # mean_service_time = float(input("Enter the mean service time: "))
# # mean_arrival_time = float(input("Enter the mean arrival time: "))
# # num_servers = int(input("Enter the number of servers: "))

# # wait_in_queue, wait_in_system, probability_of_server, length_of_queue, length_of_system = multi_server_exponential_queue(mean_service_time, mean_arrival_time, num_servers)

# # print("Wait in Queue:", wait_in_queue)
# # print("Wait in System:", wait_in_system)
# # print("Probability of Server:", probability_of_server)
# # print("Length of Queue:", length_of_queue)
# # print("Length of System:", length_of_system)

# mean_service_time=st.number_input("Mean arrival rate",1,50)
# mean_arrival_time=st.number_input("Mean service rate",1,50)
# num_servers=st.number_input('number of servers', 1, 2)


# wait_in_queue, wait_in_system, probability_of_server, length_of_queue, length_of_system =multi_server_exponential_queue(
# mean_service_time,
# mean_arrival_time,
# num_servers
# )
# st.write("wq=",wait_in_queue)
# st.write("ws=",wait_in_system)
# st.write("p=",probability_of_server)
# st.write("lq=",length_of_queue)
# st.write("ls=",length_of_system)