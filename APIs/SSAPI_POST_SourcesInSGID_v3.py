# PYTHON para cargar Twitter Sources en un Source group via SS API
# VERSION ESTABLE 3
# python SSAPI_POST_SourcesInSGID_v3.py

import csv
import time
import requests
import pprint
import json
import pandas as pd
from pathlib import Path
from datetime import datetime

clientInfo = {'client_id': 'mcxxf5f12fb3f8be492aaf5aa85b12931173',
              'client_secret': '5c2842f0a1f8461bac670b72882fe916'}

userInfo = {'username': 'SysAdmin.MC@prosumia.la',
            'password': '!)12)!98QWEazsx'}

auth_URL = 'https://api.socialstudio.radian6.com/oauth/token'
sourceGroudId = 182588
now = datetime.now()
logFile = Path.cwd() / 'API_Logs' / ('LOG_'+str(sourceGroudId) +
                                     '_'+now.strftime('%d%m%Y_%H_%M_%S')+'.csv')
logFieldNames = ["row", "statusCode", "ReqResponseDescription", "title", "uri"]
rowCount = 0
refreshCounter = 0
responseStatusCode = 0
responseDescription = ''
sourceTitle = ''
sourceUri = ''

# METHODS


def getAccessToken(authClient, authUser, authURL):
    authData1 = {}
    key1 = ''
    grantType1 = {'grant_type': 'password'}
    authData1 = {**grantType1, **authClient, **authUser}
    try:
        r1 = requests.post(authURL, data=authData1, timeout=3)
        responseStatusCode = r1.status_code
        responseDescription = r1.text
        r1.raise_for_status()
    except requests.exceptions.RequestException as err1:  # catches any EXCEPTION
        responseStatusCode = err1.response.status_code
        responseDescription = err1.text
        raise SystemExit(err1)
    load1 = json.loads(r1.content)
    key1 = load1['access_token']
    refreshToken1 = load1['refresh_token']
    return load1, key1, refreshToken1


def refreshAccessToken(authClient, authRefreshToken, authURL, refreshCounter2):
    refreshCounter2 += 1
    authData2 = {}
    key2 = ''
    grantType2 = {'grant_type': 'refresh_token'}
    refresh_token2 = {'refresh_token': authRefreshToken}
    authData2 = {**grantType2, **authClient, **refresh_token2}
    try:
        r2 = requests.post(authURL, data=authData2, timeout=3)
        r2.raise_for_status()
    except requests.exceptions.RequestException as err2:  # catches any EXCEPTION
        errResponseStatusCode = err2.response.status_code
        raise SystemExit(err2)
    load2 = json.loads(r2.content)
    key2 = load2['access_token']
    refreshToken2 = load2['refresh_token']
    return load2, key2, refreshToken2, refreshCounter2


def endInfo(counter, refreshCounter, sourceGroudId, localInitTime, localEndTime, key, refreshToken):
    print("Finally finished loading = ", counter,
          " sources in SG ID =", sourceGroudId)
    print("Number of Refreshed Access Tokens = ", refreshCounter)
    print("End Time = ", time.ctime(localEndTime))
    print("Job Duration = ", localEndTime-localInitTime, " seconds")
    print("Last Access Token = ", key)
    print("Last Refresh Token = ", refreshToken)


def openLogCSV(log_File, log_FieldNames):
    # Abre el archivo de salida y genera los headers de campos
    with open(log_File, 'w', newline='\n') as log_Object:
        dictwriter_Object = csv.DictWriter(
            log_Object, fieldnames=log_FieldNames)
        dictwriter_Object.writeheader()   # genera los nombres de columna
        log_Object.close()


def addLogRow(log_File, log_FieldNames, row_Count, status_Code, response_Description, body_title, body_uri):
    new_row = {"row": row_Count, "statusCode": status_Code,
               "ReqResponseDescription": response_Description, "title": body_title, "uri": body_uri}
    with open(log_File, 'a', newline='\n') as log_Object:
        dictwriter_Object = csv.DictWriter(
            log_Object, fieldnames=log_FieldNames)
        dictwriter_Object.writerow(new_row)
        log_Object.close()


