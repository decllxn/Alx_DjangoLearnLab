from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BookAPITests(APITestCase):
    
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        
        # Create some test books
        self.book1 = Book.objects.create(title='Book 1', author='Author 1', publication_year='2022')
        self.book2 = Book.objects.create(title='Book 2', author='Author 2', publication_year='2021')
        
        # Define the base URL
        self.list_url = reverse('book-list')

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_book(self):
        self.authenticate()
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': '2023'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_update_book(self):
        self.authenticate()
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': '2024'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        self.authenticate()
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        url = self.list_url + '?author=Author 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Book 1')

    def test_search_books(self):
        url = self.list_url + '?search=Book 1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Book 1')

    def test_ordering_books(self):
        url = self.list_url + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Book 2')  # Assuming Book 2 has an earlier year

