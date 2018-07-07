from django.conf.urls import url
from .views import CreateMessageView, ChatBoxList, LoadMessagesViewSet
urlpatterns = [
url(r'^conversations$', ChatBoxList.as_view(), name='conversation'),
url(r'^send-message$', CreateMessageView.as_view(), name='send-message'),
url(r'^load-messages/(?P<receiver>\d+)$', LoadMessagesViewSet.as_view({'get': 'list'}), name='load-messages'),
]
