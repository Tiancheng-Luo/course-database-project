from django.shortcuts import render
from .models import Course
from django.db.models import Q
from django.contrib.auth.models import User
from .filters import UserFilter
#he
# Create your views here.
def search(request):

    course_list = Course.objects.all()
    user_filter = UserFilter(request.GET, queryset=course_list)
    return render(request,'searchBar.html', {'filter': user_filter, 'class_list': Course.objects.all()})

def class_page(request, class_name):
    course = Course.objects.filter(title=class_name)[0]
    return render(request, 'classPage.html', {'course': course})

def search_results(request):
    query = request.POST.get("query", "")
    class_list = retrieveObjects(request)
    return render(request, 'searchResults.html', {'query': query, 'class_list': class_list})

def retrieveObjects(request):
    query = request.POST.get("query", "")
    entries = Course.objects.filter(
        Q(title__icontains= query) |
        Q(instructor__icontains= query) |
        Q(description__icontains=query)
    ).distinct()

    return entries


def login(request):
    return render(request, 'LoginTest.html')