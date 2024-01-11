import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_department_api(self):
        # Add a department
        department_data = {
            "department_id": "CSE",
            "department_name": "Computer Science and Engineering",
            "phone": "123-456-7890",
            "email": "cse@example.com",
            "courses": "CS101, CS102, CS103"
        }
        response = requests.post(f'{self.base_url}/department/add', json=department_data)
        self.assertEqual(response.status_code, 200)

        # Retrieve all departments
        response = requests.get(f'{self.base_url}/department')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Update the added department
        updated_data = {
            "department_id": "CSE",
            "department_name": "Updated Computer Science and Engineering",
            "phone": "987-654-3210",
            "email": "updated_cse@example.com",
            "courses": "CS201, CS202, CS203"
        }
        response = requests.put(f'{self.base_url}/department/CSE', json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Delete the added/updated department
        response = requests.delete(f'{self.base_url}/department/CSE')
        self.assertEqual(response.status_code, 200)

    def test_faculty_api(self):
        # Add a faculty
        faculty_data = {
            "faculty_id": "F101",
            "faculty_name": "John Doe",
            "department": "Computer Science and Engineering",
            "position": "Professor",
            "email": "john.doe@example.com"
        }
        response = requests.post(f'{self.base_url}/faculty', json=faculty_data)
        self.assertEqual(response.status_code, 201)

        # Retrieve all faculty
        response = requests.get(f'{self.base_url}/faculty')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Update the added faculty
        updated_data = {
            "faculty_id": "F101",
            "faculty_name": "Updated John Doe",
            "department": "Computer Science and Engineering",
            "position": "Associate Professor",
            "email": "updated_john.doe@example.com"
        }
        response = requests.put(f'{self.base_url}/faculty/F101', json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Delete the added/updated faculty
        response = requests.delete(f'{self.base_url}/faculty/F101')
        self.assertEqual(response.status_code, 200)

    def test_campus_api(self):
        # Add a campus
        campus_data = {
            "campus_id": "Campus1",
            "campus_name": "Main Campus",
            "location": "City Center",
            "established_date": "2022-01-01"
        }
        response = requests.post(f'{self.base_url}/campus', json=campus_data)
        self.assertEqual(response.status_code, 201)

        # Retrieve all campuses
        response = requests.get(f'{self.base_url}/campus')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Update the added campus
        updated_data = {
            "campus_id": "Campus1",
            "campus_name": "Updated Main Campus",
            "location": "Downtown",
            "established_date": "2023-01-01"
        }
        response = requests.put(f'{self.base_url}/campus/Campus1', json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Delete the added/updated campus
        response = requests.delete(f'{self.base_url}/campus/Campus1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()