from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):

    return render(request, 'blog/blogHome.html')
    # return HttpResponse('This is bloghome')

def blogPost(request, slug):
    return render(request, 'blog/blog.htmPost.html')

    # return HttpResponse(f'This is blogPost:{slug}')
    
