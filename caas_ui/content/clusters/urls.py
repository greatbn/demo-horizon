from django.conf.urls import url

from caas_ui.content.clusters import views

urlpatterns = [
    url(r'^$',
        view=views.IndexView.as_view(),
        name='index')
]