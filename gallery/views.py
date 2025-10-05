from django.shortcuts import render
from .models import GalleryImage

def gallery_view(request):
    images1 = GalleryImage.objects.filter(category='image1')
    images2 = GalleryImage.objects.filter(category='image2')
    images3 = GalleryImage.objects.filter(category='image3')
    images4 = GalleryImage.objects.filter(category='image4')

    context = {
        'images1': images1,
        'images2': images2,
        'images3': images3,
        'images4': images4,
    }
    return render(request, 'gallery.html', context)
