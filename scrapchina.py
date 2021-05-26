# Python program to read
# json file


import json

# Opening JSON file
f = open('china.txt','r')

# returns JSON object as
# a dictionary
Lines = f.readlines()

# Iterating through the json
# list
c=0
list1=[]
for i in Lines:
    a = i.split(':')
    #print(a)
    dict={}
    dict['uid']=""
    dict['Name']=a[0].strip()
    dict['alias_name']=[]
    dict['country']=["China"]
    dict['list_type']="individual"
    dict['last_updated']=""
    dict['address']=[]
    dict2={}

    dict2['date_of_birth']=[]
    dict2['gender']=""
    dict2['organisation']=a[1].strip()
    dict['individual_details']=dict2
    dict3={}
    dict3['passport']=""
    dict3['ssn']=''
    dict3['other_id']=''
    dict['documents']=dict3
    dict4={}
    dict4['sl_source']='http://en.people.cn/index.html'
    dict4['sl_type']='List of ministerial members of China Cabinet'
    dict4['sl_url']='http://en.people.cn/90001/90776/90785/6375040.html#'
    dict4['sl_authority']="People's Daily"
    dict4['sl_host_country']='China'
    dict['sanctions_list']=dict4

    # try:
    #     dict['DOB']=i['DataBirth']
    # except KeyError:
    #     dict['DOB']=None
    #
    # try:
    #     dict['CATEGORY'] = i['CategoryPerson']
    # except KeyError:
    #     dict['CATEGORY'] = None
    # try:
    #     dict['DOI']=i['DateInclusion']
    # except KeyError:
    #     dict['DOI']=None
    #
    # dict['Reference']='https://kfm.gov.kz/ru/the-list-of-organizations-and-individuals-associa/current.html'
    # try:
    #     dict['OTHERS']=i['BasicInclusion']
    # except KeyError:
    #     dict['OTHERS']=None
    # # print(dict)
    # c=c+1
    # print(c)
    list1.append(dict)
list1=json.dumps(list1)
f1 = open( 'china.json', 'w' )
f1.write(list1)
f1.close()


# Closing file
f.close()
