from django.conf.urls import url

from .views import (
    PessoasEnvolvidasList,
    PessoasEnvolvidasDetail,
    DepartamentoSetorList,
    DepartamentoSetorDetail
    )


urlpatterns = [
     url(r'^pessoas-envolvidas/$', PessoasEnvolvidasList.as_view()),
     url(r'^pessoas-envolvidas/(?P<pk>[0-9]+)/$', PessoasEnvolvidasDetail.as_view()),

     url(r'^departamento-setor/$', DepartamentoSetorList.as_view()),
     url(r'^departamento-setor/(?P<pk>[0-9]+)/$', DepartamentoSetorDetail.as_view())

     #url(r'^statuses/(?P<pk>[0-9]+)/$', views.StatusDetail.as_view())
]
