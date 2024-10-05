# Django Libraries
from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom Libraries
from core.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="이름")
    contact = models.CharField(max_length=50, blank=True, null=True, verbose_name="연락처")
    email = models.EmailField(max_length=50, unique=True, verbose_name="이메일")
    profile_image = models.ImageField(upload_to="profile_images", blank=True, null=True, verbose_name="프로필 이미지")
    birthdate = models.DateField(blank=True, null=True, verbose_name="생년월일")
    team = models.ForeignKey("Team", on_delete=models.CASCADE, blank=True, null=True, verbose_name="팀")
    permission = models.CharField(max_length=50, default="user", verbose_name="권한")
    position = models.CharField(max_length=50, blank=True, null=True, verbose_name="직책")
    role = models.CharField(max_length=50, blank=True, null=True, verbose_name="역할")
    

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
        
    def __str__(self):
        return f"{self.name} - {self.team} - {self.position}"
    

class Team(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name="팀명")
    team_image = models.ImageField(upload_to="team_images", blank=True, null=True, verbose_name="팀 이미지")
    leader = models.ForeignKey("User", on_delete=models.CASCADE, related_name="leader", verbose_name="팀장")
    members = models.ManyToManyField("User", related_name="members", verbose_name="팀원")
    
    class Meta:
        db_table = "teams"
        ordering = ["-created_at"]
        verbose_name = "팀"
        verbose_name_plural = "팀"
        
    def __str__(self):
        return f"{self.name} - {self.leader}"
