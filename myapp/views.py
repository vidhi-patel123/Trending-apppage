from django.shortcuts import render, redirect
from .models import*
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Brochure

# Create your views here.

def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        cuid = Contact.objects.create(name=name,
                                      email=email,
                                      subject=subject,
                                      message=message)
        
        return render(request, 'contact.html')
    else:
        return render(request,'contact.html')
  
def download_brochure(request):
    brochure = get_object_or_404(Brochure, id=1)
    return FileResponse(brochure.file.open(), as_attachment=True, filename=brochure.file.name)
