import json
from collections import Counter

today=[]

for line in open('today.json.gz_out','r'):
    today.append(json.loads(line))

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

#1. No of URLH which are overlapping.
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
print("1) number of URLH which are overlapping between today.json and yesterday.json = " ,len(overlapping))

# or
#over = u_set.intersection(y_set)
#print(len(over))

print(":) __________________________________ :)")
print()

#2 

'''
price=[]
for item in overlapping:
    for (i , j) in zip(today,yesterday):
        if j["available_price"] == None and i["available_price"] == None:
            pass
        else:
            x = i["available_price"]
            print(x)
            y=j["available_price"]
            diff = float(x)-float(y)
            price.append(diff)
print(price)      
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

#3 No of Unique categories in both files.

cata_t = set()
subcategory_t =[]
for line in today:
    cata_t.add(line['category'])
    subcategory_t.append(line['subcategory'])
print(' No of Unique categories in today.json ',len(cata_t))

cata_y = set()
subcategory_y =[]
for line in yesterday:
    cata_y.add(line['category'])
    subcategory_y.append(line['subcategory'])
print(' No of Unique categories in yesterday.json ',len(cata_y))


unique = cata_t
for category in cata_y:
    unique.add(category)
print(' 3) No of Unique categories in both files ',len(unique))

print(" :) __________________________________ :)")
print()

#4
cata_tlist= list(cata_t)
cata_ylist=list(cata_y)
#unique = list(unique)

cata_over = cata_y.intersection(cata_t)

for category in cata_over:
    unique.remove(category)
print('  4) List of categories which is not overlapping = ',len(unique))
print("  :) __________________________________ :)")
print()

#5. Generate the stats with count for all taxonomies 

'''

today_new= []
for dic in today:
    today_new= ([key,val] for key, val in dic.items() if key =='subcategory' )
print(today_new[0])
Counter(today_new)
#print(json.dumps(today_new,indent=0,separators=(">","=")))
#print(type(today_new))
'''
'''
for i in today_new[0:3]:
    today.remove
    (json.dumps(i,indent=0,separators=(">","=")))
 
''' '''
today_new=[]

for line in x:
    today_new.append(json.loads(line))

print(today_new[0])
'''


tommorow = today + yesterday
sub_total=subcategory_t+subcategory_y
cou= Counter(sub_total)
subcategory_yset =set(subcategory_y)


for line in tommorow:
    if line['category'] in cata_y and line['subcategory'] in subcategory_yset :
        print(line['category'] , ' > ', line['subcategory'],'=',cou[ line['subcategory']])
        subcategory_yset.remove(line['subcategory'])
    
print("   :) __________________________________ :)")
print()

#6. Generate a new file where mrp is normalized.


for line in today:
    if line['mrp'] == '0' or line['mrp'] == None:
        line['mrp'] = "NA"

with open('data.json', 'w') as outfile:
    json.dump(today, outfile)



        