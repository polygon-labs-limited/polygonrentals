from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", views.PropertyLandingView.as_view(), name="property-landing"),
    path("about", views.AboutView.as_view(), name="about"),
    path("news", views.NewsView.as_view(), name="news"),
    path("contact", views.ContactView.as_view(), name="contact"),
    path("properties", views.PropertyListView.as_view(), name="property-list"),
    path("<int:pk>", login_required(views.PropertyDetailView.as_view()), name="property-detail"),
    path('api', login_required(views.PropertyListApiView.as_view())),
    path("analysis", login_required(views.PropertyAnalysisView.as_view()), name="property-analysis"),
    path("tools", login_required(views.PropertyToolsView.as_view()), name="property-tools"),
]