from rest_framework.pagination import CursorPagination

class StudentCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'


