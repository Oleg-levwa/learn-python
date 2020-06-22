#list_number = [3, 5, 7, 9, 10.5]
#print (list_number)

#list_number.append('Python')
#print (list_number)
#print (len(list_number))
#print (list_number[0])
#print (list_number[-1])
#print (list_number[1:4])
#list_number.remove('Python')
#print (list_number)

city = {
    'city': 'Москва',
    'temperature': '20'
}
#print(city['city'])

city['temperature'] = int(city['temperature'])
#print (type(city['temperature']))
city['temperature'] -= 5
print (city)
print (city.get('country', 'Россия'))
city['date'] = '27.05.2019'
print(len(city))
print (city)


