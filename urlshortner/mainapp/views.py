from django.shortcuts import render, redirect
from services.models import Url
from django.contrib import auth, messages
from django.contrib.sites.shortcuts import get_current_site
import random
import string


def getAlias(l):
    return "".join([random.choice(string.ascii_letters+string.digits)
                    for i in range(l)])


def home(request):
    if request.method == "POST":
        url = request.POST["URL"]
        alias = getAlias(6)
        try:
            Url.objects.create(user=request.user,
                               target_url=url, alias=alias).save()
            messages.success(request, "Shorted successfuly")
            return redirect("home")

        except:
            messages.error(request, "Alias aleardy in use, choose another one")
            return render(request, 'home.html', {"url": url, "alias": alias})
    site = get_current_site(request)
    return render(request, 'home.html', {"domain": site})
