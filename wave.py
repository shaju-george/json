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
print("number of URLH which are repeating inside today.json itself = " ,num)

yesterday=[]

for line in open('yesterday.json.gz_out','r'):
    yesterday.append(json.loads(line))

y_set = set()
for line in yesterday:
    y_set.add(line['urlh'])
#print(len(y_set))

overlapping= []
#over = 0
diff =0
for i in u_set:
    if i in y_set :
        #over+=1
        overlapping.append(i)
        '''
        for j in today:
            try :
                if i in j['available_price']:
                     temp= float(j['available_price'])
                     diff = diff - temp
            except TypeError as t:
                pass
            
        '''

#print(len(overlapping))

#print(over)
#print("number of URLH which are overlapping between today.json and yesterday.json = " ,over)
print("1) number of URLH which are overlapping between today.json and yesterday.json = " ,len(overlapping))

over = u_set.intersection(y_set)
print(len(over))
'''
y_list = list()
for line in yesterday:
    y_list.append(line['urlh'])
#print(len(y_set))




over = 0
for i in u_list:
    if i in y_list :
        over+=1

#print(over)
print("number of URLH which are overlapping between today.json and yesterday.json when repetation is allowed = " ,over)

'''

'''
diff=0.0
for line in today:
    for i in overlapping:
        
        if i in line['urlh']:
            try:
                temp= float(line['available_price'])
                diff = diff - temp
            except TypeError:
                pass
print(diff)
'''          
#some where 'available_price' is returning None type!
