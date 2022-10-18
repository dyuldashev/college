from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # path('news/', include('news.urls')),
    # path('', include('texnicum.urls')),
]

urlpatterns += i18n_patterns(
    url(r'', include('news.urls')),
    url(r'', include('texnicum.urls'))
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
