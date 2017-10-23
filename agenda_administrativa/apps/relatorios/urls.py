from django.conf.urls import url

from .views import (
    # agenda
    agenda_relatorio,

)

urlpatterns = [
    # post views
    # pessoas
    url(r'^agenda-relatorio/(?P<pk>\d+)$', agenda_relatorio, name='agenda_relatorio'),
]
