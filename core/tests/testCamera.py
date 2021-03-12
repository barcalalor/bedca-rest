from django.test import TestCase
from core.models import Camera
from faker import Faker

class CameraTestCase(TestCase):
    def setUp(self):
        faker = Faker()
        
    def test_camera_create_ok(self,faker):
        cam_name = faker.name()
        cam_url = faker.url()

        camera = Camera.objects.create(cam_name, cam_url)
        assert camera != None
        camera.save()
        assert camera.id != None