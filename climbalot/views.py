from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from climbalot.models import Session
from climbalot.forms import SessionInputForm

# Create your views here.


@login_required
def session(request, pk):
    # get the session with the correct PK.
    session = get_object_or_404(Session, pk=pk)
    # create a dictionary that maps the session instance to a string 'session'
    context = {'session':session}
    if request.method == 'POST':
        pass
    else:
        # Append a form set to the proper instance to the dictionary and map it to the string 'form'.
        context['form'] = SessionInputForm(instance=session)
    return render(request, 'climbalot/session.html', context)
