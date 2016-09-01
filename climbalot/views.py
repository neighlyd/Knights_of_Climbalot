from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from climbalot.models import Session, Monkey, C_Routes
from climbalot.forms import SessionInputForm, C_Route_Formset, CreateMonkey

from django.views.generic import ListView
from django.utils.decorators import method_decorator



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if Monkey.objects.filter(player=request.user.id).exists():
            monkey = get_object_or_404(Monkey, player=request.user.id)
            return redirect('monkey-home', monkey_pk=monkey.pk)
        else:
            return redirect('create-monkey')
            return render(request, 'climbalot/create_monkey.html')
    else:
        return render(request, 'climbalot/index.html')

def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')

@login_required
def monkey(request, monkey_pk):
    monkey = get_object_or_404(Monkey, pk=monkey_pk)
    context = {'monkey': monkey}
    return render(request, 'climbalot/monkey.html', context)


class AllSessionList(ListView):
    model = Session
    template_name = "climbalot/session_list.html"

    def get_queryset(self):
        return Session.objects.filter(monkey=self.kwargs['monkey_pk'])

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AllSessionList, self).dispatch(*args, **kwargs)

@login_required
def create_monkey(request):
    if Monkey.objects.filter(player=request.user.id).exists():
        monkey = get_object_or_404(Monkey, player=request.user.id)
        return redirect('monkey-home', monkey_pk=monkey.pk)
    else:
        if request.method == 'POST':
            pass
        else:
            context = {'form': CreateMonkey()}
            return render(request, 'climbalot/create_monkey.html', context)


@login_required
def new_session(request, monkey_pk):
    monkey = get_object_or_404(Monkey, pk=monkey_pk)
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
def edit_session(request, monkey_pk, session_pk):
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
