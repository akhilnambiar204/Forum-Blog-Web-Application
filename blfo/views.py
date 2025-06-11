from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os
import json

def blfo(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def forump(request):
    if os.path.exists(f'{os.getcwd()}/data.json'):
      with open('data.json','r') as f:
        data = json.load(f)   
        return render(request, 'forump.html',{'data': data})
    return render(request, 'forump.html')
def post(request):
  if request.method == "POST":
      forum = request.POST.get('forum')
      print(forum)
      if os.path.exists(f'{os.getcwd()}/data.json'):
        with open('data.json','r') as f:
          data = json.load(f) 
          if forum in data:
            return render(request, 'post.html', {'data': data[forum]['posts'], 'forum':forum}) 
  return render(request, 'post.html') 
def create_forum(request):
  if request.method == "POST":
      username = request.POST.get('username')
      forum = request.POST.get('forumname')
      fordes = request.POST.get('fordes')
      # username = request.POST.get('username')      

      if not os.path.exists(f'{os.getcwd()}/data.json'):
        data = {}
        with open('data.json','w') as f:
          json.dump(data, f)
      else:
        with open('data.json','r') as f:
          data = json.load(f)
        
      time = datetime.now()
      if not forum in data:
        data[forum] = {}

      data[forum] = {}
      data[forum]['forum_created_by'] = username
      data[forum]['forum_description'] = fordes
      data[forum]['posts'] = {}
      data[forum]['no_of_posts'] = 0
      data[forum]['date'] = time.strftime("%b %d, %Y")
      with open('data.json','w') as f:
        json.dump(data, f, indent = 6) 
      return render(request, 'forump.html',{'status':200})
  return render(request, 'create_forum.html') 


def create(request):
  # template = loader.get_template('create.html')
  print(request.POST)
  if request.method == "POST":
      forum = request.POST.get('forum')
      title = request.POST.get('title')
      if title:
        post_details = request.POST.get('post_details') 
        username = request.POST.get('username')      

        if not os.path.exists(f'{os.getcwd()}/data.json'):
          print("Please create Forum first")
        else:
          with open('data.json','r') as f:
            data = json.load(f)
            if not forum in data:
              print("Please create Forum first")
            else:
              time = datetime.now()
              id = len(data[forum]['posts'])
              data[forum]['posts'][id] = {}
              data[forum]['posts'][id]['title'] = title
              data[forum]['posts'][id]['post_details'] = post_details
              data[forum]['posts'][id]['username'] = username
              data[forum]['posts'][id]['comments'] = []
              data[forum]['posts'][id]['comment_length'] = len(data[forum]['posts'][id]['comments'])
              data[forum]['posts'][id]['date'] = time.strftime("%b %d, %Y")
              with open('data.json','w') as f:
                json.dump(data, f, indent = 6) 
              return render(request, 'post.html',{'status':200 , 'forum': forum, 'data' : data[forum]['posts']})
      else:
        forum = request.POST.get('forum')
        return render(request, 'create.html',{'forum':forum})
      
  return render(request, 'create.html')

def details(request):
  if request.method == "POST":
    key = request.POST.get('key')
    forum = request.POST.get('forum')
    comment = request.POST.get('comment')
    username = request.POST.get('username')
    if os.path.exists(f'{os.getcwd()}/data.json'):
      with open('data.json','r') as f:
        data = json.load(f) 
        if forum in data:
          if comment:
            time = datetime.now()
            data[forum]['posts'][key]['comments'].append({'username':username,'comment':comment, 'date':time.strftime("%b %d, %Y")})
            data[forum]['posts'][key]['comment_length'] = len(data[forum]['posts'][key]['comments'])
            with open('data.json','w') as f:
              json.dump(data, f, indent = 6) 
          return render(request, 'details.html', {'data': data[forum]['posts'][key], 'forum':forum, 'key':key}) 
  return render(request, 'details.html') 

def create_comment(request):
  if request.method == "POST":
    key = request.POST.get('key')
    forum = request.POST.get('forum')
    if os.path.exists(f'{os.getcwd()}/data.json'):
      with open('data.json','r') as f:
        data = json.load(f) 
        if forum in data:
          return render(request, 'create_comment.html', {'data': data[forum]['posts'][key], 'key':key, 'forum':forum})
  return render(request, 'create_comment.html')

def blog_view(request):
  if os.path.exists(f'{os.getcwd()}/blog.json'):
    with open('blog.json','r') as f:
      data = json.load(f) 
      print(data)
      return render(request, 'blog_view.html', {'data': data}) 
  return render(request, 'blog_view.html')

def blog_panel(request):
  print(request.POST)
  if request.method == "POST":
    key = request.POST.get('key')
    print(key)
    with open('blog.json','r') as f:
      data = json.load(f) 
      return render(request, 'blog_panel.html', {'data': data[key]}) 
  return render(request, 'blog_panel.html')

def create_blog(request):
  if request.method == "POST":
    username = request.POST.get('username')
    blogname = request.POST.get('blogname')
    blog_description = request.POST.get('blog_description')
    # username = request.POST.get('username')      

    if not os.path.exists(f'{os.getcwd()}/blog.json'):
      data = {}
      with open('blog.json','w') as f:
        json.dump(data, f)
    else:
      with open('blog.json','r') as f:
        data = json.load(f)
        
    id = len(data)
    time = datetime.now()
    data[id] = {}
    data[id]['blog_created_by'] = username
    data[id]['blogname'] = blogname
    data[id]['blog_description'] = blog_description
    data[id]['date'] = time.strftime("%b %d, %Y")
    with open('blog.json','w') as f:
      json.dump(data, f, indent = 6) 
    return render(request, 'blog_view.html',{'status':200, 'data': data})
  return render(request, 'create_blog.html')
 