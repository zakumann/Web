members = ['sentai','gavan']
for x in members:
    print('toei',x)
    
members2 = [
    ['sentai', 'tokyo', 'trooper'],
    ['kamen', 'kyoto', 'hero'],
    ['gavan', 'space', 'sherif']
]
print(members2[0][2])
for member in members2:
    print(member[0], member[1])
    
chosen = ['chosen', 'prison','knight']
chosen2 = {'name':'chosen', 'born':'prison', 'job':'knight'} # 사전형
print(chosen2['born'])
for name in chosen2:
    print(chosen2[name])
    
members3 = [
    {'name':'john', 'city':'washington', 'job':'soldier'},
    {'name':'Ken', 'city':'Tokyo', 'job':'journalist'}
]
for member in members3:
    print(member['name'])