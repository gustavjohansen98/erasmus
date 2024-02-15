from os import environ
from typing import Any
from .singleton import Singleton
from firebase_admin import firestore, credentials, storage, initialize_app

class API(metaclass=Singleton):
    def __init__(self):
        if not hasattr(self, 'db') or self.db is None:
            self.__init_from_credentials()
            self.db = firestore.client()
            self.bucket = storage.bucket()

    def __init_from_credentials(self):
        firebase_credentials = credentials.Certificate({
            "type": "service_account",
            "project_id": "transcribe-app-8099d",
            "private_key_id": environ['FIREBASE_PRIVATE_KEY_ID'],
            "private_key": environ['FIREBASE_PRIVATE_KEY'].replace(r'\n', '\n'),
            "client_email": environ['FIREBASE_CLIENT_EMAIL'],
            "client_id": environ['FIREBASE_CLIENT_ID'],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": environ['FIREBASE_CLIENT_X509_CERT_URL']
        })
        initialize_app(
            firebase_credentials,
            {
                'storageBucket': 'transcribe-app-8099d.appspot.com'
            }
        )
            
    
    def upload_file(
        self, 
        file: Any,
    ):
        pass
        # create_time, log_ref = (
        #     self.db
        #     .collection(u'logs')
        #     .add(log_model.dict())
        # )
        # return log_ref.id

