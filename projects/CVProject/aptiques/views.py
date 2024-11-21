from django.shortcuts import render
from .models import AptiQues
from .models import PersonQues
from .models import JobDetails
from .models import JobRequirement
from .models import PreferredCV
 
# Create your views here.

def index(request):
    
    return render(request, 'index.html')

