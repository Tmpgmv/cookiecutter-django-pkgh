{% if cookiecutter.tests_required %}
from "{{ cookiecutter.project_slug }}".cookiecutter_const import PROJECT_NAME_RUS
from django.test import TestCase
from django.urls import reverse

{% if cookiecutter.custom_user %}
from accounts.models import User
{% else %}
from django.contrib.auth.models import User
{% endif %}

class HomePageTest(TestCase):
    def setUp(self):
        {% if cookiecutter.login_required %}
        self.user = User.objects.create_user(username='testuser', password='testpass')
        {% endif %}

    def test_home_page_contains_project_name(self):
        """
        На страницу home присутствует ли название проекта?
        """
        {% if cookiecutter.login_required %}
        self.client.login(username='testuser', password='testpass')
        {% endif %}
        response = self.client.get(reverse('home'))
        html = response.content.decode("utf8")
        self.assertIn(PROJECT_NAME_RUS, html)

    def test_user_can_be_created(self):
        """
        Если программно сохранить в БД нового пользователя,
        он должен присутствовать в БД. Так ли это?
        """
        User.objects.create_user(username='foo', password='bar')
        selected_user = bool(User.objects.filter(username='foo'))
        self.assertEqual(selected_user, True)

class SeleniumHomePageTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='selenium_user', password='selenium_pass')
        self.selenium.get(self.live_server_url + reverse("login"))
        username_field = self.selenium.find_element(By.ID, "username")
        password_field = self.selenium.find_element(By.ID, "password")
        username_field.send_keys('selenium_user')
        password_field.send_keys('selenium_pass')
        password_field.send_keys(Keys.RETURN)
        WebDriverWait(self.selenium, 10).until(
            lambda driver: "login" not in driver.current_url
        )

    def test_logo_exists_on_home(self):
        """
        На странице home присутствует логотип. Так ли это?
        """
        self.selenium.get(self.live_server_url + reverse('home'))
        logo = self.selenium.find_element(By.ID, "logo")
        self.assertTrue(logo.is_displayed())
{% endif %}
