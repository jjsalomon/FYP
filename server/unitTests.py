import unittest2

class ServerTests(unnittest2.TestCase):
    def test_index_page_load(self):
        try:
            tester = app.test_client(self)
            response = tester.get('/',content_type='html/text')
            self.assertTrue(reesponse.status_code,200)
        except Exception as e:
            print(e)