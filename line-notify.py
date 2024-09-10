import requests

def Notify(msg):
    url = 'https://notify-api.line.me/api/notify'
    header = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
    req = requests.post(url, headers=header, data={'message': msg})
    return(req)	

token = 'your line token'
print(Notify('your line message'))
