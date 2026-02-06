weather= (1,0,1,1,1,1,0)
sunny = 0
rain = 0
for i in range(0,7):
    if (weather[i]==0):
        rain+=1
    else:
        sunny +=1
if (sunny>rain):
    print("good weather")
else:
    print("bad weather")