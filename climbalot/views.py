from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    return render(request, 'climbalot/session.html', {'session': session})
