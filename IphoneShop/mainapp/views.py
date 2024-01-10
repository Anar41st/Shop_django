from django.shortcuts import render, redirect
from django.http import Http404
from .models import Telephone, Models, Clients, Employees, Feedback
from .forms import ClientForm, FeedbackForm

telephone1 = Telephone.objects.all()[0]
telephone2 = Telephone.objects.all()[1]
telephone3 = Telephone.objects.all()[2]
telephone4 = Telephone.objects.all()[3]
models= Models.objects.all()
modelsp =Models.objects.order_by('memory')[:1]
Fback = Feedback.objects.all()
def index(request):
    return render(request, 'mainapp/mainpage.html', {'telephone1': telephone1, 'telephone2': telephone2, 'telephone3': telephone3, 'telephone4': telephone4, 'models': models, 'modelsp': modelsp})
def about(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    form = FeedbackForm()
    return render(request, 'mainapp/about.html', {'feedback': Fback, 'error': error, 'form': form})

def services(request):
    return render(request, 'mainapp/services.html')
def order(request):
    return render(request, 'mainapp/order.html')
def iphone15(request):
    error=''
    if request.method=='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            error='Форма неверная'
    form = ClientForm()
    return render(request, 'mainapp/iph15.html', {'telephone1': telephone1, 'models': models, 'modelsp': modelsp, 'form': form, 'error': error})
def iphone14(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            error = 'Форма неверная'
    form = ClientForm()
    return render(request, 'mainapp/iph14.html', {'telephone2': telephone2, 'models': models, 'modelsp': modelsp, 'form': form, 'error': error})
def iphone13(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            error = 'Форма неверная'
    form = ClientForm()
    return render(request, 'mainapp/iph13.html', {'telephone3': telephone3, 'models': models, 'modelsp': modelsp, 'form': form, 'error': error})
def iphone11(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            error = 'Форма неверная'
    form = ClientForm()
    return render(request, 'mainapp/iph11.html', {'telephone4': telephone4, 'models': models, 'modelsp': modelsp, 'form': form, 'error': error})
def error(request):
    raise Http404()