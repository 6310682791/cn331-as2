from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Enrollment

# Create your tests here.

class CourseTestCase(TestCase):

    def setUp(self):
        student1 = User.objects.create(username = "6310682791", first_name = "Kasidej")
        course1 = Course.objects.create(sub_code = "CN331", max_seat = 2)
        course1.registered.add(student1)


    def test_seat_available(self):
        cn331 = Course.objects.first()

        self.assertTrue(cn331.registered.count() < cn331.max_seat)

    def test_seat_unavailable(self):
        student2 = User.objects.create(username = "6310611113", first_name = "Yanadech" )

        cn331 = Course.objects.first()
        cn331.registered.add(student2)

        self.assertFalse(cn331.registered.count() < cn331.max_seat)



