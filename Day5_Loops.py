#!/bin/python

import math
import os
import random
import re
import sys

n = int(raw_input())
if(2<=n<=20):
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(n, i, n*i))
