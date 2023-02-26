from django.shortcuts import get_object_or_404 , render
from django.shortcuts import redirect
from .forms import CommenForm, EmailForm
from django.core.mail import send_mail
from django.utils import timezone
from .models import Post, Comment, Tag
import yagmail

def get_promo_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            yag = yagmail.SMTP("pybot58@gmail.com",
                               "tviekdwnvpncavmk")
            print('!!!EMAIL SEND!!!')
            yag.send(to=data['email'],
                subject = f"Hello, its test email from AVEAD",
                contents = 'TEST EMAIL',
            )
    return redirect('home')

# Create your views here.
def home_page(request):
    tags = Tag.objects.all()[:10]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    data = {'tags' : tags, 'posts' : posts}
    return render(request, 'home/post_list.html', {'data': data})
def post_detail(request, pk):
    
    obj={}
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    obj['post'] = post
    obj['comments'] = comments
    return render(request, 'home/post_detail.html', {'obj': obj})
def comment_new(request, pk):
    if request.method == 'POST':
        form = CommenForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommenForm()
    return render(request, 'home/new_comment.html', {'form': form})

def tags_page(request):
    tags = Tag.objects.all()
    return render(request, 'home/tags_list.html', {'tags': tags})
def tag_detail(request, pk): 
    tag = get_object_or_404(Tag, pk=pk)
    tags = Tag.objects.all()[:10]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').filter(tags=tag)
    data = {'tags' : tags, 'posts' : posts}
    return render(request, 'home/post_list.html', {'data': data})
def contacts_page(request): 
    return render(request, 'home/contacts_list.html')