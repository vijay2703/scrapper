# Python program to read
# json file


import json

# Opening JSON file
f = open('csvjson.json','rb')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
c=1
list1=[]
for i in data:
	#print(i)
	dict={}
	# print(i)
	dict['uid'] = ""
	dict['Name'] = i['Name 6']
	dict['alias_name'] = ""
	dict['country'] = ['Ukraine']
	dict['list_type'] = "entity"
	dict['list_updated'] = i['Last Updated']
	dict['nns_status']=""
	dict['address'] = []
	dict2 = {}

	dict2['comment'] = ''
	dict2['Date of Imposition of Sanction'] = i['Listed On']
	dict2['Sanction Imposed'] = i['Other Information']
	dict['entity_details'] = dict2
	dict3 = {}
	dict3['CRN'] = ""
	dict3['CIN']=""
	dict['documents'] = dict3
	dict4 = {}
	dict4['sl_source'] = 'https://www.gov.uk/'
	dict4['sl_type'] = "Ukraine: list of persons subject to restrictive measures in view of Russia's actions destabilising the situation in Ukraine"
	dict4['sl_url'] = 'https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets/ukraine-list-of-persons-subject-to-restrictive-measures-in-view-of-russias-actions-destabilising-the-situation-in-ukraine'
	dict4['sl_authority'] = 'Office of Financial Sanctions Implementation HM Treasury'
	dict4['sl_host_country'] = 'Ukraine'
	dict4['sl_description'] ="Ukraine: list of persons subject to restrictive measures in view of Russia's actions destabilising the situation in Ukraine"
	dict['sanctions_list'] = dict4
	list1.append(dict)

print(list1)
list1=json.dumps(list1)
f1 = open( 'ukraine1.json', 'w' )
f1.write( list1 )
f1.close()


f.close()
