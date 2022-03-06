from nturl2path import url2pathname
from urllib import response
import requests

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from testproject.settings import IMDB_API_KEY, IMDB_API_URL


def get_top_250_movies():
    method = 'Top250Movies/'
    url = IMDB_API_URL + method + IMDB_API_KEY
    response_data = requests.get(url)
    return response_data.json()


def get_list_movie(q):
    method = 'SearchMovie/'
    url = IMDB_API_URL + method + IMDB_API_KEY +f'/{q}'
    response_data = requests.get(url)
    return response_data.json()


@api_view(['GET'])
def search_movies(request):
    method = 'SearchMovie/'
    search_text = request.GET.get('search_text')
    response_data = get_list_movie(search_text)
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def top_250(request):
    top_movies = get_top_250_movies()
    data = top_movies['items']
    year = request.GET.get('year')

    if year:
        data = [m for m in data if int(m['year']) >= int(year)]
 
    return Response(data, status=status.HTTP_200_OK)


