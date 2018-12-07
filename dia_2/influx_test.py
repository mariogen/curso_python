from influxdb import InfluxDBClient
from random import random
from datetime import datetime, timedelta
from tqdm import tqdm
from matplotlib.pyplot import plot

host='localhost'
port=8086
database = 'test'
query = 'select latitude,longitude from coordenadas'
body = {
    'measurement': 'coordenadas',
    'tags': {
        'clima': 'ensolarado',
    },
    'time': '2018-01-01T00:00:00Z',
    'fields': {
        'latitude': 0,
        'longitude': 0,
    }
}

client = InfluxDBClient(host, port, database=database)
client.drop_database(database)
client.create_database(database)

initialTime = datetime(2018,1,1)
hour = timedelta(days=1)

for i in tqdm(range(365)):
    body['time'] = (initialTime+i*hour).isoformat()+'Z'
    body['fields']['latitude'] += random() - 0.5
    body['fields']['longitude'] += random() - 0.5
    if random() > 0.99 :
        body['tags']['clima'] = 'nublado' if body['tags']['clima'] == 'ensolarado' else 'ensolarado'
    
    client.write_points([body])

result = list(client.query(query).get_points())

latitude = [point['latitude'] for point in result]
longitude = [point['longitude'] for point in result]

plot(latitude, longitude)

print('Result: {0}'.format(result))
