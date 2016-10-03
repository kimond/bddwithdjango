from django.test import TestCase

from .factories import UserFactory, InterestFactory


class UserModelTest(TestCase):
    def user_has_interests(self):
        user = UserFactory()
        user.interests.add('Django')
        user.save()
        self.assertEquals(user.interests.count(), 1)


class InterestModelTest(TestCase):
    def test_string_representation(self):
        interest = InterestFactory()

        self.assertEquals(str(interest), interest.name)


class HomepageTest(TestCase):
    def test_homepage_is_loaded_correctly(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_homepage_render_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_render_interests_checkboxes(self):
        user = UserFactory()
        interest = InterestFactory()
        user.interests.add(interest)
        self.client.force_login(user)
        response = self.client.get('/')
        self.assertContains(response, interest.name)

    def test_POST_returns_filtered_users_in_template(self):
        user = UserFactory()
        user2 = UserFactory()
        interest = InterestFactory(name="Django")
        interest2 = InterestFactory(name="Testing")
        user.interests.add(interest)
        user2.interests.add(interest2)
        self.client.force_login(user)
        response = self.client.post('/', data={'interests': ['Django', 'Testing']})
        self.assertContains(response, user.first_name, )
        self.assertContains(response, user2.first_name, )

    def test_POST_returns_nothing_if_no_match(self):
        user = UserFactory()
        interest = InterestFactory(name="Django")
        user.interests.add(interest)
        self.client.force_login(user)
        response = self.client.post('/', data={'interests': 'Hola'})
        self.assertNotContains(response, user.first_name, )


class LoginTest(TestCase):
    def test_login_view_is_loaded_correctly(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)

    def test_login_redirects_to_homepage_if_succeed(self):
        user = UserFactory()
        response = self.client.post("/accounts/login/", data={'username': user.email, 'password': 'pass'})
        self.assertRedirects(response, '/')
        self.assertIn('_auth_user_id', self.client.session)

    def test_login_renders_login_template(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'login.html')
