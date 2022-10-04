from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .forms import RegisterForm
from django.contrib import messages

def home(request):
  return render(request, 'pages/home.html')
  
def login(request):
  return render(request, 'pages/login.html')

def register_usuario(request):
  register_form_data = request.session.get('register_from_data',None)
  form = RegisterForm(register_form_data)
  return render(request, 'pages/usuario.html', {
    'form': form,
  })

def register_create(request):
  if not request.POST:
    raise Http404()

  POST = request.POST
  request.session['register_form_data'] = POST
  form = RegisterForm(POST)

  if form.is_valid():
    form.save()
    messages.success(request,'Your user is created, please log in.')

    del(request.session['register_form_data'])
  return redirect('MYC:usuario')

def register_estabelecimento(request):
  return render(request, 'pages/estab.html')

