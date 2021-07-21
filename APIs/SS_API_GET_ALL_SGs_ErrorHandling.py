
import sys
import requests
import pprint 
import json
import pandas as pd

data = {'grant_type': 'password', 
        'client_id': 'mcxxf5f12fb3f8be492aaf5aa85b12931173', 
        'client_secret': '5c2842f0a1f8461bac670b72882fe916', 
        'username': 'juan.kleylein@prosumia.la', 
        'password': '!!!123)))987QWEazsx!)'}

url1='https://api.socialstudio.radian6.com/oauth/token'
try:
    r = requests.post(url1,data=data,timeout=3)
    r.raise_for_status()
except requests.exceptions.RequestException as err:   #catches any EXCEPTION
    errResponseBody =err.response.text
    errResponseStatusCode = err.response.status_code
    #print ("ERROR Status Code = " , errResponseStatusCode)
    #print ("ERROR Body = " , errResponseBody)
    #print("------------------------------------------------------")
    errschema = r.__dict__
    errkeys = errschema.keys()
    errvalues = errschema.values()
    #print("err keys = ", errschema.keys())
    #print("------------------------------------------------------")
    #print("err values = ", errschema.values())
    #print("------------------------------------------------------")
    raise SystemExit(err)
# else:
    print("Cualquiera")
# finally:
    print("esto se ejecuta siempre")

#print(r)
#eqResponseBody =r.text
#reqResponseStatusCode = r.status_code
#print ("Status Code = " , reqResponseStatusCode)
#print ("Body = " , reqResponseBody

load = json.loads(r.content)
key = load['access_token']
refreshToken = load['refresh_token']
# pprint.pprint(load)

# ------------------GET ALL SOURCE GROUPS LIST FROM SS API ----------------------
# DECLARE VARIABLES FOR REQUEST URL = get ALL SOURCE GROUPS
headers = {"access_token": key}
url2 = 'https://api.socialstudio.radian6.com/v3/sourceFilters'

# EXECUTE REQUEST WITH ERROR HANDLING
try:
    resp = requests.get(url2, headers=headers, timeout=100)
    resp.raise_for_status()
except requests.exceptions.RequestException as err:   #catches any EXCEPTION
    errResponseBody =err.response.text
    errResponseStatusCode = err.response.status_code
    #print ("ERROR Status Code = " , errResponseStatusCode)
    #print ("ERROR Body = " , errResponseBody)
    #print("------------------------------------------------------")
    errschema = r.__dict__
    errkeys = errschema.keys()
    errvalues = errschema.values()
    #print("err keys = ", errschema.keys())
    #print("------------------------------------------------------")
    #print("err values = ", errschema.values())
    #print("------------------------------------------------------")
    raise SystemExit(err)


jsonResponseBody = json.loads(resp.content)
print ("jsonResponseBody Type =", type(jsonResponseBody))

# view Object Keys
jsonResponseBodyKeys = jsonResponseBody.keys()
print("jsonResponseBody Keys =" , jsonResponseBody.keys())       # 'data' and 'meta'

dataListOfDicts = jsonResponseBody ['data']  # 'data' is a key in the jsonResponseBody

# using pandas dataframe to create a table from a LIST of DICTS
df = pd.DataFrame.from_records(dataListOfDicts, columns=['id', 'title'])
print(df)
