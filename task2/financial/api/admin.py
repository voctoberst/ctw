from django.contrib import admin
from .models import financial_data, ApiAdmin


# 額外 import 這個套件
from django.utils.translation import gettext_lazy as _

# 自行宣告 類別
class start_date(admin.SimpleListFilter):

	title = _('start_date')
	parameter_name = 'start_date' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>=2023-02-21',_('>=2023-02-21')), # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
			
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>=2023-02-21':
			return queryset.filter(date__gte="2023-02-21")
		
		
# 自行宣告 類別
class end_date(admin.SimpleListFilter):

	title = _('end_date')
	parameter_name = 'end_date' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('<=2023-02-25',_('<=2023-02-25')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '<=2023-02-25':
			return queryset.filter(date__lte="2023-02-25")
		
    
# 自行宣告 類別
class symbol(admin.SimpleListFilter):


	title = _('symbol')
	parameter_name = 'symbol' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('=IBM',_('=IBM')), # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
			('=AAPL',_('=AAPL')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '=IBM':
			print("IBM")
			return queryset.filter(symbol="IBM")
		if self.value() == '=AAPL':
			print("AAPL")
			return queryset.filter(symbol="AAPL")
            

@admin.register(financial_data)
class FoodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in financial_data._meta.fields]
	list_filter = (start_date,end_date,symbol,)
