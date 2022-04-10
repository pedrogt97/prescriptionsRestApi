from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.testclient import TestClient
from Services import *
import uvicorn

app = FastAPI()


class Clinic(BaseModel):
    id: int


class Physician(BaseModel):
    id: int


class Patient(BaseModel):
    id: int

class Metric(BaseModel):
    id: int


def _find_next_id():
    try:
        return max(prescription.id for prescription in prescriptions) + 1
    except ValueError:
        return 1

class Prescription(BaseModel):
    id: int = Field(default_factory=_find_next_id)
    clinic: Clinic
    physician: Physician
    patient: Patient
    text: str

prescriptions = [
]

client = TestClient(app)


@app.post("/prescriptions", status_code=201)
async def add_prescription(prescription: Prescription):

    clinic = ClinicsService(prescription.clinic.id).valida()
    if clinic is False:
        prescription.clinic.id = None


    physician = PhysiciansService(prescription.physician.id).valida()
    try:
        physician['id']
    except KeyError:
        return physician

    patient = PatientsService(prescription.patient.id).valida()
    try:
        patient['id']
    except KeyError:
        return patient

    prescriptions.append(prescription)

    metricsDic = {
                'clinic_id': None if clinic is False else clinic['id'],
                'clinic_name': None if clinic is False else clinic['name'],
                'physician_id': physician['id'],
                'physician_name': physician['name'],
                'physician_crm': physician['crm'],
                'patient_id': patient['id'],
                'patient_name': patient['name'],
                'patient_email': patient['email'],
                'patient_phone': patient['phone'],
                'prescription_id': max(prescription.id for prescription in prescriptions)
               }

    metrics = MetricsService().valida(metricsDic)
    try:
        metrics['id']
    except KeyError:
        prescriptions.pop()
        return metrics

    dicAux = dict(prescription)
    dicAux['metric'] = { 'id' : metrics['id']}

    ret = {'data': dicAux}

    return ret


if __name__ == '__main__':
    uvicorn.run(app)