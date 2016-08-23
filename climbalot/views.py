from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from climbalot.models import Session, Monkey, C_Routes
from climbalot.forms import SessionInputForm, C_Route_Formset

# Create your views here.


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
