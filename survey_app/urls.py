from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name="survey-list"),
    path('<int:id>/', SurveyDetail.as_view(), name="survey-detail"),
    path('P<id>\-P<step>\/', SurveyDetail.as_view(), name="survey-detail-step"),
    path('confirm/?P<uuid>/', ConfirmView.as_view(), name="survey-confirmation"),
]
