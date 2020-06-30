# python manage.py shell
"""
from django.test.utils import setup_test_environment
setup_test_environment()
"""

from django.test import TestCase
from django.urls import reverse


class ViewsTests(TestCase):

    def test_index_response_status_code(self):
        response = self.client.get('/')
        # Not Found: /
        # we should expect a 404 from that address; if you instead see an
        # "Invalid HTTP_HOST header" error and a 400 response, you probably
        # omitted the setup_test_environment() call described earlier.
        self.assertEqual(response.status_code, 404)

    def test_polls_response_status_code(self):
        # on the other hand we should expect to find something at '/polls/'
        # we'll use 'reverse()' rather than a hardcoded URL
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        # 200

# response.content
# b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'

# response.context['latest_question_list']
# <QuerySet [<Question: What's up?>]>
