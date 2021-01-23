from django.contrib import admin
from django.urls import path, include
from services.views import redirect_to_target_page
#from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('auth/', include('accounts.urls')),
    path('dashboard/', include('services.urls')),
    path('', include('mainapp.urls')),
    path('<str:alias>', redirect_to_target_page)


]
