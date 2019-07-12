import os
import unittest 
import boto3

from app import application

class AllTests(unittest.TestCase):
	# executed prior to each test
	def setUp(self):
		application.config['TESTING'] = True
		self.application = application.test_client()

	# check if the landing page returns expected contents
	def test_home_page_contents(self):
		response = self.application.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Sign up', response.data)


if __name__ == '__main__':
	unittest.main()