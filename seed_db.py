import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from onlinecourse.models import Instructor, Course, Lesson, Question, Choice
from django.contrib.auth.models import User

# Add admin as Instructor
admin_user = User.objects.get(username='admin')
instructor, _ = Instructor.objects.get_or_create(user=admin_user, defaults={'total_learners': 0})

# Create course
course, created = Course.objects.get_or_create(
    name="Learning Django",
    defaults={
        "description": "Django is an extremely popular and fully featured server-side web framework, written in Python",
        "pub_date": date.today(),
        "total_enrollment": 0
    }
)
if created:
    course.instructors.add(instructor)

# Create Lesson
Lesson.objects.get_or_create(
    course=course,
    title="What is Django",
    defaults={
        "order": 0,
        "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source."
    }
)

# Create Question
question, _ = Question.objects.get_or_create(
    course=course,
    question_text="Is Django a Python framework",
    defaults={
        "grade": 100
    }
)

# Create Choices
Choice.objects.get_or_create(
    question=question,
    choice_text="Yes",
    defaults={"is_correct": True}
)
Choice.objects.get_or_create(
    question=question,
    choice_text="No",
    defaults={"is_correct": False}
)

print("Database seeded successfully.")
