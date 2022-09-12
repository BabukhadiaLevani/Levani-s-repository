from pytest import* 
''' I have changed the name as admin_users_json just for convenience
    json object has become a list'''
    
''' I have changed name as regular_users_json just for convenience 
json object has become a list
'''

'''
 1.validate that X.json contains an array of users. User must have id, name and may have 
   address, street, # building
'''



admin_users_json =[
  {
    "id": 1,
    "name": "Mike"
  },
  {
    "id": 2,
    "name": "Helen"
  },
  {
    "id": 108,
    "name": "Maya"
  },
  {
    "id": 9,
    "name": "Olive"
  }
]
regular_users_json=[
  {
    "id": 345,
    "name": "Alice",
    "address": {
      "city": "LA",
      "street": "T.Anderson",
      "building": 9
    }
  },
  {
    "id": 456,
    "name": "Ann",
    "address": {
    }
  },
  {
    "id": 987,
    "name": "Oscar",
    "address": {
      "city": "Texas",
      "street": "Winner",
      "building": 77
    }
  }
]

#for array check
validation1=type(admin_users_json)
validation2=type(regular_users_json)

assert validation1==list, "json does not contain an array of users"
assert validation2==list, "json does not contain an array of users"

#for id and name check

if "id" in admin_users_json[0].keys():
    validation_id=True
assert validation_id==True, "there is no id"
if "name" in admin_users_json[0].keys():
    validation_name=True
assert validation_name==True, "there is no name"

# we can do the same for regular_users_json

if "id" in regular_users_json[0].keys():
    validation_id_regular=True
assert validation_id_regular==True, "there is no id"
if "name" in regular_users_json[0].keys():
    validation_name_regular=True
assert validation_name_regular==True, "there is no name"


'''
I have changed yaml into a list 
'''

admin_users_yaml= [ {"id":9, "name":"Olive"},  
    { "id": 108, "name": "Maya"},
    {"id": 109, "name": "Maya"},
    {"id": 3, "name": "Mike"},
    {"id": 1, "name": "Mike"},
    {"id": 2, "name": "Helen"}
    ]


'''
I have changed yaml into a list for convenience 
'''
regular_users_yaml=[
 {"id": 345,
  "name": "Alice",
  "address": {
    "city": "LA",
    "street": "T. Anderson",
    "building": 9} },
 {"id": 987,
  "name": "Oskar",
  "address": {
    "city": "Texas",
    "street": "Winner",
    "building": 77}},
{"id": 456,
  "name": "Ann"}
]

'''
 2.validate that X.yaml contains an array of users. User must have id, name and may have 
   address, street, # building
'''

# since the code for json is genereic, we can apply it to yaml too

#for array check
validation1_yaml=type(admin_users_yaml)
validation2_yaml=type(regular_users_yaml)

assert validation1_yaml==list, "yaml does not contain an array of users"
assert validation2_yaml==list, "yaml does not contain an array of users"

#for id and name check

if "id" in admin_users_yaml[0].keys():
    validation_id_yaml=True
assert validation_id_yaml==True, "there is no id"
if "name" in admin_users_yaml[0].keys():
    validation_name_yaml=True
assert validation_name_yaml==True, "there is no name"

# we can do the same for regular_users_json

if "id" in regular_users_yaml[0].keys():
    validation_id_regular_yaml=True
assert validation_id_regular_yaml==True, "there is no id"
if "name" in regular_users_yaml[0].keys():
    validation_name_regular_yaml=True
assert validation_name_regular_yaml==True, "there is no name"

#3 validate that all users that are listed in X.json are in X.yaml


'''
to verify this, it's enough to have same ids or names, 
so I will copy names from both sides and then compare them

'''
yaml_names={}
json_names={}

for i in range(len(admin_users_json)):
    json_names[i]=admin_users_json[i]["name"]

#same goes to yaml

for i in range(len(admin_users_yaml)):
    yaml_names[i]=admin_users_yaml[i]["name"]

# created lsits
yaml_list=list(yaml_names.values())
json_list=list(json_names.values())


# situation wont change if we add the second parts of data-regular users

def task3_check()->bool:
    for e in json_list:
        if e not in yaml_list:
            return False
    return True

assert task3_check, "there is a mistake in task 3"

