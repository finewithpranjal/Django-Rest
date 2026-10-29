from rest_framework.pagination import LimitOffsetPagination

class StudentOffSetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'l' 
    offset_query_param = 'o'
    # Replace the default limit and offset query parameter names with 'l' and 'o' respectively.

# http://127.0.0.1:8000/api/?limit=6&offset=10 use limit for how much data you wnat in a page and offset for data after the offset number if you entered offset = 10 so u will get data from 11 to the rest 