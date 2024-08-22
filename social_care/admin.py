from django.contrib import admin
from .models import Entity,Advance, Grant, PaymentVoucher, ReconciliationMemo, Deposit, Withdrawal, OutstandingItem, DepositDiscrepancy,UnregisteredBond,UnlistedBond
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User,Group
from unfold.admin import TabularInline
from admin_object_actions.admin import ModelAdminObjectActionsMixin
# from admin_object_actions.admin import ObjectActionsMixin

from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from unfold.contrib.filters.admin import (
    RangeDateFilter,
    RangeDateTimeFilter,
)
# from weasyprint import HTML

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Advance)
class AdvanceAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('advance_number', 'date', 'amount', 'recipient', 'approved_by')
    list_display_links = ('advance_number',)
    search_fields = ('advance_number', 'recipient')
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("date", RangeDateFilter),  # Date filter
    )

    class Meta:
        verbose_name = "سلفة"
        verbose_name_plural = "السلف"

@admin.register(Grant)
class GrantAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('grant_number', 'date', 'amount', 'recipient', 'approved_by')
    list_display_links = ('grant_number',)
    search_fields = ('grant_number', 'recipient')
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("date", RangeDateFilter),  # Date filter
    )
    class Meta:
        verbose_name = "إعانة"
        verbose_name_plural = "الإعانات"


@admin.register(PaymentVoucher)
class PaymentVoucherAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('voucher_number', 'date', 'amount', 'payee', 'approved_by')
    list_display_links = ('voucher_number',)
    search_fields = ('voucher_number', 'payee')
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("date", RangeDateFilter),  # Date filter
    )
    def get_queryset(self, request):
        return super().get_queryset(request).defer('description')

    class Meta:
        verbose_name = "إذن صرف"
        verbose_name_plural = "إذونات الصرف"





@admin.register(Deposit)
class DepositAdmin(ModelAdmin, ImportExportModelAdmin,ModelAdminObjectActionsMixin):
    list_display = ('deposit_number', 'date', 'amount', 'account')
    search_fields = ('deposit_number', 'date', 'amount', 'account')
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("date", RangeDateFilter),  # Date filter
    )

    
    
    class Meta:
        verbose_name = "إيداع"
        verbose_name_plural = "الإيداعات"


@admin.register(Withdrawal)
class WithdrawalAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('withdrawal_number', 'date', 'amount', 'account')
    search_fields = ('withdrawal_number', 'date', 'amount', 'account')
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("date", RangeDateFilter),  # Date filter
    )
    class Meta:
        verbose_name = "مسحوب"
        verbose_name_plural = "المسحوبات"


@admin.register(OutstandingItem)
class OutstandingItemAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('item_type', 'item_number', 'amount', 'status', 'date')
    search_fields = ('item_type', 'item_number', 'amount', 'status', 'date')
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("date", RangeDateFilter),  # Date filter
    )
    class Meta:
        verbose_name = "عنصر معلق"
        verbose_name_plural = "العناصر المعلقة"


@admin.register(DepositDiscrepancy)
class DepositDiscrepancyAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('discrepancy_number',  'recorded_amount', 'actual_amount', 'resolved')
    search_fields = ('discrepancy_number',  'recorded_amount', 'actual_amount', 'resolved')
    class Meta:
        verbose_name = "فرق الإيداع"
        verbose_name_plural = "فروق الإيداعات"

@admin.register(Entity)
class EntityAdmin(ModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name = "الجهات التابعة"
        verbose_name_plural = "الجهات التابعة"



class DepositInline(TabularInline):
    model = Deposit
    extra = 1

class WithdrawalInline(TabularInline):
    model = Withdrawal
    extra = 1

class OutstandingItemInline(TabularInline):
    model = OutstandingItem
    extra = 1


class DepositDiscrepancyInline(TabularInline):
    model = DepositDiscrepancy
    extra = 1

class UnregisteredBondInline(TabularInline):
    model = UnregisteredBond
    extra = 1

class UnlistedBondInline(TabularInline):
    model = UnlistedBond
    extra = 1


@admin.register(ReconciliationMemo)
class ReconciliationMemoAdmin(ModelAdmin):
    # list_display = '__all__'
    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = (
        ("date", RangeDateFilter),  # Date filter
    )
    inlines = [DepositInline, WithdrawalInline, OutstandingItemInline, DepositDiscrepancyInline,UnregisteredBondInline,UnlistedBondInline]
    class Meta:
        verbose_name = "مذكرة تسوية"
        verbose_name_plural = "مذكرات التسوية"