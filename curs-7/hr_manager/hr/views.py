from django.shortcuts import render
from .models import Employer


def homepage(request):
    print('111111111111', request)

    all_employers_qs = Employer.objects.all()
    return render(request, 'homepage.html', {
        'framework_name': 'Django',
        'employers': all_employers_qs
    })
