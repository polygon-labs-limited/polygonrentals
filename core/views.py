from re import template

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from .models import Property, Post
from .serializers import PropertySerializer

class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'about'
        context['page_title'] = 'About us'

        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'contact'
        context['page_title'] = 'Contact us'

        return context


class NewsView(ListView):
    model = Post
    template_name = 'core/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'news'
        context['page_title'] = 'News'

        return context

class PropertyLandingView(TemplateView):
    template_name = 'core/property_landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'landing'
        context['page_title'] = 'Welcome to Polygon Rentals Ltd'

        return context


class PropertyAnalysisView(ListView):
    model = Property
    template_name = 'core/property_analysis_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'analysis'

        return context


class PropertyToolsView(ListView):
    model = Property
    template_name = 'core/property_tools.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'tools'
        context['page_title'] = 'Tools'

        return context

class PropertyDetailView(DetailView):
    model = Property

    def get_context_data(self, **kwargs):
        property = Property.objects.get(id=self.object.id)
        context = super().get_context_data(**kwargs)
        context['gross_yield'] = f'{round((property.current_rent * 12) / property.value * 100, 2)}%'
        context['potential_gross_yield'] = f'{round((property.market_rent * 12) / property.value * 100, 2)}%'
        context['is_owner'] = property.owner == self.request.user
        context['mortgage_deal_expiry_date'] = property.mortgage_deal_expiry_date
        context['page_title'] = property.address
        
        return context


class PropertyListView(ListView):
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        city = self.request.GET.get('city', False)

        val = 0
        mortgages = 0
        current_rents = 0
        potential_rents = 0

        properties = Property.objects.filter()

        if city:
            properties = properties.filter(city=city)

        for property in properties:
            val += property.value
            mortgages += property.mortgage
            current_rents += property.current_rent
            potential_rents  += property.market_rent

        current_rents = current_rents * 12
        potential_rents = potential_rents * 12

        difference_in_rent = f'£{int(potential_rents - current_rents)}'
        ltv = f'{int((mortgages / val) * 100)}%'

        equity_percentage = 100 - int((mortgages / val) * 100)
        rate_of_return = f'{round(round((1 / equity_percentage) * 100, 2) * 5, 2)}%'

        doubling_period = f'{round(72 / (round((1 / equity_percentage) * 100, 2) * 5), 2)} years'

        context['portfolio_value'] = val
        context['outstanding_mortgages'] = mortgages
        context['ltv'] = ltv
        context['current_gross_yield'] = f'{round(current_rents / val * 100, 2)}%'
        context['potential_gross_yield'] = f'{round(potential_rents / val * 100, 2)}%'
        context['difference_in_rent'] = difference_in_rent
        context['properties'] = properties
        context['rate_of_return'] = rate_of_return
        context['doubling_period'] = doubling_period
        context['potential_rents'] = potential_rents
        context['page_name'] = 'properties'
        context['page_title'] = 'Properties'

        return context


class PropertyListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Property.objects.filter(owner = request.user.id)
        serializer = PropertySerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)