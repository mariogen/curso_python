#https://techsupport.osisoft.com/Documentation/PI-SDK/Introducing_the_PI_SDK/PISDK_object_model.htm
#Não esquecer de cadastrar no PIProcessBook File/Connections/Servidor/Adicionar servidor {"Nó da rede": S2750AS10, "usuário": pidemo, "senha": pidemo}

from win32com.client.dynamic import Dispatch  
from datetime import datetime

PISDK = Dispatch("PISDK.PISDK")

server = PISDK.Servers("SERVER_NAME")

tag = 'TAG_NAME'

point = server.PIPoints(tag)

attributes = point.PointAttributes

for attribute in attributes:
    print(attribute.Name,'==>',attribute.Value)

snapshot = point.Data.Snapshot

value = snapshot.Value

timeStamp = snapshot.TimeStamp.UTCseconds

time = datetime.fromtimestamp(timeStamp)

isGood = snapshot.IsGood

#see strftime.org for time string formatting
#and docs.python.org/3.6/library/string.html for general string formating
print('\nO ponto {tag} no instante {time} tem valor {value:.2f} com qualidade {qual}'.
          format(tag = tag,
                 time = '{:%Y-%m-%d %H:%M:%S}'.format(time),
                 value = value,
                 qual = 'good' if isGood else 'bad'))

startTime = '*-1h'
endTime = '*'
values = point.Data.RecordedValues(startTime,endTime,0,"",0,None)

timeStamps = [v.TimeStamp.UTCseconds for v in values]
isGoods = [v.IsGood() for v in values]
values = [v.Value for v in values]

print('\nO número de valores lidos é:', len(values))
if False not in isGoods:
    print('não existem pontos com qualidade ruim')
else:
    print('Qualidade ruim no instante:',timeStamps(isGoods.index(False)))

from matplotlib.pyplot import figure,plot,title
figure()
plot(timeStamps,values)
title(tag)



#point.Data.UpdateValue(value+1,timestamp+60*60,0,None)