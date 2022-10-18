from django.urls import path

from texnicum.views import *

app_name = 'texnicum'

urlpatterns = [
    path('vacancy/', VacancyListView.as_view(), name='vacancy'),
    path('<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('document/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('documents/', DocumentListView.as_view(), name='document'),
    path('staff/', StaffListView.as_view(), name='staff'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('department/', DepartmentListView.as_view(), name='department'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('', HomeTemplateView.as_view(), name='home'),

]
