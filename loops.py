# value = 0
# while value < 10 :
#     print(value)
#     value = value + 1


# value = 0
# while value < 10 :
#     if value == 5 :
#         value = value + 1
#         break
#     print(value)
#     value = value + 1


sample = ["server1", "server2", "server3", "server4",1234]

# idx = 0
# while idx < len(sample):
#     print (sample[idx])
#     idx += 1

# for idx in sample:
#     print(idx)   

for idx in range(len(sample)):
    ele = sample[idx]
    print(idx,ele)