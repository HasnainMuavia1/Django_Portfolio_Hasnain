from sqlite3 import IntegrityError

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
import jwt
from .models import Experience, Education, Skills, extend, image, Certifications_license


# Create your views here.

def home(request):
    # print(request.name)
    return render(request, 'home.html')


def Login(request):
    if request.method == 'POST':
        us = request.POST['us']
        p = request.POST['p']
        acc = authenticate(request, username=us, password=p)
        if acc is not None:
            login(request, acc)
            return redirect('Dashboard')
        else:
            return render(request, 'Login.html', {'error': 'Invalid Username or Password'})
    # if request.user.is_authenticated:
    #     return redirect('Dashboard')
    else:
        return render(request, 'Login.html')


def signup(request):
    if request.method == 'POST':
        us = request.POST['us']
        e = request.POST['e']
        p = request.POST['p']
        fn = request.POST.get('fn', '')
        ln = request.POST.get('ln', '')

        # Check if the email is already registered
        if User.objects.filter(email=e).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})

        try:
            account = User.objects.create_user(username=us, password=p, email=e, first_name=fn, last_name=ln,
                                               is_active=False)
            enc = jwt.encode(payload={'id': str(account.pk)}, key='secret', algorithm='HS256')

            try:
                link = request.scheme + '://' + request.get_host() + '/activate/' + str(enc) + '/'
                confirmation_email = EmailMessage('confirmation Mail',
                                                  f'Confirmation email for {us} here is the link {link}', to=[e])

                confirmation_email.send()
            except:
                return HttpResponse('An error occurred')
            # account.save()
            return redirect('home')
        except:
            return render(request, 'signup.html', {'error': 'Username already exists'})
    return render(request, 'signup.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'Dashboard.html')


@login_required(login_url='login')
def mylogout(request):
    try:
        logout(request)
        return redirect('login')
    except:
        pass
    return redirect('login')


@login_required(login_url='login')
def activateAccount(request, id):
    dec = jwt.decode(id, key='secret', algorithms=['HS256'])
    us = User.objects.get(pk=int(dec['id']))
    us.is_active = True
    us.save()
    return redirect('login')


def sendEmail(request):
    account = User.objects.all()
    for email in account.email:
        em = EmailMessage("feeback", "I hope you are doing well please send feedback for website", to=[email])
        em.send()


def skills(request):
    return render(request, 'Skills.html', {'obj': User.objects.first(), "imgObj": image.objects.first()})


def hireMe(request):
    if request.method == 'POST':
        name = request.POST['n']
        message = request.POST['message']
        try:
            to_send = EmailMessage('HireMe', f"Hello I am {name} {message}", to=['Hasnain.muavia2004@gmail.com'])
            to_send.send()
            return render(request, 'Hire.html', {'message': 'successfully sended !'})
        except:
            pass
    return render(request, 'Hire.html', )


@login_required(login_url='login')
def data(request, name):

    user = User.objects.first()
    if request.method == 'POST':
        if name == 'skill':
            skill_name = request.POST['skill']
            Skills.objects.create(skill_id=user, skill_name=skill_name)
        elif name == 'education':
            degree = request.POST['degree']
            institute = request.POST['institute']
            year = request.POST['year']
            Education.objects.create(education_id=user, Degree=degree, institute=institute, year=year)
        elif name == 'certification':
            certificate = request.POST['certificate']
            url = request.POST['url']
            institution = request.POST['institution']
            year = request.POST['year']
            Certifications_license.objects.create(cert_id=user, certificate=certificate, url=url,
                                                  institution=institution, year=year)
        elif name == 'experience':
            experience = request.POST['experience']
            institute = request.POST['institute']
            year = request.POST['year']
            Experience.objects.create(experience_id=user, experience=experience, institute=institute, year=year)
    img = image.objects.all()
    return render(request, 'data.html', {'obj': User.objects.first(), 'name': name, 'img1': img[1], 'img2': img[2]})


import logging

logger = logging.getLogger(__name__)


@login_required(login_url='login')
def delete(request, id, name):
    try:
        if name == 'skill':
            obj = get_object_or_404(Skills, pk=int(id))
        elif name == 'certification':
            obj = get_object_or_404(Certifications_license, pk=int(id))
        elif name == 'education':
            obj = get_object_or_404(Education, pk=int(id))
        elif name == 'experience':
            obj = get_object_or_404(Experience, pk=int(id))
        elif name == 'extend':
            obj = get_object_or_404(extend, pk=int(id))
        else:
            return render(request, 'data.html', {
                'msg': 'not found',
                'name': name,
                'obj': User.objects.first()
            })

        obj.delete()
        return redirect(f'/data/{name}/')
    except Exception as e:
        logger.error(f"Failed to delete {name} with id {id}: {e}")
        return render(request, 'data.html', {
            'msg': 'Unable to delete this time',
            'name': name,
            'obj': User.objects.first()
        })


@login_required(login_url='login')
def edit(request, id, name):
    if name == 'skill':
        obj = get_object_or_404(Skills, pk=int(id))
        obj.skill_name = request.POST['skill']
        obj.save()
        return redirect(f'/data/{name}/')
    elif name == 'certification':
        obj = get_object_or_404(Certifications_license, pk=int(id))
        obj.certificate = request.POST['certificate']
        obj.institution = request.POST['institution']
        obj.url = request.POST['url']
        obj.year = request.POST['year']
        obj.save()
        return redirect(f'/data/{name}/')
    elif name == 'education':
        obj = get_object_or_404(Education, pk=int(id))
        obj.degree = request.POST['degree']
        obj.institute = request.POST['institute']
        obj.year = request.POST['year']
        obj.save()
        return redirect(f'/data/{name}/')
    elif name == 'experience':
        obj = get_object_or_404(Experience, pk=int(id))
        obj.experience = request.POST['experience']
        obj.institute = request.POST['institute']
        obj.year = request.POST['year']
        obj.save()
        return redirect(f'/data/{name}/')
