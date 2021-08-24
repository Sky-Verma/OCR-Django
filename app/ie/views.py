from django.shortcuts import render
from .forms import Image_form
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create your views here.

def home(request):
    return render(request,'index.html')

def img_to_txt(request):
    form = Image_form(request.POST,request.FILES)
    if request.method == "POST":
        form = Image_form(request.POST,request.FILES)
        image = form['image'].data
        if form.is_valid():
            image_opened = Image.open(image)
            text = tess.image_to_string(image_opened)
            if text:
                return render(request,'file_upload.html',{'text':text,'form':form})
            else:
                return render(request,'file_upload.html',{'text':'Something went wrong','form':form})
    return render(request,'file_upload.html',{'form':form})


