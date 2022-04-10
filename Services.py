import requests
from enum import Enum

import urllib3.exceptions

class Services:
    def __init__(self):
        self.host = 'https://mock-api-challenge.dev.iclinic.com.br'

class PhysiciansService(Services):
    def __init__(self, id):
        super().__init__()
        self.path = '/physicians/' + str(id) + '/'
        self.auth = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJzZXJ2aWNlIjoicGh5c2ljaWFucyJ9.Ei58MtFFGBK4uzpxwnzLxG0Ljdd-NQKVcOXIS4UYJtA'
        self.endpoint = self.host + self.path

    def valida(self):
        try:
            resposta = requests.get(self.endpoint, headers={"Authorization": self.auth}, verify=False)
            if resposta.status_code == 404:
                return {'error': {'message': 'physician not found', 'code': '02'}}
            return resposta.json()
        except (urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError) as err:
            return {'error': {'message': 'physicians service not available', 'code': '05'}}



class ClinicsService(Services):
    def __init__(self, id):
        super().__init__()
        self.path = '/clinics/' + str(id) + '/'
        self.auth = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJzZXJ2aWNlIjoiY2xpbmljcyJ9.r3w8KS4LfkKqZhOUK8YnIdLhVGJEqnReSClLCMBIJRQ'
        self.endpoint = self.host + self.path

    def valida(self):
        try:
            resposta = requests.get(self.endpoint, headers={"Authorization": self.auth}, verify=False)
            if resposta.status_code == 404:
                return False
            return resposta.json()
        except (urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError, requests.exceptions.SSLError) as err:
            return False


class PatientsService(Services):
    def __init__(self, id):
        super().__init__()
        self.path = '/patients/' + str(id) + '/'
        self.auth = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJzZXJ2aWNlIjoicGF0aWVudHMifQ.Pr6Z58GzNRtjX8Y09hEBzl7dluxsGiaxGlfzdaphzVU'
        self.endpoint = self.host + self.path

    def valida(self):
        try:
            resposta = requests.get(self.endpoint, headers={"Authorization": self.auth}, verify=False)
            if resposta.status_code == 404:
                return {'error': {'message': 'patient not found', 'code': '03'}}
            return resposta.json()
        except (urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError) as err:
            return {'error': {'message': 'patients service not available', 'code': '06'}}

class MetricsService(Services):
    def __init__(self):
        super().__init__()
        self.path = '/metrics/'
        self.auth = 'Bearer SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
        self.timeout = 6
        self.retry = 5
        self.endpoint = self.host + self.path

    def valida(self, metricsDic):
        try:
            resposta = requests.post(self.endpoint, headers={"Authorization": self.auth}, data=metricsDic, verify=False)
            return resposta.json()
        except (urllib3.exceptions.MaxRetryError, urllib3.exceptions.TimeoutError) as err:
            return {'error': {'message': 'metrics service not available', 'code': '04'}}


