from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()
credentials_dict = {
    'type': 'service_account',
    'client_id': os.getenv("client_id"),
    'client_email': os.getenv("client_email"),
    'private_key_id': os.getenv("private_key_id"),
    'private_key': os.getenv("private_key"),
}
credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    credentials_dict
)
client = storage.Client(credentials=credentials, project='ey-poc')
bucket = client.get_bucket('ey-poc')
blob = bucket.blob(r'C:\Users\WF941RK\OneDrive - EY\Documents\GitHub\dbt_gcp\reporting\dbt_test\run_results_2023-06-30_02-17-PM.csv')
blob.upload_from_filename(r'C:\Users\WF941RK\OneDrive - EY\Documents\GitHub\dbt_gcp\reporting\dbt_test\run_results_2023-06-30_02-17-PM.csv')