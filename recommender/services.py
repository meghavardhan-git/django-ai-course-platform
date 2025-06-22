from .models import Course, UserProgress

def get_courses(search_query=None, category=None):
    courses = Course.objects.all()
    if search_query:
        courses = courses.filter(title__icontains=search_query) | courses.filter(category__icontains=search_query)
    if category:
        courses = courses.filter(category__icontains=category)
    return courses

def get_recommendations_for_user(user):
    completed_courses = UserProgress.objects.filter(user=user, completed=True)
    if completed_courses.exists():
        last_course = completed_courses.last().course
        return Course.objects.filter(category=last_course.category).exclude(id=last_course.id)
    else:
        return Course.objects.all()[:5]
