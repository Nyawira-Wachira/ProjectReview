from django.test import TestCase
from .models import Project,Profile

# Create your tests here.
class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Bikes= Project( user ='Abigail', title ='Bikes',image='default.png', description='A project about posting and hiring bikes')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Bikes,Project))

        # Testing Save Method
    def test_save_method(self):
       self.Bikes.save_project()
       all_objects = Project.objects.all()
       self.assertTrue(len(all_objects)>0)

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Abigail= Profile(user='Abigail',profile_picture='default.png', bio='Hey There, I am using ProjectReview!')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Abigail,Profile))

        # Testing Save Method
    def test_save_method(self):
       self.Abigail.save()
       all_objects = Profile.objects.all()
       self.assertTrue(len(all_objects)>0)


    
