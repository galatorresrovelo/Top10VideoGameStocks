def get_specific_data (company_year_dict):
  company_year_data = {
      'January': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '01')[0]),2),
      'February': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '02')[0]),2),
      'March': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '03')[0]),2),
      'April': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '04')[0]),2),
      'May': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '05')[0]),2),
      'June': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '06')[0]),2),
      'July': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '07')[0]),2),
      'August': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '08')[0]),2),
      'September': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '09')[0]),2),
      'October': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '10')[0]),2),
      'November': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '11')[0]),2),
      'December': round(float(list(item['Adj Close'] for item in company_year_dict if item['Date'][5:7] == '12')[0]),2),
  }
  labels = company_year_data.keys()
  values = company_year_data.values()
  return labels, values

def close_by_company_year(company, year, data):
  result =list(filter(lambda 
  item:item['Ticker Symbol']==company and item['Date'][0:4]==year, data))
  return result