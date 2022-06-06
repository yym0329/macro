import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '64b81b1ad78f5d964b0e84557a4804b1'
redirect_uri = 'https://www.naver.com/'
authorize_code = 'WPNcSMCVpl15bWLLYnWhIaCTEfveVQBeElBHqVIaYEX2SGe_LNcZTSslJLq8Ya15ELmEjgopcFEAAAGBOHf-FQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"tokens\kakao_code.json","w") as fp:
    json.dump(tokens, fp)
