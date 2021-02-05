
import requests
import unittest

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:5000'
        self.movies = '/movies'
        self.categories = '/categories'
        self.put = '/1'
        self.delete = '/2'

    def test_get(self):
        # GET -> 2
        req = requests.get(self.url+self.movies)
        self.assertEqual(req.status_code , 200)
        req = requests.get(self.url+self.categories)
        self.assertEqual(req.status_code , 200)

    def test_post(self):
        # POST -> 3
        data = {
            'title' : 'Peppermint',
            'image' : '',
            'rating' : 8.2,
            'category' : 'Action'
        }
        req = requests.post(self.url+self.movies,data=data)
        self.assertEqual(req.status_code , 201)
        data = {
            'title' : 'Friends',
            'image' : 'friends.jpg',
            'rating' : 9,
            'category' : 'Comedy'
        }
        req = requests.post(self.url+self.movies,data=data)
        self.assertEqual(req.status_code , 201)
        data = {
            'name' : 'Romance'
        }
        req = requests.post(self.url+self.categories,data=data)
        self.assertEqual(req.status_code , 201)

    def test_put(self):
        # PUT -> 2
        data = {
            'title' : 'Put',
            'image' : 'put.png',
            'rating' : 8.2,
            'category' : 'Action'
        }
        req = requests.put(self.url+self.movies+self.put,data=data)
        self.assertEqual(req.status_code , 200)
        data = {
            'name' : 'new_category',
        }
        req = requests.put(self.url+self.categories+self.put,data=data)
        self.assertEqual(req.status_code , 200)

    def test_delete(self):
        # DELETE -> 4
        req = requests.delete(self.url+self.movies+self.delete)
        self.assertEqual(req.status_code , 204)
        req = requests.delete(self.url+self.categories+self.delete)
        self.assertEqual(req.status_code , 204)
        req = requests.delete(self.url+self.movies)
        self.assertEqual(req.status_code , 204)
        req = requests.delete(self.url+self.categories)
        self.assertEqual(req.status_code , 204)

if __name__ == '__main__':
    unittest.main()

