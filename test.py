#from urllib3.exceptions import ProtocolError
import requests

sdata = {"sensid": 123}
r = requests.post("https://citizensensing.itn.liu.se/cs/setsdata", json = sdata)
print(r.status_code, r.reason)

