#XML1
import xml.etree.ElementTree as ET
data = ''' <person>
<name>Chuck</name>
<phone type ="intl">99878 56678</phone>
<email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text) #find retrievs the NODE
print('Attr:',tree.find('email').get('hide'))
print('Phone:',tree.find('phone').get('type'))
print('Phone:',tree.find('phone').text)
print("-----------------------------")

#XML2
import xml.etree.ElementTree as ET
data1 = '''<stuff>
<users>

<user x='2'>
<name>Shrisha</name>
<id>002</id>
</user>

<user x='7'>
<name>Chichi</name>
<id>007</id>
</user>

</users>
</stuff>'''

stuff = ET.fromstring(data1)
userz = stuff.findall('users/user')
print("count of users",len(userz))
for each in userz:
    print('Name:',each.find('name').text)
    print('id:',each.find('id').text)
    print('Attribute---',each.get('x'))

#-------------------------------------------------------------------------------------------------
import json

dataa = '''[
    {
        "name": "chuck",
        "id": "002",
        "x": "2"
    },
    {
        "name": "markle",
        "id": "007",
        "x": "7"
    }
]'''

item = json.loads(dataa)
print("users:",len(item))
for item1 in item:
    print('name:',item1['name'])
    print('id:',item1['id'])
    print('x:',item1['x'])