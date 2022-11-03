from datetime import datetime, timedelta


def rangeDate(request, hours: int = None, days: int = None, weeks: int = None):
    startDate = request.GET.get("start")
    endDate = request.GET.get("end")

    date_to = date_from = None
    if startDate and endDate:
        date_from = datetime.strptime(startDate, "%Y-%m-%d")
        date_to = datetime.strptime(endDate, "%Y-%m-%d")
    if startDate and not endDate:
        date_from = datetime.strptime(startDate, "%Y-%m-%d")
        date_to = datetime.now()
    if date_to and date_from:
        return date_from, date_to

    if hours:
        date_from = datetime.now() - timedelta(hours=hours)
    elif days:
        date_from = datetime.now() - timedelta(days=days)
    elif weeks:
        date_from = datetime.now() - timedelta(weeks=weeks)
    date_to = datetime.now()
    return date_from, date_to
