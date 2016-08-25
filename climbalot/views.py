from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from climbalot.models import Session, Monkey, C_Routes
from climbalot.forms import SessionInputForm, C_Route_Formset

# API Imports
from rest_framework import mixins, generics
from climbalot.serializers import MonkeySerializer, UserSerializer, SessionSerializer, C_RoutesSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MonkeyList(generics.ListCreateAPIView):
    queryset = Monkey.objects.all()
    serializer_class = MonkeySerializer

class MonkeyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monkey.objects.all()
    serializer_class = MonkeySerializer

class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class C_RouteList(generics.ListCreateAPIView):
    queryset = C_Routes.objects.all()
    serializer_class = C_RoutesSerializer

class C_RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = C_Routes.objects.all()
    serializer_class = C_RoutesSerializer

# non-API views

@login_required
def new_session(request):
    monkey = get_object_or_404(Monkey, player = request.user.id)
    context = {'monkey': monkey}
    if request.method == "POST":
        session = Session(monkey=monkey)
        form = SessionInputForm(data=request.POST, instance=session)
        if form.is_valid():
            session = form.save(commit=False)
            c_route_formset = C_Route_Formset(data=request.POST, instance=session)
            if c_route_formset.is_valid():
                session.save()
                c_route_formset.save()
                return redirect('index')
    else:
        context['form'] = SessionInputForm()
        context['c_route_formset'] = C_Route_Formset()
    return render(request, 'climbalot/session.html', context)

@login_required
def edit_session(request, pk):
    # get the monkey associated with the request.
    monkey = get_object_or_404(Monkey, player = request.user.id)
    # all variables are passed to the template through a dictionary.
    context = {'monkey': monkey}
    # get the session with the correct PK.
    session = get_object_or_404(Session, pk=pk)
    context['session'] = session
    context['c_route_formset'] = C_Route_Formset(instance=session)
    if request.method == 'POST':
        form = SessionInputForm(data=request.POST, instance=session)
        if form.is_valid():
            session = form.save(commit=False)
            c_route_formset = C_Route_Formset(data = request.POST, instance=session)
            if c_route_formset.is_valid():
                session.save()
                c_route_formset.save()
                return redirect('index')
    else:
        # Append a form set to the proper instance to the dictionary and map it to the string 'form'.
        context['form'] = SessionInputForm(instance=session)
    return render(request, 'climbalot/session.html', context)
