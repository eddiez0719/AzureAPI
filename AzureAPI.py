import requests, json
clientId = "8xxxx-bxxxx-xc32-12xx4d"
tenantName = "vetpartners.com.au"
clientSecret = "abcde"
resource = "https://graph.microsoft.com/"
username = 'xyz@domain.com'
password = 'password'

req_token_body = {'Grant_Type': 'Password',
                  'Client_Id': clientId,
                  'Client_Secret': clientSecret,
                   'Username': username,
                   'Password': password,
                   'Scope': 'https://graph.microsoft.com/.default'
                  }
r = requests.post('https://login.microsoftonline.com/vetpartners.com.au/oauth2/v2.0/token', data=req_token_body)

token = json.loads(r.text)
token_json = r.json()

# print(r)
# print(token['access_token'])

g = requests.get('https://graph.microsoft.com/v1.0/security/alerts', headers={'Authorization': token['access_token']})
gg = json.loads(g.text)
#print(gg)
print(gg['value'])
for i in gg['value']:
    print('User: {} \nAlert: {} \nDescription: {} \nfrom: {} \non: {} \nSeverity: {} \n'.format(i['userStates'][0]['accountName'], i['title'], i['description'], i['userStates'][0]['logonIp'], i['eventDateTime'], i['severity']))


