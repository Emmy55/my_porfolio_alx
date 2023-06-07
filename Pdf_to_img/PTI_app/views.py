from django.shortcuts import render
from django.shortcuts import redirect
from pdf2image import convert_from_bytes
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return render(request, 'PTI_app/home.html')

import glob
import fitz
import os

def image(request):
    if request.method == 'GET' and 'pdff' in request.GET:
        path = str(request.GET['pdff'])
        all_files = glob.glob(f"{path}{'.pdf'}")
        converted_images = []

        # To get better resolution
        zoom_x = 2.0  # horizontal zoom
        zoom_y = 2.0  # vertical zoom
        mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

        for filename in all_files:
            doc = fitz.open(filename)  # open document
            for page in doc:  # iterate through the pages
                pix = page.get_pixmap(matrix=mat)  # render page to an image
                image_path = os.path.join(os.path.media(__file__), 'media', f'page-{page.number}.png')
                pix.save(image_path)  # store image as a PNG
                converted_images.append({'path': image_path})
                print(converted_images)

        return converted_images
    else:
        # Handle the case when the request method is not 'POST' or 'pdf_file' is not present
        return HttpResponse("Input a PDF file please")

def convert_pdf(request):
    converted_images = image(request)
    print(converted_images)

    return render(request, 'PTI_app/home.html', {'converted_images': converted_images})



