from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from events.serializer import event_serializer

urlpatterns = [
    path('', home.as_view(), name='events-home'),
    path('event-list', event_list.as_view(), name='events-list'),
    path('event-create', event_create.as_view(), name='events-create'),
    path('event-list/<int:id>/', event_detail.as_view(), name='events-detail'),
    path('api', API_events.as_view(), name='api-list-events'),

    # path('search', events_search.as_view(), name='search')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
