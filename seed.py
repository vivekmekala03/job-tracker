import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobtracker.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job

# Create a demo user if not exists
user, created = User.objects.get_or_create(username='demo')
if created:
    user.set_password('demo1234')
    user.save()
    print('Demo user created — username: demo / password: demo1234')

# Clear existing jobs for this user
Job.objects.filter(user=user).delete()

# Seed jobs
jobs = [
    {'company': 'Google',        'role': 'Software Engineer',         'status': 'interview', 'job_url': 'https://careers.google.com', 'notes': 'Technical round scheduled for next week.'},
    {'company': 'Microsoft',     'role': 'Backend Developer',         'status': 'screening', 'job_url': 'https://careers.microsoft.com', 'notes': 'HR call done, waiting for technical round.'},
    {'company': 'Amazon',        'role': 'SDE Intern',                'status': 'applied',   'job_url': 'https://amazon.jobs', 'notes': ''},
    {'company': 'Flipkart',      'role': 'Python Developer',          'status': 'offer',     'job_url': 'https://flipkart.com/careers', 'notes': 'Offer letter received. CTC: 8 LPA.'},
    {'company': 'Zoho',          'role': 'Django Developer',          'status': 'applied',   'job_url': 'https://zoho.com/careers', 'notes': 'Applied via referral.'},
    {'company': 'Infosys',       'role': 'Systems Engineer',          'status': 'rejected',  'job_url': '', 'notes': 'Did not clear the aptitude round.'},
    {'company': 'Swiggy',        'role': 'Full Stack Developer',      'status': 'interview', 'job_url': 'https://careers.swiggy.com', 'notes': 'System design round pending.'},
    {'company': 'Razorpay',      'role': 'Backend Engineer',          'status': 'screening', 'job_url': 'https://razorpay.com/jobs', 'notes': ''},
    {'company': 'Freshworks',    'role': 'Associate Software Engineer','status': 'applied',  'job_url': 'https://freshworks.com/company/careers', 'notes': 'Applied through LinkedIn.'},
    {'company': 'TCS',           'role': 'Graduate Engineer Trainee', 'status': 'rejected',  'job_url': '', 'notes': 'Rejected after HR round.'},
]

for j in jobs:
    Job.objects.create(user=user, **j)

print(f'{len(jobs)} demo jobs added successfully!')