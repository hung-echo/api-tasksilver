from django.conf.urls import url
from HiredApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'service$',views.ServiceAPI),
    url(r'^service/([0-9]+)$',views.ServiceAPI),


    url(r'^service/savefile',views.SaveFile),
    url(r'^task/savefile',views.SaveFile),
    url(r'^user/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)