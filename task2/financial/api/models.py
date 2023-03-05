from django.db import models
from django.contrib import admin

class financial_data(models.Model):
	symbol = models.CharField(max_length = 30) 
	date = models.CharField(max_length = 30)
	open_price = models.CharField(max_length = 30)
	close_price = models.CharField(max_length = 30) 
	volume = models.CharField(max_length = 30) 

    # 覆寫 __str__
	def __str__(self):
		return self.symbol
	
# 新增
class ApiAdmin(admin.ModelAdmin):
	list_display = ('id', 'symbol') 