from django.contrib import admin
from .models import Question, GroupQuestions, Answers
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answers


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

    class Meta:
        model = Question


class GroupQuestionsAdmin(admin.ModelAdmin):

    class Meta:
        model = GroupQuestions


admin.site.register(Question, QuestionAdmin)
admin.site.register(GroupQuestions, GroupQuestionsAdmin)