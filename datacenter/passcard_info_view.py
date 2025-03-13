from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.utilities_view import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in all_visits:
        duration = get_duration(visit)
        is_strange = is_visit_long(visit)
        this_passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_strange
        }

        this_passcard_visits.append(this_passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
