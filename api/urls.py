from django.urls import path
from .views import CalculatorApiView


urlpatterns = [
    path('', CalculatorApiView.as_view())    
]
