from django.shortcuts import render
from django.http import HttpResponse
import tempfile
import fitz

def home(request):
    return render(request, 'PTI_app/home.html')

# def convert_pdf(request):
#     if request.method == 'POST' and request.FILES['pdf_file']:
#         pdf_file = request.FILES['pdf_file']
#         images = []

#         with tempfile.TemporaryDirectory() as temp_dir:
#             temp_file = tempfile.NamedTemporaryFile(suffix='.pdf', dir=temp_dir, delete=False)
#             with open(temp_file.name, 'wb') as f:
#                 for chunk in pdf_file.chunks():
#                     f.write(chunk)

#             doc = fitz.open(temp_file.name)
#             for page_num in range(doc.page_count):
#                 page = doc.load_page(page_num)
#                 pix = page.get_pixmap()
#                 image_data = pix.get_image_data(output='png')
#                 images.append(image_data)

#         return render(request, 'PTI_app/home.html', {'images': images})

#     return HttpResponse("Invalid request")

import base64
import fitz

def convert_pd(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    string = text.encode('ascii')
    encoded_string = base64.b64encode(string)
    decoded_string = encoded_string.decode('ascii')
    
    return decoded_string


from django.shortcuts import render

def convert_pdf(request):
    pdf_path = request.GET.get('pdff')
    base64_string = convert_pd(pdf_path)
    
    context = {
        'base64_string': base64_string
    }
    return render(request, 'PTI_app/home.html', context)