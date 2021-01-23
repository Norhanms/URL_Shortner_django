from django.shortcuts import render, redirect
from .models import Url
from django.contrib import auth, messages
from django.contrib.sites.shortcuts import get_current_site
import random
import string


def getAlias(l):
    return "".join([random.choice(string.ascii_letters+string.digits)
                    for i in range(l)])


def dashboard(request):
    if request.method == "POST":
        url = request.POST["URL"]
        alias = request.POST.get("alias", None)

        if not alias:
            alias = getAlias(6)
        try:
            # request.user.url_set(target_ur-url)
            Url.objects.create(user=request.user,
                               target_url=url, alias=alias).save()
            messages.success(request, "Shorted successfuly")
            return redirect("dashboard")

        except:
            messages.error(request, "Alias aleardy in use, choose another one")
            return render(request, 'dashboard.html', {"url": url, "alias": alias})
    site = get_current_site(request)
    return render(request, 'dashboard.html', {"domain": site})


def home(request):
    print("home")
    return render(request, 'home.html', {})
