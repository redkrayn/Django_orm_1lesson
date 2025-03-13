import django
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def get_duration(visit):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at

        seconds = delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return hours, minutes
    else:
        delta = django.utils.timezone.localtime() - visit.entered_at

        seconds = delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return hours, minutes


def format_duration(duration):
    hours, minutes = duration
    return f'{hours}ч : {minutes}мин'


def is_visit_long(visit, moment=60):
    hours, minutes = get_duration(visit)
    total_minutes = hours * 60 + minutes
    if total_minutes < moment:
        return False
    else:
        return True  # Если не добавить True, будет показывать None


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in all_visits:
        is_strange = is_visit_long(visit)
        this_passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_strange
        }

        this_passcard_visits.append(this_passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
