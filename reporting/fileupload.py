import os
import pandas as pd
from google.cloud import storage
import datetime
from dbt_test_report import df

from google.cloud import storage
# The private JSON key of the service account
# path_to_private_key = './gcs-project-354207-099ef6796af6.json'
# client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)

#Set the JSON Key as Env Variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\WF941RK\OneDrive - EY\Documents\GitHub\dbt_gcp\creds.json"

storage_client = storage.Client()
print(storage_client)

# bucket = storage_client.create_bucket('dbt-runresults')
# print(f'Bucket with name [{bucket.name}] created on GCS!')

def create_bucket(bucket_name):
    """Creates a bucket in GCP if it does not already exist."""
    bucket = storage_client.bucket(bucket_name)
    if not bucket.exists():
        print(f'Bucket with name [{bucket_name}] not exist on GCS!')
        bucket.create()
    else:
        print(f'Bucket with name [{bucket_name}] already exist on GCS!')

def upload_dataframe(bucket_name, dataframe, file_name):
    """Uploads a Pandas DataFrame to a bucket in GCP."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(dataframe.to_csv(index=False))

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%p")
if __name__ == "__main__":
    bucket_name = "dbt-runresults"
    dataframe = df
    file_name = f"run_results_{timestamp}.csv"
    create_bucket(bucket_name)
    upload_dataframe(bucket_name, dataframe, file_name)