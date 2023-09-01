from datetime import datetime
import os
from django.conf import settings
from django.shortcuts import render
from .forms import GoogleVisionForm
from .utils import detectObjects

def home(request):
    url = ""

    if request.method == 'POST':
        form = GoogleVisionForm(request.POST, request.FILES)
        if form.is_valid():
            google_vision = form.save(commit=False)

            now = datetime.now()
            timestamp = now.strftime("%Y%m%d%H%M%S")
            # Dosya adını oluşturun
            filename = f"orj_{timestamp}.jpg"
            google_vision.image.name = filename
            
            google_vision.save()

            url = os.path.join(settings.MEDIA_ROOT, 'images\\')
            
            google_vision.result = detectObjects(url + filename)

            google_vision.save()
    else:
        form = GoogleVisionForm()

    return render(request, 'home.html', {'form': form})
