# Create your views here.
from django.shortcuts import render_to_response
from teams.models import Customer, Manager, Developer, Project, Specification, Job
import logging
logger = logging.getLogger(__name__)


def index(request):
    c = Customer.objects.filter(name=request.user.username)
    m = Manager.objects.filter(name=request.user.username)
    d = Developer.objects.filter(name=request.user.username)
    if c:
        user = Customer.objects.get(name=request.user.username)
        specifications = Specification.objects.filter(customer=user)
        return render_to_response('teams/customer.html', {'specifications': specifications})
    elif m:
        user = m.get(name=request.user.username)
        projects = Project.objects.filter(manager=user)
        specifications = Specification.objects.all()
        return render_to_response('teams/manager.html', {'projects': projects, 'specifications': specifications})
    elif d:
        user = d.get(name=request.user.username)
        jobs = Job.objects.filter(developer=user)
        return render_to_response('teams/developer.html', {'developer': user, 'jobs': jobs})


def login(request):
    return render_to_response('login/login.html')


def customer(request):
    user = Customer.objects.get(name=request.user.username)
    specifications = Specification.objects.filter(id=user.id)
    return render_to_response('teams/customer.html', {'specifications': specifications})


def manager(request):
    user = Manager.objects.get(name=request.user.username)
    projects = Project.objects.filter(id=user.id)
    return render_to_response('teams/manager.html', {'projects': projects})


def developer(request):
    user = Developer.objects.get(name=request.user.username)
    project = Project.objects.get(id=user.id)
    return render_to_response('teams/developer.html', {'project': project})


def create_project(request):
    new_project = Project()

    new_project.manager = Manager.objects.get(name=request.user.username)
    new_project.name = request.GET["name"]
    if Specification.objects.filter(id=request.GET["specification_id"]):
        new_project.specification = Specification.objects.get(id=request.GET["specification_id"])
    else:
        return render_to_response('teams/error.html', {"error_message": "Incorrect specification's id"})
    new_project.save()

    return render_to_response('teams/create_project.html', {'new_project': new_project})


def create_project_form(request):
    return render_to_response('teams/create_project_form.html')


def create_specification(request):
    new_specification = Specification()
    new_specification.name = request.GET["name"]
    new_specification.customer = Customer.objects.get(name=request.user.username)
    new_specification.save()

    return render_to_response('teams/create_specification.html', {'new_specification': new_specification})


def create_specification_form(request):
    return render_to_response('teams/create_specification_form.html', {''})


def create_job(request):
    new_job = Job()
    new_job.qualification = request.GET["qualification"]
    new_job.specification = Specification.objects.get(id=request.GET["specification_id"])
    new_job.developer = Developer.objects.get(name="Zasenko")
    new_job.haveDeveloper = False
    new_job.save()

    return render_to_response('teams/create_job.html', {'new_job': new_job})


def create_job_form(request):
    specification_id = request.GET["specification_id"]
    return render_to_response('teams/create_job_form.html', {"specification_id": specification_id})


def specification_detail(request, pk):
    specification = Specification.objects.get(id=pk)
    jobs = Job.objects.filter(specification=specification)
    return render_to_response('teams/specification_detail.html', {'specification': specification, 'jobs': jobs})


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    j1 = Job.objects.filter(specification=project.specification, haveDeveloper=False)
    j2 = Job.objects.filter(specification=project.specification, haveDeveloper=True)
    return render_to_response('teams/project_detail.html', {'project': project, 'free_jobs': j1, 'busy_jobs': j2})


def job_detail(request, pk):
    job = Job.objects.get(id=pk)
    project = Project.objects.get(specification=job.specification)
    developers = Developer.objects.filter(qualification=job.qualification)
    return render_to_response('teams/job_detail.html', {'job': job, 'project': project, 'developers': developers})


def choose(request):
    job = Job.objects.get(id=request.GET['job_id'])
    job.haveDeveloper = True
    developer = Developer.objects.get(id=request.GET['developer_id'])
    job.developer = developer
    job.save()
    return render_to_response('teams/choose_form.html', {'developer': developer, 'job': job})


def error(request):
    return render_to_response('teams/error.html', {'error_message': "ERROR"})