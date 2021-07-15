from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from import_export.admin import ExportActionMixin
from django.contrib.auth.models import User,Group
from . models import demoCodes, Challenge,Question,Candidate,Test_Feedback,Testcase,Candidate_codes,challenge_questions,Question_Testcase,Testcase,Submission
# Register your models here.
# admin.site.register(Challenge)
# admin.site.register(Question)
class contestQuestion(admin.ModelAdmin):
    list_display=('combine_contest_question','challenge','question')
    def combine_contest_question(self,obj):
        return "{}  - {} ".format(obj.challenge,obj.question)
admin.site.register(challenge_questions, contestQuestion)

class TestCasesAdmin(admin.ModelAdmin):
    list_display=('question','testcase','description','score')
    list_display_links = ('question',)
    list_filter = ('question','description','score')
    fieldsets = (
        (None, {
            "fields": (
                  'question','testcase','description','score',
            ),
        }),
    )
class ChallengeAdmin(admin.ModelAdmin):
    list_display=('Title','Slug','Test_Duration','combine_title_slug','College')
    list_display_links = ('Title',
                        'Slug')
    list_filter = ('Title',
    )
    fieldsets = (
        (None, {
            "fields": (
                  'Slug',
                  'Title',
                  'Description',
                  'Active',
                  'College',
                  'Date',
                  'Test_Duration',
            ),
        }),
    )
    def combine_title_slug(self,obj):
        return "{} - {}".format(obj.Title,obj.Slug)

admin.site.register(Challenge,ChallengeAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display=('Title','Level','Type','combine_title_slug')
    list_display_links = ('Title',
                        'Level')
    list_filter = ('Title', 'Type',
    )
    fieldsets = (
        (None, {
            "fields": (
                  'Slug',
                  'Title',
                  'Type',
                  'Description',
                  'sample_inputs',
                  'sample_outputs',
                  'default_c_code',
                  'default_cpp_code',
                  'default_csharp_code',
                  'default_java_code',
                  'default_python_code',
            ),
        }),
    )
    def combine_title_slug(self,obj):
        return "{} - {}".format(obj.Title,obj.Slug)
admin.site.register(Question,QuestionAdmin)

class InLineSubmittedcodes(admin.TabularInline):
    model = Candidate_codes
    extra = 0
class CandidateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    inlines = [InLineSubmittedcodes]
    list_filter = ('test_name','total_score','fullname')
    search_fields = ('fullname','test_name','total_score','rollnumber')
    list_display=(
        'fullname',
        'rollnumber',
        'test_name',
        'college',
        'mobile_number',
        'total_score',
        'completed_status',
        'suspicious_count',
    )
    fieldsets = (
        (None, {
            "fields": (
                  'user',
                  'test_name',
                  'fullname',
                  'rollnumber',
                  'college',
                  'mobile_number',
                  'total_score',
                  'start_time',
                  'end_time',
                  'completed_status',
                  'suspicious_count',
            ),
        }),
    )
    
class Candidate_codesAdmin(admin.ModelAdmin):
    list_filter = ('candidate','question')
    search_fields = ('candidate','question')
    list_display=(
        'candidate',
        'question',
    )

class SubmissionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_filter = ('challenge','candidate','question','language')
    list_display=(
        'challenge',
        'candidate',
        'question',
        'code',
        'language',
        'total_score'
    )

admin.site.register(Candidate,CandidateAdmin)
admin.site.register(Candidate_codes,Candidate_codesAdmin)
admin.site.register(Question_Testcase, TestCasesAdmin)
admin.site.register(Testcase)
admin.site.register(Test_Feedback)
admin.site.register(demoCodes)
admin.site.register(Submission,SubmissionAdmin)

