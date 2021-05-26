import bs4
import re
import requests
import json

res = requests.get('https://www.goavidhansabha.gov.in/member.php')
soup = bs4.BeautifulSoup(res.text,'html.parser')

contantTable = soup.find('div', {"class":"mla-list"})
rows = contantTable.find_all('div',{"class":"details-blk"})
count=0
result=[]
for text in rows :
    if count<40:
        dict={}
        a=(' '.join(text.text.split()))
        b=a[a.index('-')+1:a.index('Constituency :')]
        try :
            b=b[b.index('Shri.')+5:]

        except ValueError:
            try:
                b = b[b.index('Smt.') + 4:]
            except ValueError:
                b=b

        dict['name']=b
        c=a[a.index('Constituency :')+15:a.index('Party :')]
        dict['area']=c
        d=a[a.index('Party :')+8:]
        dict['party']=d
        count=count+1
        print(b)
        result.append(dict)

c=0
list1=[]
for i in result:
    dict={}
    dict['uid']=""
    dict['Name']=i['name']
    a=i['name'].split()
    c=str(a[-1])+' '+str(a[0])

    dict['alias_name']=c
    dict['country']="India"
    dict['list_type']=""
    dict['address']=i['area']
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
    dict4['sl_source']='7th GOA Legislative Assembly '
    dict4['sl_type']=''
    dict4['sl_url']='https://www.goavidhansabha.gov.in/member.php'
    dict4['sl_authority']=''
    dict4['sl_host_country']='India'
    dict['sanctions_list']=dict4
    list1.append(dict)
list1=json.dumps(list1)
print(list1)
