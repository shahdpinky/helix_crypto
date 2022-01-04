import time
import hmac
from requests import Request

ts = int(time.time() * 1000)
request = Request('GET', '<api_endpoint>')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new('YOUR_API_SECRET'.encode(), signature_payload, 'sha256').hexdigest()

request.headers['FTX-KEY'] = 'YOUR_API_KEY'
request.headers['FTX-SIGN'] = signature
request.headers['FTX-TS'] = str(ts)