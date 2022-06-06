import json
#1.
with open(r"tokens/kakao_code.json","r") as fp:
    ts = json.load(fp)

print(ts)
print(ts["access_token"])