import requests

# requests.get(url, params=None, headers=None, cookies=None, auth=None, timeout=None)
"""
url (zorunlu): İstek gönderilecek adres.
params (isteğe bağlı): Gönderilen isteği özelleştirebilecek ifadeler.
headers (isteğe bağlı): İsteğin nasıl yorumlanacağına dair sunucuya bilgi veren ifadeler.
cookies (isteğe bağlı): İstemciye ait oturum (session) bilgilerini saklayan ifadeler.
auth (isteğe bağlı): İstemciye ait kimlik bilgileri.
timeout (isteğe bağlı): Gönderilen isteğin yanıtı için beklenecek saniye cinsinden süre.
"""

istek = requests.get("https://api.github.com")
# print(istek)

headers = {
 
"user-agent": "ravenfo",
'Content-Type': 'application/json'
 
}
 
istek = requests.get("https://api.github.com", headers = headers)
# print(istek)


parameters = {
 
"market": "TR",
"ids": "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"
 
}
 
tr_song = requests.get("https://api.spotify.com/v1/tracks", params = parameters)
# print(tr_song)

#Yandex
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
# requests.get(url, params = {key=API_KEY})
 
#Zendesk
url = "https://your_subdomain.zendesk.com/api/v2/groups.json"
requests.get(url, auth=("username", "password"))


from requests.exceptions import Timeout
 
try:
    istek = requests.get('https://api.github.com', timeout=0.0001)
except Timeout:
    print('Zaman aşımı!')
else:
    print('Her şey yolunda!')