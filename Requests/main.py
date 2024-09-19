import requests

g = requests.get('http://httpbin.org/get')
# print(g)

p = requests.post('http://httpbin.org/post')
# print(p)

pu = requests.put('http://httpbin.org/put')
# print(pu)

d = requests.delete('http://httpbin.org/delete')
# print(d)

r = requests.get('http://httpbin.org/get', params={"kategori":"elektronik","marka":"samsung"})
print(r.url)