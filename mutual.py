import json

# both should be given already
people = []
email_dict = {}

file = open("MutualF.json")

data = json.load(file)

for p in data["crushes"].keys():
    people.append(p)

#print(people)
# matching emails to people which shouldn't be necessary in main algorithm since it'll be given
for key in people:
    em1 = data['crushes'][key]['email1']
    em2 = data['crushes'][key]['email2']
    names = em1.split('@')[0]
    names2 = em2.split('@')[0]
    if em1 not in email_dict:
        email_dict[em1] = names
    if em2 not in email_dict:
        email_dict[em2] = names2
      
#print(email_dict)

#people
edges = {}
for person in email_dict.keys():
    edges[email_dict[person]] = []
  
for person in edges.keys():
    if person in data['crushes']:
      if data['crushes'][person]['email1'] in email_dict:
      	e1 = email_dict[data['crushes'][person]['email1']] #assuming the email is in the system
        if e1 is not person and e1 not in edges[person] and person not in edges[e1]:
          edges[person].append(e1)
          edges[e1].append(person)
          
      if data['crushes'][person]['email2'] in email_dict:
      	e2 = email_dict[data['crushes'][person]['email2']] #assuming the email is in the system
        if e2 is not person and e2 not in edges[person] and person not in edges[e2]:
          edges[person].append(e2)
          edges[e2].append(person)

print(edges)


#find number of mutual friends among crushes

def check_friends(l1, l2):
  l_new = l1 + l2
  return len(l_new) - set(l_new)


weight_dict = {}

for name in email_dict:
  weight_dict[name] = 0

isvalid = True
while isValid:
  for person in data['crushes']:
  	e1 = email_dict[data['crushes'][person]['email1']]
    e2 = email_dict[data['crushes'][person]['email2']]
    mutual_friends = check_friends(edges[e1], edges[e2])
    compatibility_increase = (mutual_friends ** 1.1) / 100
    weight_dict[person] += compatability_increase
		


file.close()
  

'''
{
    "crushes": {
        "cat": {
            "email1": "alice@college.harvard.edu",
            "email2": "bob@college.harvard.edu"
        },
        "bob": {
            "email1": "bob@college.harvard.edu",
            "email2": "cat@college.harvard.edu"
        },
        "lilly": {
            "email1": "derek@college.harvard.edu",
            "email2": "lilly@college.harvard.edu"
        },
        "alice": {
            "email1": "derek@college.harvard.edu",
            "email2": "sammy@college.harvard.edu"
        },
        "derek": {
            "email1": "sammy@college.harvard.edu",
            "email2": "zayn@college.harvard.edu"
        },
        "zayn": {
            "email1": "zayn@college.harvard.edu",
            "email2": "jamie@college.harvard.edu"
        },
        "aaa": {
            "email1": "aaa@college.harvard.edu",
            "email2": "bbb@college.harvard.edu"
        },
        "bbb": {
            "email1": "bbb@college.harvard.edu",
            "email2": "ccc@college.harvard.edu"
        },
        "ccc": {
            "email1": "jamie@college.harvard.edu",
            "email2": "ccc@college.harvard.edu"
        }
    }
}


'''
