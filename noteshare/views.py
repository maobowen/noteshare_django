from django.shortcuts import render, get_object_or_404
from noteshare.models import *

# Create your views here.
COLOR_SCHEME = ['rosered', 'lightorange', 'darkyellow', 'mudyellow', 'grassgreen', 'darkgreen', 'bluegreen', 'greyblue',
                'darkblue', 'darkpurple']


def index(request):
    return render(request, 'noteshare/index.html', context={
        'page_title': 'Home | ',
        'universities': University.objects.all(),
    })


def university(request, university_id):
    university = get_object_or_404(University, id=university_id.lower())
    try:
        courses = Course.objects.filter(university=university_id.lower())
        courses2 = {}
        i = 0
        for c in courses:
            courses2[c] = COLOR_SCHEME[i % len(COLOR_SCHEME)]
            i += 1
        subjects = Course.objects.filter(university=university_id.lower()).values_list('subject', flat=True).distinct().order_by()
    except Course.DoesNotExist:
        pass
    return render(request, 'noteshare/university.html', context={
        'page_title': university.name + ' | ',
        'universities': University.objects.all(),
        'university_name': university.name,
        'university_country': university.country.name,
        'subjects': subjects,
        'courses': courses2,
    })


def course(request, university_id, course_id):
    course = get_object_or_404(Course, id=course_id.lower(), university=university_id.lower())
    with open('noteshare/' + course.university.id + '/' + course.id + '.html', 'r') as f:
        content = f.read()
    return render(request, 'noteshare/course.html', context={
        'page_title': course.number + ' | ' + course.university.name + ' | ',
        'universities': University.objects.all(),
        'course_number': course.number,
        'course_name': course.name,
        'university_id': course.university.id,
        'university_name': course.university.name,
        'content': content
    })
