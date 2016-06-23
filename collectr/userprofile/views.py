# django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

from userprofile import forms


class LoginRequiredMixin(object):
    """User must be logged in to access this view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


@login_required
def home(request):
    return render(request, 'userprofile/home.html')


@login_required
def rss(request):
    form = forms.RssForm(request.user, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        to_add = form.cleaned_data['feeds']
        to_del = list(set(form.fields['feeds'].initial) - set(to_add))

        for feed in to_add:
            feed.users.add(request.user)

        for feed in to_del:
            feed.users.remove(request.user)
        return redirect('userprofile:rss')

    data = {
        'form': form,
    }
    return render(request, 'userprofile/rss.html', data)


@login_required
def add_rss(request):
    form = forms.AddRssForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('userprofile:rss')
    data = {
        'form': form,
    }
    return render(request, 'userprofile/add_rss.html', data)


@login_required
def filters(request):

    form = forms.FiltersForm(request.user, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        for filtr in forms.filters:
            pass
        return redirect('userprofile:home')

    data = {
        'form': form,
    }
    return render(request, 'userprofile/filters.html', data)
