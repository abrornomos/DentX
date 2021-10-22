from datetime import timedelta
from dentist.models import Service_translation


def compare_time(datetime, appointments):
    for appointment in appointments:
        if datetime - appointment.begin >= timedelta() and appointment.end - datetime > timedelta():
            return False
    return True


def compare_appointment(new_appointment, appointments):
    for appointment in appointments:
        if new_appointment.begin - appointment.begin >= timedelta():
            if not new_appointment.begin - appointment.end >= timedelta():
                return False
        elif not appointment.begin - new_appointment.end >= timedelta():
            return False
    return True


def get_services(services, language_id):
    results = []
    for service in services:
        results.append({
            'service': service,
            'service_name': Service_translation.objects.filter(
                service=service,
                language__pk=language_id
            )[0]
        })
    return results
