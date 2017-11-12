from django.contrib import admin
from idfams.models import JobType, Rte, Rwe, FamilyMember, IdFams

@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(Rte)
class RteAdmin(admin.ModelAdmin):
	pass

@admin.register(Rwe)
class RweAdmin(admin.ModelAdmin):
	pass

@admin.register(IdFams)
class IdFamsAdmin(admin.ModelAdmin):
	pass

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
	pass
# Register your models here.
