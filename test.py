import json

from fastapi.testclient import TestClient
from app import app
from random import randrange

from Services import *

client = TestClient(app)


def test_add_prescription():
    for i in range(100):
        clinic_id = randrange(333)
        physician_id = randrange(333)
        patient_id = randrange(333)

        response = client.post('http://127.0.0.1:8000/prescriptions',
                           '{{"clinic": {{"id": {0} }},"physician": {{"id": {1} }}, "patient": {{"id": {2} }},"text": "Dipirona 1x ao dia"}}'.format(clinic_id,physician_id,patient_id))

        assert response.status_code == 200
        assert response_types(response.json())



def response_types(response):
    dic_erro02 = json.loads('{"error": {"message": "physician not found", "code": "02"}}')
    dic_erro03 = json.loads('{"error": {"message": "patient not found", "code": "03"}}')
    dic_erro04 = json.loads('{"error": {"message": "metrics service not available", "code": "04"}}')
    dic_erro05 = json.loads('{"error": {"message": "patient not found", "code": "05"}}')
    dic_erro06 = json.loads('{"error": {"message": "metrics service not available", "code": "06"}}')
    if response == dic_erro02 or response == dic_erro03 or response == dic_erro04 or response == dic_erro05 or response == dic_erro06:
        return True
    try:
        response['data']['id']
        response['data']['physician']['id']
        response['data']['patient']['id']
        response['data']['text']
        response['data']['metric']['id']
        return True
    except KeyError:
        return False



if __name__ == '__main__':
    test_add_prescription()