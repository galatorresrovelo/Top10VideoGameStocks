import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app2/data2.csv')
  company = input('Type company => ')
  company= company.upper()
  year = input('Type year => ')
  year = str(year)
  result = utils.close_by_company_year( company, year, data)

  if len(result) > 0:
    company_by_year = result
    labels, values = utils.get_specific_data(company_by_year)
    charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()