from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path


urlpatterns = [
    path('', show_landing, name='landing_holiday'),
    path('events/<int:pk>', show_list_events, name='list_event_holiday'),
    path('event/<int:pk>', show_event, name='event_holiday')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)