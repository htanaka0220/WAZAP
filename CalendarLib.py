from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
#日付周りのインポート
import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
class Calendar():
    def get_schedule():
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        #service = build('calendar', 'v3', http=creds.authorize(Http()))
        
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        return events 

    def schedule_today():
        
        tmp_list = []
        
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            if(str(start[0:10]) == str(now[0:10])):
                tmp_list.append(event['summary'])
        if tmp_list:
            for event in tmp_list:
                print(event)
                os.system("./jtalk.sh " + "\"" + event + "\"")
        else:
            os.system("./jtalk.sh " + "\"今日の予定は未定です\"")

        