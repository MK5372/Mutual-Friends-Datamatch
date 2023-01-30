import json

# both given
people = []
email_dict = {}

file = open("MutualF.json")

data = json.load(file)

for p in data["crushes"].keys():
    people.append(p)

#print(people)

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
        e1 = email_dict[data['crushes'][person]['email1']]
        e2 = email_dict[data['crushes'][person]['email2']]
        if e1 is not person and e1 not in edges[person] and person not in edges[e1]:
            edges[person].append(e1)
            edges[e1].append(person)
        if e2 is not person and e2 not in edges[person] and person not in edges[e2]:
            edges[person].append(e2)
            edges[e2].append(person)
print(edges)

#weighting ----> .066



      

file.close()
  
