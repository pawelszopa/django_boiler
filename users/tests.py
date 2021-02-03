from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Igor",
            email="b@b.pl",
            password="testpass123"
        )

        #   asercje (ify z roznymi conditions)
        self.assertEqual(user.username, "Igor")
        self.assertEqual(user.email, "b@b.pl")
        self.assertTrue(user.is_active)
        # email send by app to user to confirm and when he confirmed he/she status will be in active
        self.assertFalse(user.is_staff)  # czy jest modem
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="b@b.pl",
            password="testpass123"
        )

        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "b@b.pl")
        self.assertTrue(admin_user.is_active)
        # email send by app to user to confirm and when he confirmed he/she status will be in active
        self.assertTrue(admin_user.is_staff)  # czy jest modem
        self.assertTrue(admin_user.is_superuser)
