import django
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from utilities_view import get_duration, format_duration


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
        duration = get_duration(visit)
        non_closed_visit = {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at.strftime('%Y-%m-%d %H:%M'),
                'duration': format_duration(duration),
        }

        non_closed_visits.append(non_closed_visit)

    context = {
            'non_closed_visits': non_closed_visits
    }

    return render(request, 'storage_information.html', context)




