time=input("enter Hour,minutes and second")
time=time.split(" ")
sum = ((int(time[0]) * 3600)+(int(time[1]) * 60)+int(time[2]))
print(sum)