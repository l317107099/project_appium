from daili.dailis import Ip
import requests

ip = Ip()
ipdaile = ip.run()
# print(ipdaile)
lists = []
for dail in ipdaile:
    proiex = {}
    proiex["http"]='http://{ip}:{port}'.format(ip=dail[0],port=dail[1])
    proiex["https"]="http://{}:{}".format(dail[0],dail[1])
    lists.append(proiex)
url = 'https://chs.meituan.com/meishi/'
ke_list = []
for list in lists:
    try:
        response = requests.get(url, proxies=list)
    except Exception as e :
        print(e)
    else:
        if  response.status_code in [200,201]:
                ke_list.append(list)

print(ke_list)
