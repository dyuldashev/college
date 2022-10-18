from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from news.models import *
from teachers.models import *


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['banner'] = BannerModel.objects.order_by('-pk')[:3]
        context['statistics'] = StatisticsModel.objects.order_by('-pk')[:3]
        context['staff'] = StaffModel.objects.order_by('-pk')[:3]
        context['news'] = NewsModel.objects.order_by('-pk')[:3]
        context['event'] = EventModel.objects.order_by('-pk')[:3]
        context['gallery'] = GalleryModel.objects.order_by('-pk')[:3]
        context['department'] = DepartmentModels.objects.order_by('-pk')[:3]

        return context


class DepartmentListView(ListView):
    template_name = 'department.html'
    queryset = DepartmentModels.objects.order_by('-pk')


class DepartmentDetailView(DetailView):
    model = DepartmentModels
    template_name = 'detail_department.html'


class StaffListView(ListView):
    template_name = 'staff.html'
    queryset = StaffModel.objects.order_by('-pk')


class StaffDetailView(DetailView):
    model = StaffModel
    template_name = 'staff_detail.html'


class DocumentListView(ListView):
    template_name = 'dacument.html'
    queryset = DocumentsofAdmissionsModel.objects.order_by('-pk')


class DocumentDetailView(DetailView):
    model = DocumentsofAdmissionsModel
    template_name = 'dacument_detail.html'


class VacancyListView(ListView):
    template_name = 'vacancy.html'
    queryset = VacancyModel.objects.order_by('-pk')


class VacancyDetailView(DetailView):
    model = VacancyModel
    template_name = 'vacancy_detail.html'



