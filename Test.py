import requests

url = 'http://bbnmout3lik.cf:80'
headers = {'content-type' : 'application/json'}
r = requests.post(url, data={'name':"tayebdz",'submit':'submit'})

if('success' in r.text):
  print('==<successfuly added>==')
