from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from noteapp import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.main, name='index'),
    url(r'^note/$', views.note_list),
    url(r'^note/(?P<pk>[0-9]+)/$', views.note_detail),

]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])