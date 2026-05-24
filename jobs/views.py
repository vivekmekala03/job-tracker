from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, JobForm
from .models import Job


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'jobs/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'jobs/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    jobs = Job.objects.filter(user=request.user)

    # search
    query = request.GET.get('q', '')
    if query:
        jobs = jobs.filter(company__icontains=query) | jobs.filter(role__icontains=query)

    # filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        jobs = jobs.filter(status=status_filter)

    status_choices = Job.STATUS_CHOICES

    context = {
        'jobs':           jobs,
        'query':          query,
        'status_filter':  status_filter,
        'status_choices': status_choices,
        'total':          Job.objects.filter(user=request.user).count(),
        'interviews':     Job.objects.filter(user=request.user, status='interview').count(),
        'offers':         Job.objects.filter(user=request.user, status='offer').count(),
        'rejected':       Job.objects.filter(user=request.user, status='rejected').count(),
    }
    return render(request, 'jobs/dashboard.html', context)


@login_required(login_url='login')
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job      = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request, 'Job added successfully!')
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Add Job'})


@login_required(login_url='login')
def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated!')
            return redirect('dashboard')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Edit Job'})


@login_required(login_url='login')
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job removed.')
        return redirect('dashboard')
    return render(request, 'jobs/confirm_delete.html', {'job': job})