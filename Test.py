import requests

url = 'http://bbnmout3lik.cc/index.php'

r = requests.post(url, data={'name':"tayebdz",'submit':'submit'})

if('success' in r.text):
  print('==<successfuly added>==')
