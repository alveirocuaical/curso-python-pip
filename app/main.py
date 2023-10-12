import mod
import utils
import read_csv
import charts
'''
data = [{
    'Country': 'Colombia',
    'Population': 3939
}, {
    'Country': 'Bolivia',
    'Population': 2233
}]

'''


def run():

  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda region : region['Continent'] == 'South America', data))
  countries = list(map(lambda x : x['Country/Territory'], data))
  percentages = list(map(lambda x : x['World Population Percentage'], data))
  
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type counrtry  => ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_char(labels, values, country['Country/Territory']) 
  



#se gestiona la dualidad para que el archivo funcione como script y como
# modulo.

if __name__ == '__main__':
  run()