def main():
    rowCount = 0
    refreshCounter = 0
    # ----------CREATE LOG FILE AND COLUMN HEADERS-------------
    openLogCSV(logFile, logFieldNames)

    # ----------GET ACCESS TOKEN-------------
    load, key, refreshToken = getAccessToken(clientInfo, userInfo, auth_URL)

    # ----------Start Timer and Init Job Local Time-------------
    startTimer = time.time()
    localInitTime = startTimer
    print(time.ctime(localInitTime))

    # ----------DECLARE VARIABLES FOR REQUEST HEADER AND URL-------------
    url2 = 'https://api.socialstudio.radian6.com/v3/sourceFilters/' + \
        str(sourceGroudId)+'/sourceFilterQueries'

    # ---------GET REQUIRED DATA FROM CSV --------------------------------
    # CSV must have 2 cloumns with headers "title" and "uri"
    #infileName = sys.argv[1]
    infileName = 'UCR_PBA_Twitter_SG_40'
    input_file = '/Users/juancarloskleylein/Library/Mobile Documents/com~apple~CloudDocs/VSCodePython/CSV_JSON_IN/' + \
        infileName+".csv"  # name of csv file without the .csv

    # ----------Uso Pandas para convertir el CSV en un PANDAS DATAFRAME < class 'pandas.core.frame.DataFrame' >
    df_csv = pd.read_csv(input_file)
    df_rowsNumber = len(df_csv.index)
    print("Number of Rows = ", df_rowsNumber)
    pprint.pprint(df_csv.head(10))

    # ---------EXECUTE POST df_rowsNumber TIMES--------------------------------
    while rowCount < df_rowsNumber:
        sourceTitle = df_csv.at[rowCount, 'title']
        sourceUri = df_csv.at[rowCount, 'uri']
        # converts Python DICT to JSON object for the request
        payLoad = json.dumps({"title": sourceTitle, "uri": sourceUri})
        print(payLoad)
    # --------- EXECUTE REQUEST WITH ERROR HANDLING----------------------------
        try:
            headers = {"access_token": key,
                       "Content-Type": 'application/json', "charset'": 'utf-8'}
            print("Access Token = ", key)
            resp = requests.post(url2, headers=headers,
                                 data=payLoad, timeout=100)
            resp.raise_for_status()
            responseStatusCode = resp.status_code
            responseDescription = resp.text
            addLogRow(logFile, logFieldNames, rowCount, responseStatusCode,
                      responseDescription, sourceTitle, sourceUri)
            rowCount += 1
        except requests.exceptions.RequestException as err:  # catches any EXCEPTION
            responseStatusCode = err.response.status_code
            responseDescription = err.response.text
            if responseStatusCode != 401:
                localEndTime = time.time()
                endInfo(rowCount, refreshCounter, sourceGroudId,
                        localInitTime, localEndTime, key, refreshToken)
                raise SystemExit(err)
            else:
                addLogRow(logFile, logFieldNames, rowCount, responseStatusCode,
                          responseDescription, sourceTitle, sourceUri)
                print("------------------------------------------------------")
                print("ERROR Status Code = ", responseStatusCode)
                print("ERROR Body = ", responseDescription)
                print("Number Of ROWS executed = ", rowCount)
                print("------------------------------------------------------")
                load, key, refreshToken, refreshCounter = refreshAccessToken(
                    clientInfo, refreshToken, auth_URL, refreshCounter)
        # time.sleep(100)
    else:
        localEndTime = time.time()
        print("---------------------------Success End!------------------------------")
        endInfo(rowCount, refreshCounter, sourceGroudId,
                localInitTime, localEndTime, key, refreshToken)


if __name__ == '__main__':
    main()
