num = [1,3,5,7,8,7,10,50,3]
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[j] == num[i]:
            print("Duplicate found", + num[i])