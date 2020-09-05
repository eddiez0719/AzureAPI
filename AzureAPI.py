import requests, json
clientId = "8d4538e6-b1a5-4c05-b449-54d62fb18413"
tenantName = "vetpartners.com.au"
clientSecret = ".2S_z50qp.BVff~~5J_9_cxM1e1TRXrJ94"
resource = "https://graph.microsoft.com/"
username = 'xezhang@vet.partners'
password = '3351976Zy'

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


