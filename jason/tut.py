import json
# person = {"name":"arati","age":22,"city":"kathmandu","haschildren":False,"titles":["engineer","artist","programmer"]}
# personJSON = json.dumps(person, indent=4, sort_keys=True) #in the key word 'dumps'  's' stands for string
# print(personJSON)

# # #to convert python file to json file
# # with open('person.json','w') as file:
# #     json.dump(person, file, indent=4)

# #to convert json format to python format
# person = json.loads(personJSON) #in keyword loads 's' stands for string
# print(person)

# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person )

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
user = User('max', 22)

def encode_user(o):
    if isinstance(o, User):
        return{'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')
    
from json import  JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return{'name':o.name,'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self, o)
    
        
 
userJSON = UserEncoder().encode(user)
print(userJSON)

user = json.loads(userJSON)
print(type(user))



