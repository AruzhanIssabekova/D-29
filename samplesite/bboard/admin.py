from django.contrib import admin
from .models import Book, Reader, Reading, Author

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Reading)