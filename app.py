import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

import logging

# Initialise Logger
logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{')
logger = logging.getLogger("GOOGLESHEETSDB")

try:
    # Connect to Google Sheets
    logger.info("Connecting to Google Sheets...")

    scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("certificates/google_sheets_credentials.json", scope)
    client = gspread.authorize(credentials)

    logger.info("Connected to Google Sheets")

except Exception as error:
    logger.error(f"{error}")