# Python program to read
# json file


import json

# Opening JSON file
f = open('DATA.json','rb')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
c=0
list1=[]
for i in data:
	dict={}
	# print(i)
	dict['uid'] = ""
	try:
		name=i['name']+' '+i['patronymic']+' '+i['surname']
	except KeyError:
		name=i['name']+" "+i['surname']
	dict['Name'] = name
	dict['alias_name'] = ""
	dict['country'] = ""
	dict['list_type'] = ""
	dict['address'] = ""
	dict['last_updated'] = ""
	dict2 = {}

	dict2['comment'] = ''
	dict2['Date of Imposition of Sanction'] = ""
	dict2['Sanction Imposed'] = ''
	dict['entity_details'] = dict2
	dict3 = {}
	dict3['passport'] = ""
	dict3['ssn'] = ''
	dict3['other_id'] = ''
	dict['documents'] = dict3
	dict4 = {}
	dict4['sl_source'] = 'Committee on financial monitoring of the Ministry of finance of the Republic of Kazakhstan'
	dict4['sl_type'] = ''
	dict4['sl_url'] = 'https://kfm.gov.kz/ru/the-list-of-organizations-and-individuals-associa/current.html'
	dict4['sl_authority'] = ''
	dict4['sl_host_country'] = ''
	dict['sanctions_list'] = dict4
	# try:
	# 	dict['DOB']=i['DOB']
	# except KeyError:
	# 	dict['DOB']=None
	# try:
	# 	dict['IIN']=i['IIN']
	# except KeyError:
	# 	dict['IIN']=None
	# dict['Reference']='https://kfm.gov.kz/ru/the-list-of-organizations-and-individuals-associa/current.html'
	# print(dict)
	c=c+1
	# print(c)
	list1.append(dict)
list1=json.dumps(list1)
print(list1)


# Closing file
f.close()
