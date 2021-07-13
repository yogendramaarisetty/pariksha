from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)

def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Challenge(models.Model):
    Slug = models.SlugField()
    Title = models.CharField(max_length=120)
    Description = models.TextField(max_length=5520)
    College = models.CharField(max_length=120)
    Date = models.CharField( blank =True,default="",max_length=20)
    Test_Duration = models.IntegerField(default=0)
    Active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.Title}'
    def is_active(self):
        return f'{self.Active}'

class Question(models.Model):
    Level = models.CharField(max_length=120,default="easy")
    Title = models.CharField(max_length=120)
    Type= models.CharField(max_length=120)
    Description = models.TextField()
    default_code={
        'java': "//NOTE: Don't change class name\npublic class MyClass {\n    public static void main(String args[]) {\n      System.out.println(\"\" );\n    }\n}\n",
        'python':"if __name__ == '__main__':\n",
        'csharp':"//Note don't change the class name \nusing System;\n\nclass Program\n{\n    static void Main() {\n        Console.Write(\"\");\n    }\n}\n",
        'cpp':"#include <iostream>\n\nusing namespace std;\n\nint main() {\n    \n    cout<<\"\";\n}\n",
        'c':"#include<stdio.h>\n\nint main() {\n    \n    printf(\"\");\n    \n}\n",
                }
    default_c_code = models.TextField(default=default_code['c'],max_length=1000000)
    default_cpp_code = models.TextField(default=default_code['cpp'],max_length=1000000)
    default_csharp_code = models.TextField(default=default_code['csharp'],max_length=1000000)
    default_java_code = models.TextField(default=default_code['java'],max_length=1000000)
    default_python_code = models.TextField(default=default_code['python'],max_length=1000000)


    def __str__(self):
        return f'{self.Title}'
    def get_absolute_url(self):
        return reverse('question_edit', kwargs={'q_id' :self.id})

class challenge_questions(models.Model):
    class Meta:
        unique_together = [['challenge','question'],]
    challenge = models.ForeignKey(Challenge,on_delete=models.CASCADE,null=True)
    question  = models.ForeignKey(Question,on_delete=models.CASCADE,null=True)

class demoCodes(models.Model):
    user =   models.OneToOneField(User,on_delete=models.CASCADE)
    default_code={
        'java': "//NOTE: Don't change class name\npublic class MyClass {\n    public static void main(String args[]) {\n      System.out.println(\"\" );\n    }\n}\n",
        'python':"if __name__ == '__main__':\n",
        'csharp':"//Note don't change the class name \nusing System;\n\nclass Program\n{\n    static void Main() {\n        Console.Write(\"\");\n    }\n}\n",
        'cpp':"#include <iostream>\n\nusing namespace std;\n\nint main() {\n    \n    cout<<\"\";\n}\n",
        'c':"#include<stdio.h>\n\nint main() {\n    \n    printf(\"\");\n    \n}\n",
            }
    c_code = models.TextField(default=default_code['c'],max_length=1000000)
    cpp_code = models.TextField(default=default_code['cpp'],max_length=1000000)
    csharp_code = models.TextField(default=default_code['csharp'],max_length=1000000)
    java_code = models.TextField(default=default_code['java'],max_length=1000000)
    python_code = models.TextField(default=default_code['python'],max_length=1000000)
    submitted_code = models.TextField(default="NA",max_length=1000000)
    score = models.IntegerField(default=0)  

class Candidate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    test_name = models.ForeignKey(Challenge,on_delete=models.CASCADE,null=True)
    fullname = models.CharField(default="",max_length=24)
    rollnumber = models.CharField(default="",max_length=20)
    college = models.CharField(default="",max_length=50)
    mobile_number = models.CharField(max_length=100)
    total_score = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    start_time = models.DateTimeField(blank=True,null=True,auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(blank=True,null=True,auto_now=False, auto_now_add=False)
    completed_status = models.BooleanField(default=False)
    suspicious_count = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.fullname} ({self.user.username})'

class Testcase(models.Model):
    Tinput = models.TextField()
    Toutput = models.TextField()

class Question_Testcase(models.Model):
    class Meta:
        unique_together = [['testcase','question'],]
    testcase = models.ForeignKey(Testcase,on_delete=models.SET_NULL,null=True)
    question  = models.ForeignKey(Question,on_delete=models.SET_NULL,null=True)
    score = models.IntegerField(default=0)
    description = models.TextField(null=True)

class Candidate_codes(models.Model):
    class Meta:
        unique_together = [['candidate','question'],]
    default_code={
        'java': "//NOTE: Don't change class name\npublic class MyClass {\n    public static void main(String args[]) {\n      System.out.println(\"\" );\n    }\n}\n",
        'python':"if __name__ == '__main__':\n",
        'csharp':"//Note don't change the class name \nusing System;\n\nclass Program\n{\n    static void Main() {\n        Console.Write(\"\");\n    }\n}\n",
        'cpp':"#include <iostream>\n\nusing namespace std;\n\nint main() {\n    \n    cout<<\"\";\n}\n",
        'c':"#include<stdio.h>\n\nint main() {\n    \n    printf(\"\");\n    \n}\n",
            }
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_code = models.TextField(default=default_code['c'],max_length=1000000)
    cpp_code = models.TextField(default=default_code['cpp'],max_length=1000000)
    csharp_code = models.TextField(default=default_code['csharp'],max_length=1000000)
    java_code = models.TextField(default=default_code['java'],max_length=1000000)
    python_code = models.TextField(default=default_code['python'],max_length=1000000)
    submitted_code = models.TextField(default="NA",max_length=1000000)
    submitted_code_language = models.TextField(default="NA",max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.candidate.fullname}  {self.question.Title}'

class Test_Feedback(models.Model):
    Candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0,max_length=5)
    description = models.TextField(default="")

