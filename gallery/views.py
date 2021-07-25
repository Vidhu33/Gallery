from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Image
from .serializers import ImageSerializer
from .forms import ImageForm
from PIL import Image as im


#View for the home page where all the images are listed 
def gallery(request):
    queryset = Image.objects.all()
    tag = request.GET.get('tag', None)
    if tag:
        queryset = Image.objects.filter(tags__name__in = [tag])
    page = request.GET.get('page', 1)
    #setting page_count to 8
    paginator = Paginator(queryset, 8)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    
    result = ImageSerializer(images,many=True)
    context = {'images':result.data}
    context['paginated_image'] = images
    return render(request,'home.html',context = context)


#View for the particular image page where clockwise and anticlockwise buttons are present
def image(request,pk):
    query = Image.objects.get(id=pk)

    if request.method == "POST":
        data = request.POST
        if data.get('clockwise'):
            img = im.open(query.image)
            rotated_image = img.rotate(270)
            rotated_image.save(query.image.file.name, overwrite=True)

        elif data.get('anticlockwise'):
            img = im.open(query.image)
            rotated_image = img.rotate(90)
            rotated_image.save(query.image.file.name, overwrite=True)


    image = ImageSerializer(query)
    return render(request,'image.html',{'image':image.data})


#View for a separat
def addImage(request):
    images = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newImg = form.save(commit=False)
            newImg.save()
            form.save_m2m()
            image = ImageSerializer(newImg)
            return render(request,'image.html',{'image':image.data})
    context ={'form': ImageForm()}
    return render(request,'addImage.html',context=context)
