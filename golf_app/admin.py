from django.contrib import admin
from golf_app.models import * 

class ProfileAdmin(admin.ModelAdmin):
    pass

class RoundAdmin(admin.ModelAdmin):
    pass 

class CourseAdmin(admin.ModelAdmin):
    pass

class HoleAdmin(admin.ModelAdmin):
    pass

class ScoreAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Round, RoundAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Hole, HoleAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Profile, ProfileAdmin)

