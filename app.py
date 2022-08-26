import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

import logging

# Initialise Logger
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("GOOGLESHEETSDB")

try:
    # Connect to Google Sheets
    logger.info("Connecting to Google Sheets")

    scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("certificates/google_sheets_credentials.json", scope)
    client = gspread.authorize(credentials)

    logger.info("Create sheet")
    sheet = client.create("NewDatabase")
    logger.info("Share with me")
    sheet.share('felidaesrule@gmail.com', perm_type='user', role='writer')

    logger.info("Open sheet")
    sheet = client.open("NewDatabase").sheet1

    logger.info("Read local CSV into Pandas")
    df = pd.read_csv('sheets/football_news.csv')

    logger.info("Updating new sheet with data from local file")
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

    logger.info("Completed")

except Exception as error:
    logger.error(f"{error}")