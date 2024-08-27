import pandas as pd
data = {
    "clories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar)

#Adding index (it will take place instead of 0,1,2)

data = {
    "clories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data,index = ["day1","day2","day3"])
print(myvar)
