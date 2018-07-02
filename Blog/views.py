from django.shortcuts import render   # using FBV
from django.shortcuts import get_object_or_404  # using get object in line 17
from django.utils import timezone  # using timezone
from .models import Post  # extracting data from the Post table

# Create your views here.
# y=f(x)
# response=f(request),


def post_list(request):
    #  get post (as list[]) with publsihed date <= (lte) timezone is now AND order by published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request,'Blog/post_detail.html', {'post':post})