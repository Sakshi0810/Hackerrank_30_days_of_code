#!/bin/python

import math
import os
import random
import re
import sys
a=int(input())
if(a%2==0):
    if(a>=2 and a<=5 or a>20):
        print("Not Weird")
    if(a>=6 and a<=20):
        print("Weird")  
else:
    print("Weird")    
