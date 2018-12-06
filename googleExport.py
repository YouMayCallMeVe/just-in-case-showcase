from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
def getValues():
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1eUE-Zzq5PpBWvYEQvWmllrBM3MWwPcXq4t7ZP4LttJo'
    SAMPLE_RANGE_NAME = 'Current_Sprint!B:D'
    retVal = []
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            retVal.append((row[0],row[-1]))
    return retVal
