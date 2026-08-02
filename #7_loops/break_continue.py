for i in range(51):
    if i == 31:                        # loop will end when i == 31
        break
    print(i)

for i in range(51):
    if(i == 30 or i == 45):             # 30 and 45 will not get print , will be skipped
        continue
    print(i)