phone = {'mike' : '702-123-456'} #Key : Value

phone['john'] = '619-222-3300'


#print(phone['mike']) # Access the value of Key

#print('mike' in phone.keys()) #Validate keys in a dict.

#print('mike' in phone.values()) # validate values in a dict.



statesDict = { 'California':38802000, 'Texas':26956000, 'Florida':19893000,
'New York':19746000, 'Illinois': 12880000,
'Pennsylvania': 12787000, 'Ohio':11594000,
'Georgia': 10097000, 'North Carolina': 9943964,
'Michigan':9909000, 'New Jersey': 8938000
}

for state in statesDict:
    population = statesDict[state]
print (state, population)


word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
    print(d)

name = 'Jackie'
print('Whatcha havin, {}'.format(name))


