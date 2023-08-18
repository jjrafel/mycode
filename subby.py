#!/usr/bin/env Python3

from subprocess import call
from subprocess import check_output

call(['ip','link','show','up'])
print("This program will check your interfaces.")
interface="ens3"
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])

