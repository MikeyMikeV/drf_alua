from django.db import models

GENRE = (
    ('Rock','Rock'),
    ('Jazz','Jazz'),
    ('Pop','Pop'),
    ('Ambience','Ambience'),
    ('Classical','Classical'),
)

class Music(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='music_files', max_length=100, null=True)
    desc = models.TextField()
    cover = models.ImageField(upload_to="music_covers")
    author = models.CharField(max_length=50)
    time = models.DurationField()
    genre =  models.CharField(choices=GENRE, default = 0, max_length=50)

    def __str__(self) -> str:
        return f"{self.author} - {self.title}"