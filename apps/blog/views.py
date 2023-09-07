from django.shortcuts import render, redirect

from .models import Post
from libs.utils.utils import send_notification


# Create your views here.
def post_list(request):
    content = {}

    published_posts = Post.objects.published()
    content['published_posts'] = published_posts

    # Check if user is admin/superuser
    if request.user.is_superuser:
        not_published_posts = Post.objects.not_published()
        content['not_published_posts'] = not_published_posts

    return render(request, 'blog/post-list.html', content)


def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        # Get blog post title
        title = request.POST.get('title')
        content = request.POST.get('editor')

        # Create blog post
        post = Post.objects.create(title=title, content=content, status=Post.STATUS.DRAFT)
        post.authors.add(request.user)

        # Redirect user to edit_post
        send_notification(request, tag='success', title='Blog post created',
                          message='Your post has been successfully created')
        return redirect('blog:edit-post', uuid=post.uuid)

    return render(request, 'blog/create-post.html')


def edit_post(request, uuid):
    post = Post.objects.get(uuid=uuid)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('editor')
        post.title = title
        post.content = content
        post.save()
        send_notification(request, tag='success', title='Blog post saved', message='Your post has been successfully saved')

    return render(request, 'blog/edit-post.html', {'post': post})
