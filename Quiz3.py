#3
#방법1
for i in range(1, 21):
    if i % 2 == 1:
        print("A" + str(i), end=" ")

#방법2
for i in range(1, 21)[::2]:
    print("A" + str(i), end=" ")