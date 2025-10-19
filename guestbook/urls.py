
from django.urls import path
from .views import (
    EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView, signup, guestbook_my
)

urlpatterns = [
    path('', EntryListView.as_view(), name='guestbook'),
    path('<int:pk>/', EntryDetailView.as_view(), name='guestbook-detail'),
    path('create/', EntryCreateView.as_view(), name='guestbook-create'),
    path('<int:pk>/edit/', EntryUpdateView.as_view(), name='guestbook-edit'),
    path('<int:pk>/delete/', EntryDeleteView.as_view(), name='guestbook-delete'),
    path('signup/', signup, name='signup'),
    path('<int:pk>/my/', guestbook_my, name='guestbook-my'),
]

