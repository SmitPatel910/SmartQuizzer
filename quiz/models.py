from django.db import models
from student.models import Student

class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   exam_date = models.DateField(null=True)
   exam_time = models.TimeField(null=True)
   exam_end_time = models.TimeField(null=True)

   status = [
        ("Upcoming", "Upcoming"),
    ]
   quiz_status = models.CharField(
        max_length=12,
        choices=status,
        default="Upcoming",
    )
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    que_pic= models.ImageField(upload_to="Quiz/",null=True,blank=True)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200,blank=True)
    option4=models.CharField(max_length=200,blank=True)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
    
    

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

