from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
from .models import Course, Enrollment

class CourseViewTestCase(TestCase):

    def setUp(self):
        student1 = User.objects.create_user(username = "6310682791", password = "ton12345", first_name = "Kasidej")
        course1 = Course.objects.create(sub_code = "CN331", max_seat = 1)
        course1.registered.add(student1)
        
    def test_subject_view_status_code(self):
        """ index view's status code is ok """
        c = Client()
        c.login(username="6310682791", password= "ton12345")
        response = c.get("/subject")
        self.assertEqual(response.status_code, 200)

    def test_subject_view_context(self):
        """ context is correctly set """
        c = Client()
        c.login(username="6310682791", password= "ton12345")
        response = c.get("/subject")
        self.assertEqual(
            response.context['subject'].count(), 1)

    # def test_valid_flight_page(self):
    #     """ valid flight page should return status code 200 """
    #     c = Client()
    #     c.login(username="6310682791", password= "ton12345")
    #     response = c.get(reverse('flights:flight', args=(f.id,)))
    #     self.assertEqual(response.status_code, 200)

    # def test_invalid_flight_page(self):
    #     """ invalid flight page should return status code 404 """

    #     max_id = User.objects.all().aggregate(Max("id"))['id__max']

    #     c = Client()
    #     response = c.get(reverse('flights:flight', args=(max_id+1,)))
    #     self.assertEqual(response.status_code, 404)

    def test_cannot_book_nonavailable_seat_flight(self):
        """ cannot book full capacity flight"""
        student2 = User.objects.create_user(username= "6310611113", password="fluke123",first_name = "Yannadech")
        f = Course.objects.first()
        f.registered.add(student2)
        f.save()

        c = Client()
        c.login(username = "6310611113", password = "fluke123")
        c.get('/addSubs')

        self.assertFalse(f.registered.count() < f.max_seat)