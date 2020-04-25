# Import the client
from td.client import TDClient
from config import account_number,client_id

# Create a new session, credentials path is optional.
TDSession = TDClient(
    account_number=account_number,
    client_id=client_id,
    redirect_uri='http://localhost/TDtest',
    credentials_path='credentials.json'
)

# Login to the session
TDSession.login()

# Grab real-time quotes for 'MSFT' (Microsoft)
msft_quotes = TDSession.get_quotes(instruments=['TSLA'])

# Grab real-time quotes for 'AMZN' (Amazon) and 'SQ' (Square)
multiple_quotes = TDSession.get_quotes(instruments=['AMZN,SQ'])

multiple_quotes['AMZN']

#print(msft_quotes)
print(multiple_quotes['AMZN'])