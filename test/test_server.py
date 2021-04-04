import unittest
import requests

unittest.TestLoader.sortTestMethodsUsing = None

HOST = 'localhost'
PORT = '8080'

class ServerTest(unittest.TestCase):
    sample_shoe = {
        'size': 30,
        'shoes_type': 'SPORT',
        'manufacturer': 'abibas',
        'model': 'air'
    }

    def test_step1_create(self):
        response = requests.post(f'http://{HOST}:{PORT}/shoe', json=ServerTest.sample_shoe)
        self.assertEqual(response.status_code, 200)
        ServerTest.sample_shoe = response.json()

    def test_step2_get_all(self):
        response = requests.get(f'http://{HOST}:{PORT}/shoe')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json() != [])

    def test_step3_get_shoe(self):
        response = requests.get(f'http://{HOST}:{PORT}/shoe/' + str(ServerTest.sample_shoe['id']))
        self.assertEqual(response.status_code, 200)
        for key, val in response.json().items():
            if key not in ServerTest.sample_shoe or ServerTest.sample_shoe[key] != val:
                self.assertTrue(False, f'\'{key}\' from response does not match with stored record')

    def test_step4_update_shoe(self):
        ServerTest.sample_shoe['size'] = 50
        response = requests.put(f'http://{HOST}:{PORT}/shoe/' + str(ServerTest.sample_shoe['id']), json=ServerTest.sample_shoe)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['size'], 50)

    def test_step5_delete_shoe(self):
        response = requests.delete(f'http://{HOST}:{PORT}/shoe/' + str(ServerTest.sample_shoe['id']))
        self.assertEqual(response.status_code, 200)
        response = requests.delete(f'http://{HOST}:{PORT}/shoe/' + str(ServerTest.sample_shoe['id']))
        self.assertEqual(response.status_code, 404)

