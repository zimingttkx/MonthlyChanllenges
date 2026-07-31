from django.urls import path
from chanllenges import views

# urlConfig
urlpatterns = [
    path("<int:month>",  views.monthly__challenge_by_number, name = "a"),
    path("<str:month>", views.monthly__challenge_by_str, name = 'b'),
    path("", views.index, name = 'c')
]
