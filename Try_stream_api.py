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

# Create a streaming sesion
TDStreamingClient = TDSession.create_streaming_session()

print(TDStreamingClient)

# Level One Quote

