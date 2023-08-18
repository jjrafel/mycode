import re
from job_variables import *
from jobfunctions import *

#two sets of pre-made inputs
jobtype=1       #shows networking jobs
jobsalary=60000 #shows 2/2 jobs since neither are below $60000
#jobtype=2       #shows software dev jobs
#jobsalary=105000#shows 2/3 jobs, level I is below threshold salary

#lines for user input
#jobtype=input("Job position preferred:\n1. Networking\n2. Software Development\n3. Systems Engineer\n4. IT Specialist\n5. Any position\n")
#jobsalary=int(input("Job salary desired:\n$"))

jobtypefilter(jobtype, jobdata) #inputs job type (1-5) and all jobs (jobdata) from job_variables.py
                                #each job has a number based on job type which the function filters
                                #this would allow for- adding multiple job types instead of just one

salaryfilter(jobsalary)         #further filters list output from previous function using user-input salary

resultformat(jobsalary)         #takes final list/dictionary and formats to human-readable

#print(sortedlist2) #uncomment for final unformatted dictionary results
