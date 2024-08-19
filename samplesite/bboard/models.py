from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, through='Reading', related_name='readers')

    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'
        ordering = ['name']

    def __str__(self):
        return self.name

class Reading(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Reading'
        verbose_name_plural = 'Readings'
        ordering = ['start_date']
        unique_together = ('reader', 'book', 'start_date')

    def __str__(self):
        return f"{self.reader.name} reading {self.book.title}"
