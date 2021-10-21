from django.contrib.auth.models import User
from dentist.models import User as DentistUser
from patient.models import User as PatientUser

def get_queries(queries):
    results = []
    for query in queries:
        dentist_extra = DentistUser.objects.get(pk=query.dentist_id)
        patient_extra = PatientUser.objects.get(pk=query.patient_id)
        results.append({
            'dentist': User.objects.get(pk=dentist_extra.user_id),
            'dentist_extra': dentist_extra,
            'patient': User.objects.get(pk=patient_extra.user_id),
            'patient_extra': patient_extra,
            'query': query
        })
    return results
