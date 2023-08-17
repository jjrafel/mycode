import itertools
import re
#def jobhunt():

jobsalary=input("Job salary desired:\n$")
"""jobtype=input("Job position preferred:\n1. Networking\n2. Software Development\n
#        3. Systems Engineer\n4. IT Specialist\n5. Any position\n")
jobshift=input("Job hours preferred:\n1. 12am - 8am\n 2. 8am - 4pm\n3. 4pm - 12am\n4. Any shift\n")
jobsalary=input("Job salary desired:\n$")
match jobtype:
    case 1:
        
        selection=input(f"Job ")
        
    case 2:
        p
    case 3:
        d
    case 4:
        f
    case 5:"""

def fetchjobs():
    for i in jobdata:
        jobdata()
        salarylist=[]=int(re.sub("[Salary: $,]","",jobdata["salary"]))
        return
fetchjobs()
print(salarylist)

#salaryf=int(re.sub("[Salary: $,]","",job1[2]))
#salaryf=int(Job1[2].replace('$',",",'')


def jobdata():
    jobdata=[
    {
        "title":"Network Engineer",
        "shift":"Hours: 8am - 4pm",
        "salary":"Salary: $92,000",
        },
    {
        "title":"Software Dev",
        "shift":"Hours: 4pm - 12am",
        "salary":"Salary: $135,000",
        },
    {
        "title":"Systems Engineer",
        "shift":"Hours: 12am - 4pm",
        "salary":"Salary: $69,000",
        },
    ]
    return
