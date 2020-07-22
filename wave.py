import json

today=[]

for line in open('today.json.gz_out','r'):
    today.append(json.loads(line))
'''
with open("today.json.gz_out",'a') as f:
    for line in f:
        today.append(json.load(line))
''' '''
dictionay = { "t" : today}
print(dictionay)
'''
# print(today[0]['urlh'])

u_set = set()
for line in today:
   
    #for URLH in  line['urlh']:
    u_set.add(line['urlh'])
#print(len(u_set))
us = len(u_set)

#test urlh count
#convert set to list
#ul = list(u)
#print(ul[0])
#a=0
#if '90d8967979b37a682553c116629e86f7f2c4efbb' in u:
#    a+=1
#print(a)
'''
print(len(u))
print(u)
'''  
u_list = []
for line in today:
    u_list.append(line['urlh'])
#print(len(u_list))
#print(u_list[1])
ul = len(u_list)
num = ul - us 
print("number of URLH which are overlapping is = " ,num)

