import django


def get_duration(visit):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at
        seconds = int(delta.total_seconds())
        return seconds
    else:
        delta = django.utils.timezone.localtime() - visit.entered_at
        seconds = int(delta.total_seconds())
        return seconds


def format_duration(seconds):
    default_hour = 3600
    default_minutes = 60
    hours = seconds // default_hour
    minutes = (seconds % default_hour) // default_minutes
    return f'{hours}ч {minutes:02d}мин'


def is_visit_long(visit, minutes=60):
    seconds = get_duration(visit)
    total_minutes = seconds // minutes

    return total_minutes > minutes
