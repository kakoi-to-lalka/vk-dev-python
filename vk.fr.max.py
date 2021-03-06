import requests
import json
import time

f=open('token.txt','r')
token=f.read()
f.close()

def get_name_by_id(id):
    """ получить имя друга по идентификатору """
    url = 'https://api.vk.com/method/users.get'
    params = {'user_ids':id, 'v':'5.52', 'access_token':token}
    r=requests.get(url, params)
    j = json.loads(r.content)
    first_name = j['response'][0]['first_name']
    last_name = j['response'][0]['last_name']
    return first_name + ' ' +last_name

params = {'v' : '5.52', 'access_token': token,'count':10, 'order':'hints'}
r=requests.get('https://api.vk.com/method/friends.get', params=params)
friends = json.loads(r.content)

max_count = 0
max_user_id = ''
for friend in friends['response']['items']:
    params = {'user_id': friend,'v' : '5.52', 'access_token': token}
    r=requests.get('https://api.vk.com/method/friends.get', params=params)
    friends = json.loads(r.content)
    count = friends['response']['count']
    if count > max_count:
        max_count = count
        max_user_id = friend
    print('.',end='')
    time.sleep(1)
print()
print(max_user_id, get_name_by_id(max_user_id), max_count)
