
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q


class BlogHomePage(View):
    template_name = 'blog/bhome.html'
    def get(self, request):
        blogs = Blogpost.objects.all()
        context={'blogs':blogs,'blog':'active'}
        return render(request,self.template_name,context)

def blogpost(request,id=None):
    blog = Blogpost.objects.get(post_id=id)
    if request.user.is_authenticated:
        user= User.objects.get(username=request.user)
        blogviewers = blog.views_by.split(' +')
        if not str(request.user) in blogviewers:
            blog.views_by += str(user.username) + ' +'
            blog.views += 1
            blog.save()


 
    # blog.views = len
    blog.save()
    comments = BlogComment.objects.filter(blog=blog)
    # only_comments = BlogComment.objects.filter(Q(reply=False) & Q(blog=blog))
    reply = BlogComment.objects.filter(blog=blog).exclude(parent=None)

    context = {'blog':blog,'comments':comments,'reply':reply}
    return render(request,'blog/blogpost.html',context)

def blogsearch(request):
    equery = request.GET.get('search')
    query = equery
 
    if query != '':
        blogs_title = Blogpost.objects.filter(title__icontains=query)
        blogs_category = Blogpost.objects.filter(category__icontains=query)
        blogs_description = Blogpost.objects.filter(description__icontains=query)

        blogs = blogs_title.union(blogs_description,blogs_category) ## union of all multiple queryset

    else:
        blogs = Blogpost.objects.none()

    context = {'blogs':blogs,'query':equery,}
    return render(request,'blog/blogsearch.html',context)
    

def blogComment(request,post_id):
    if request.method == 'POST':
        if request.user.is_authenticated :
            comment = BlogComment()
            # comment = request.POST.get('comment')
            # user = request.user
            # blog = Blogpost.objects.get(post_id=post_id)
            
            # comment = BlogComment(comment=comment, user=user, blog=blog)
            comment.comment = request.POST.get('comment')
            comment.user = request.user
            comment.blog = Blogpost.objects.get(post_id=post_id)
            
            reply = request.POST.get('reply')
            if reply == None:
                comment.save()
                messages.success(request,'Your Comment Added Sucessfully')
            else:
                comment.reply = True 
                com = BlogComment.objects.get(sno=reply)
                comment.parent = com
                comment.save()
                messages.success(request,'Your Reply Added Sucessfully')

        else:
            messages.warning(request,'Please login first')
    

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def blog_dashboard(request):
    return render(request,'blog/blog_dashboard.html')




