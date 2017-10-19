from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from filebrowser.sites import site


from atividades.api.viewsets import (
    PessoasEnvolvidasAgendaViewSet,
    DepartamentoSetorViewSet,
    EsferaViewSet,
    OrgaoDemandanteViewSet,
    AgendaTipoViewSet,
    AgendaAdministrativaViewSet,
    AgendaMovimentacaoViewSet,
    AgendaAnexoViewSet
    )


router = DefaultRouter()
router.register('pessoa-envolvida', PessoasEnvolvidasAgendaViewSet)
router.register('departamento-setor', DepartamentoSetorViewSet)
router.register('esfera', EsferaViewSet)
router.register('orgao-demandante', OrgaoDemandanteViewSet)
router.register('agenda-tipo', AgendaTipoViewSet)
router.register('agenda-administrativa', AgendaAdministrativaViewSet)
router.register('agenda-movimentacao', AgendaMovimentacaoViewSet)
router.register('agenda-anexo', AgendaAnexoViewSet)

urlpatterns = router.urls

urlpatterns = [

    url(r'^account/', include('account.urls')),

    # grappelli
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),

    # api urls
    # url(r'^', include('atividades.urls')),
    url(r'^api/', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),

    # thirdy part url
    url(r'^select2/', include('django_select2.urls')),

    # local apps
    url(r'^', include('atividades.urls', namespace='atividades', app_name='atividades')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
