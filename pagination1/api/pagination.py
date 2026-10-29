from rest_framework.pagination import PageNumberPagination

class StudentNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'  # page number query parameter replaces 'page' with 'p'
    page_size_query_param = 'size'  # user can decide how per page records he wants 
    max_page_size = 6 # maximum number of records per page
    # example = /api/?p=1&size=8, 
    # Use p=last for last page and if you want to replace 'last' with another string you can use the settings below.
    last_page_strings = 'end'  # replaced 'last', with 'end' you can use /api/?p=end&size=8 to get the last page records