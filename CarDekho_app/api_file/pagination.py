from rest_framework.pagination import PageNumberPagination
class ReviewListPagination(PageNumberPagination):
  page_size = 2
  