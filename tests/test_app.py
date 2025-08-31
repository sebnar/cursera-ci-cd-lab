import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        response = self.app.get('/')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertIn('message', data)

    def test_health_endpoint(self):
        response = self.app.get('/health')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'ci-cd-app')

    def test_get_data_endpoint(self):
        response = self.app.get('/api/data')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', data)
        self.assertIsInstance(data['data'], list)

    def test_create_data_endpoint(self):
        test_data = {'name': 'Test Item', 'description': 'Test Description'}
        response = self.app.post('/api/data',
                               data=json.dumps(test_data),
                               content_type='application/json')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Data created successfully')
        self.assertEqual(data['data'], test_data)

if __name__ == '__main__':
    unittest.main() 