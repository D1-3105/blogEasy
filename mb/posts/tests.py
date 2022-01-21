from django.test import TestCase
from .models import Post
from django.urls import reverse
class BDtest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')
    def test_object_insertion(self):
        post=Post.objects.get(id=1)
        expected_txt='just a test'
        self.assertEqual(post.text, expected_txt)
class HomePageTests(TestCase):
    def test_correct_template(self):
        resp=self.client.get('/')
        self.assertTemplateUsed(response=resp, template_name='home.html')
        self.assertEqual(resp.status_code, 200)
    def test_correct_location(self):
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

# Create your tests here.
