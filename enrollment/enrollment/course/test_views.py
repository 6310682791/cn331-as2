from http import client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
from .models import Course, Enrollment
#from course.views import login_view, subject, addSub, removeSub, logout_view

class CourseViewTestCase(TestCase):

    def setUp(self):
        student1 = User.objects.create_user(username = "6310682791", password = "ton12345", first_name = "Kasidej")
        course1 = Course.objects.create(sub_code = "CN331", max_seat = 1)
        course1.registered.add(student1)

    def test_subject_view_context(self):
        """ context is correctly set """
        c = Client()
        c.login(username="6310682791", password= "ton12345")
        response = c.get("/subject")
        self.assertEqual(
            response.context['subject'].count(), 1)

    def test_cannot_book_nonavailable_seat_flight(self):
        """ cannot book full capacity flight"""
        student2 = User.objects.create_user(username= "6310611113", password="fluke123",first_name = "Yannadech")
        f = Course.objects.first()
        f.registered.add(student2)
        f.save()

        c = Client()
        c.login(username = "6310611113", password = "fluke123")
        c.get('addSub')

        self.assertFalse(f.registered.count() < f.max_seat)

    def test_project_index(self):
        c = Client()
        c.login(username="6310682791", password= "ton12345")
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/index.html')

    def test_project_test(self):
        c = Client()
        c.login(username="6310682791", password= "ton12345")
        response = c.get(reverse('test'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/test.html')
    
    def test_project_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course/login.html')

    # def test_project_addSub(self):
    #     c = Client()
    #     c.login(username="6310682791", password= "ton12345")
    #     response = c.get(reverse('addSub'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'course/subject.html')

    # def test_project_removeSub(self):
    #     response = self.client.get(reverse('removeSub'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'course/subject.html')

