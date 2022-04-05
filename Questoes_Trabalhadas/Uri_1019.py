tempo_segundos=int(input())
horas=tempo_segundos//3600
resto_horas=tempo_segundos-horas*3600
minutos=resto_horas//60
resto_minutos=resto_horas-minutos*60
print('{}:{}:{}'.format(horas, minutos, resto_minutos))