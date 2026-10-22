from django.db import models

# Create your models here.
#schema name=Questions
#fields:-title,language,difficulty-level,notes,topic,published_date,sample input,sample output,is_active

class Questions(models.Model):
    title=models.CharField(max_length=200)
    language_choice=(
        ("python","python"),
        ("java","java"),
        ("js","js")
    )
    language=models.CharField(max_length=100,choices=language_choice,default='python')
    DIFFICULTY_LEVEL=(
        ("easy","easy"),
        ("medium","medium"),
        ("hard","hard")
    )
    difficulty_level=models.CharField(max_length=200,choices=DIFFICULTY_LEVEL,default='easy')
    notes=models.TextField(null=True)
    topic=models.CharField(max_length=200)
    published_date=models.DateTimeField(auto_now_add=True)
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_active=models.BooleanField(default=True)

class submission(models.Model):
    answer=models.TextField()
    question_id=models.IntegerField()
    points=models.PositiveIntegerField(null=True)
    owner=models.CharField(max_length=100)
    Submission_date=models.DateTimeField(auto_now_add=True)
    remarks=models.TextField(null=True)