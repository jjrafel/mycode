import re
from job_variables import *
from jobfunctions import *

sortedlist=[]
sortedlist2=[]
salarylist=[]

def jobtypefilter(jobtype, jobdata):
    x=0
    for i in jobdata:
        if jobdata[x]["type"] == jobtype:
            sortedlist.append(jobdata[x])
        x+=1
def salaryfilter(jobsalary):
    x=0
    for i in sortedlist:
        salarylist.append(int(re.sub("[Salary: $,]","",sortedlist[x]["salary"])))

        if salarylist[x] > jobsalary:
            sortedlist2.append(sortedlist[x])
            #print(sortedlist2)
        x+=1
    return x
    
def resultformat(jobsalary):
    x=len(sortedlist2)
    y=0
    print("Here are available jobs that meet your criteria:\n")
    for i in range(x):
        z=sortedlist2[y]
        print("------")
        print(z["title"])
        print(z["shift"])
        print(z["salary"])
        y+=1
    

