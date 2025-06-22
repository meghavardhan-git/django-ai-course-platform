from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json

from .models import Course, UserProgress
from .gemini_service import ask_gemini, ask_gemini_suggestions

@login_required
def course_list(request):
    query = request.GET.get('search')
    category_filter = request.GET.get('category')

    if query:
        courses = Course.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
    elif category_filter:
        courses = Course.objects.filter(category=category_filter)
    else:
        courses = Course.objects.all()

    recommended_videos = [
        {'title': 'DSA - Striver', 'youtube_id': '49kBWM3RQQ8'},
        {'title': 'Python - Telusko', 'youtube_id': 'qHJjMvHLJdg'},
        {'title': 'Python Full Course - CodeWithHarry', 'youtube_id': 'XKHEtdqhLK8'},
    ]

    return render(request, 'course_list.html', {
        'courses': courses,
        'recommended_videos': recommended_videos
    })

@csrf_exempt
@login_required
def gemini_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message', '')
        response = ask_gemini(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
@login_required
def gemini_suggest_courses(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message', '')
        suggestions = ask_gemini_suggestions(user_input)
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

@login_required
def mark_complete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    UserProgress.objects.update_or_create(user=request.user, course=course, defaults={'completed': True})
    return redirect('course_list')

@login_required
def user_progress(request):
    progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'user_progress.html', {'progress': progress})
