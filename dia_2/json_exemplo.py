#adaptado de https://github.com/ozlerhakan/mongodb-json-files

import json
import matplotlib.pyplot as plt
import pandas as pd

with open('datasets/data/country.json','r',encoding="utf8") as f:
    countries = json.load(f)

countries[0]

names = [country['name']['common'] for country in countries] 
idBrazil = names.index('Brazil')
brazil = countries[idBrazil]
#brazil = next(c for c in countries if c['name']['common'] == 'Brazil')
#next(filter(lambda c : c['name']['common'] == 'Brazil' == code, countries))

print(json.dumps(brazil,indent=4))

latlng = [country['latlng'] for country in countries]
lat,lng = zip(*latlng) #tranposição de listas

areas =  [country['area']/1000 for country in countries]

regions = [country['region'] for country in countries]


ptCoutries = [c['name']['common'] for c in countries if 'por' in c['languages']]
    
x = max(countries, key = lambda country: len(country['languages']))

x = max(countries, key = lambda country: len(country['borders']))

x = [c['name']['common'] for c in countries 
         if c['borders']==[] and 'por' in c['languages']]

x = [c['name']['common'] for c in countries 
         if c['currency']]

def code2country(code):
    return next(filter(lambda c : c['cca3'] == code, countries))

plt.figure(figsize=(16,8))
for country in countries:
    for code in country['borders']:
        border = code2country(code)
        plt.plot([country['latlng'][1],border['latlng'][1]],
                 [country['latlng'][0],border['latlng'][0]],'black')
plt.scatter(lng,lat,
            s=areas,
            c=pd.factorize(regions)[0],
            alpha=0.5)
plt.axis('off')

myCountry = {
    "altSpellings": [
        "BN",
        "Banania",
        "Findomundistão",
        "Republica Federativa das Bananas"
    ],
    "area": 10000000.0,
    "borders": [
        "BRA",
        "RUS",
        "CRO"
    ],
    "callingCode": [
        "22"
    ],
    "capital": "Jericoscow",
    "currency": [
        "BRL"
    ],
    "demonym": "Equusasinus",
    "languages": {
        "por": "Portuguese"
    },
    "latlng": [
        20,
        -25
    ],
    "region": "Outra",
    "subregion": "South America",
}

from copy import deepcopy
countries2 = deepcopy(countries)
countries2.append(myCountry)

with open('files/country.json','r',encoding="utf8") as f:
    countries = json.dump(f)




