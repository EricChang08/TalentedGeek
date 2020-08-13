from django.http import HttpResponseRedirect
from django.shortcuts import render
from garden.models import *
from django.core import serializers
from .forms import *

# Create your views here.

json_serializer = serializers.get_serializer("json")()
edu = json_serializer.serialize(education.objects.all(), ensure_ascii=False)


def index(request):
    return render(request, "garden/Home.html", {
        "hobbies": interest.objects.all(),
        "Education": education.objects.all()
    })


# In the CV page, I display fixed 4 summaries, 6 skills
def cv(request):
    return render(
        request, "garden/CV.html", {
            "summary": summary.objects.all(),
            "skill1": skill.objects.all()[0],
            "skill2": skill.objects.all()[1],
            "skill3": skill.objects.all()[2],
            "skill4": skill.objects.all()[3],
            "skill5": skill.objects.all()[4],
            "skill6": skill.objects.all()[5],
            "project": theProject.objects.all(),
            "education": education.objects.all(),
            "interest": interest.objects.all(),
        })


def cvLog(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = userValidation(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # create a new record and store the new project data into it
            theUser = login.objects.get(pk=1)
            if (form.cleaned_data['user'] == theUser.usr
                    and form.cleaned_data['password'] == theUser.psw):
                return HttpResponseRedirect('/cv/edit?type')

            # redirect to cv Edit page:
            return HttpResponseRedirect('/cv/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = userValidation()

    return render(request, "garden/cvLog.html", {'form': form})


def cvEdit(request):
    # TODO: implement these database operations here

    # FEATURE 1: delete the project
    if (request.GET['type'] == 'proDel'):
        param1 = request.GET['id']

        item = theProject.objects.get(pk=param1)
        item.delete()
        return HttpResponseRedirect('/cv/edit?type')

    # FEATURE 2: delete the education
    elif (request.GET['type'] == 'eduDel'):
        param1 = request.GET['id']

        item = education.objects.get(pk=param1)
        item.delete()
        return HttpResponseRedirect('/cv/edit?type')

    # FEATURE 3: delete the interest
    elif (request.GET['type'] == 'intDel'):
        param1 = request.GET['id']

        item = interest.objects.get(pk=param1)
        item.delete()
        return HttpResponseRedirect('/cv/edit?type')

    else:
        return render(
            request, "garden/cvEdit.html", {
                "summary": summary.objects.all(),
                "skill1": skill.objects.all()[0],
                "skill2": skill.objects.all()[1],
                "skill3": skill.objects.all()[2],
                "skill4": skill.objects.all()[3],
                "skill5": skill.objects.all()[4],
                "skill6": skill.objects.all()[5],
                "project": theProject.objects.all(),
                "education": education.objects.all(),
                "interest": interest.objects.all(),
            })


def proAdd(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addProject(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # create a new record and store the new project data into it
            project = theProject()  #gets new project object
            project.time = form.cleaned_data['time']
            project.title = form.cleaned_data['title']
            project.description = form.cleaned_data['description']
            project.role1 = form.cleaned_data['role1']
            project.role2 = form.cleaned_data['role2']
            #finally save the object in db
            project.save()

            # redirect to cv Edit page:
            return HttpResponseRedirect('/cv/edit?type')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addProject()

    return render(request, "garden/cvInfoAdd/addPro.html", {'form': form})


def intAdd(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addInterest(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # create a new record and store the new project data into it
            inte = interest()  #gets new project object
            inte.title = form.cleaned_data['title']
            inte.description = form.cleaned_data['description']
            inte.language = 'English'
            #finally save the object in db
            inte.save()

            # redirect to cv Edit page:
            return HttpResponseRedirect('/cv/edit?type')


# if a GET (or any other method) we'll create a blank form
    else:
        form = addInterest()

    return render(request, "garden/cvInfoAdd/addInterest.html", {'form': form})


def eduAdd(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addEducation(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # create a new record and store the new project data into it
            edu = education()  #gets new project object
            edu.startTime = form.cleaned_data['start']
            edu.endTime = form.cleaned_data['end']
            edu.uni = form.cleaned_data['uni']
            edu.major = form.cleaned_data['major']
            edu.perform = form.cleaned_data['perform']
            edu.module = form.cleaned_data['module']
            edu.language = 'English'
            #finally save the object in db
            edu.save()

            # redirect to cv Edit page:
            return HttpResponseRedirect('/cv/edit?type')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addEducation()

    return render(request, "garden/cvInfoAdd/addEdu.html", {'form': form})


# Blog page for general version
def blog(request):
    return render(request, "garden/Blog.html", {
        "articles": myArt.objects.all(),
        "popTag": myTag.objects.all()
    })


# Blog page for specified version
def tagBlog(request):
    # Pass the one particular tag's id as the parameter
    param = request.GET['id']
    tagParam = request.GET['tagId']

    return render(
        request,
        "garden/Blog.html",
        {
            # find out all articles with that tag
            "articles": myArt.objects.filter(myTag=param),
            "popTag": myTag.objects.all(),
            "theTag": param,
            "tagId": tagParam
        })


def Article(request):
    # Pass the article's id as the parameter
    param = request.GET['article']
    tagParam2 = request.GET['tagId']

    return render(
        request, "garden/Article.html", {
            "article": myArt.objects.filter(id=param),
            "review": myCom.objects.filter(myArticle=param),
            "popTag": myTag.objects.all(),
            "tagId": tagParam2
        })


def editer(request):
    # Write and preview the blog article in this page
    return render(request, "garden/Edit.html")