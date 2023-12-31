from django.test import SimpleTestCase
from django.urls import reverse

# Profile


class HomepageTests(SimpleTestCase):
    databases = ['default']

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("profile"))
        self.assertTemplateUsed(response, "profile.html")


