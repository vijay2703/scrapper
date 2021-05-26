# Python program to read
# json file


import json

# Opening JSON file
f = open('DATA2.json','rb')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
c=0
list1=[]
for i in data:
    dict={}
    dict['uid']=""
    try:
        name=i['Name']+' '+i['Patronomic']+' '+i['Surname']
    except KeyError:
        name=i['Name']+" "+i['Surname']
    dict['Name']=name
    dict['alias_name']=""
    dict['country']=""
    dict['list_type']=""
    try:
        dict['address'] = i['PlaceBirth']
    except KeyError:
        dict['address'] = None
    dict['last_updated']=""
    dict2={}

    dict2['comment']=''
    dict2['Date of Imposition of Sanction']=""
    dict2['Sanction Imposed']=''
    dict['entity_details']=dict2
    dict3={}
    dict3['passport']=""
    dict3['ssn']=''
    dict3['other_id']=''
    dict['documents']=dict3
    dict4={}
    dict4['sl_source']='State Service of Financial Intelligence under the Government of the Kyrgyz Republic'
    dict4['sl_type']=''
    dict4['sl_url']='https://fiu.gov.kg/uploads/5fc4c91fb1cf0.xml'
    dict4['sl_authority']=''
    dict4['sl_host_country']=''
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
print(list1)


# Closing file
f.close()
