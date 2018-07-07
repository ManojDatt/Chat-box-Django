from django.conf.urls import url
from .views import CreateMessageView
urlpatterns = [
url(r'^send-message$', CreateMessageView.as_view(), name='send-message'),
]
