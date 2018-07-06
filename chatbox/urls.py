from django.conf.urls import url
from .views import SessionView

urlpatterns = [
url(r'^$', SessionView.as_view(), name='new_session')
]
