cities = [
    {'name':'Delhi', 'population':19000000},
    {'name':'Mumbai', 'population':20000000},
    {'name':'Jaipur', 'population':4000000},
    {'name':'Shillong', 'population':500000},
    {'name':'Chennai', 'population':11000000}
]

regions = [
    {'name':'Rajasthan', 'rainfall':60},
    {'name':'Meghalaya', 'rainfall':250},
    {'name':'Assam', 'rainfall':180},
    {'name':'Western Ghats', 'rainfall':152},
    {'name':'Ladakh', 'rainfall':10}
]

mountains = [
    {'name':'Aravalli', 'height':1722},
    {'name':'Kanchenjunga', 'height':8586},
    {'name':'Nilgiri', 'height':2637},
    {'name':'Everest', 'height':8849}
]


total_population = 0
total_rainfall = 0
total_height = 0

for city in cities:
  total_population += city['population']
for region in regions:
  total_rainfall += region['rainfall']
for mountain in mountains:
  total_height += mountain['height']



print('Geographic Summation Analysis')
print('---------------------------------')
print('Total population:',total_population)
print('Total rainfall:',total_rainfall)
print('Total height:',total_height)
