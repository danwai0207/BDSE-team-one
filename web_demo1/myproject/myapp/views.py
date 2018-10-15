from django.shortcuts import render_to_response
from .models import Futures


# Create your views here.
def index(request):
    table = Futures.objects.all()
    date = []
    open = []
    high = []
    low = []
    close = []
    for row in table:
        date += [row.date.isoformat()]
        open += [row.open]
        high += [row.high]
        low += [row.low]
        close += [row.close]

    return render_to_response("index.html", locals())
