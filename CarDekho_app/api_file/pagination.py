from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
class ReviewListPagination(PageNumberPagination):
  page_size = 2
  page_query_param = 'pa'
  page_size_query_param = 'record'
  max_page_size = 2
  last_page_strings = 'last'

class ReviewListLimitOffPage(LimitOffsetPagination):
  default_limit = 5
  max_limit = 3
  offset_query_param = 'start'
  limit_query_param = 'limitsss'  
  