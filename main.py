from csvp import *


#k=read("snakes_count_100.csv")
#k=read("annual-enterprise-survey-2019-financial-year-provisional-csv.csv")

#for zw in k:
#    print(zw)


with write("test",["a","b"]) as f:
    for i in range(100):
        f({"a":3*i,"b":4*i})






