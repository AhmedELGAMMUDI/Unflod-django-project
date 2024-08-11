from django.contrib import admin
from .models import Entity,Advance, Grant, PaymentVoucher, ReconciliationMemo, Deposit, Withdrawal, OutstandingItem, DepositDiscrepancy
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User,Group

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Advance)
class AdvanceAdmin(ModelAdmin):
    list_display = ('advance_number', 'date', 'amount', 'recipient', 'approved_by')
    list_display_links = ('advance_number',)
    search_fields = ('advance_number', 'recipient')

    class Meta:
        verbose_name = "سلفة"
        verbose_name_plural = "السلف"

@admin.register(Grant)
class GrantAdmin(ModelAdmin):
    list_display = ('grant_number', 'date', 'amount', 'recipient', 'approved_by')
    list_display_links = ('grant_number',)
    search_fields = ('grant_number', 'recipient')

    class Meta:
        verbose_name = "إعانة"
        verbose_name_plural = "الإعانات"


@admin.register(PaymentVoucher)
class PaymentVoucherAdmin(ModelAdmin):
    list_display = ('voucher_number', 'date', 'amount', 'payee', 'approved_by')
    list_display_links = ('voucher_number',)
    search_fields = ('voucher_number', 'payee')

    def get_queryset(self, request):
        return super().get_queryset(request).defer('description')

    class Meta:
        verbose_name = "إذن صرف"
        verbose_name_plural = "إذونات الصرف"


@admin.register(ReconciliationMemo)
class ReconciliationMemoAdmin(ModelAdmin):
    list_display = ('memo_number', 'date', 'account', 'total_amount')

    class Meta:
        verbose_name = "مذكرة تسوية"
        verbose_name_plural = "مذكرات التسوية"


@admin.register(Deposit)
class DepositAdmin(ModelAdmin):
    list_display = ('deposit_number', 'date', 'amount', 'account')

    class Meta:
        verbose_name = "إيداع"
        verbose_name_plural = "الإيداعات"


@admin.register(Withdrawal)
class WithdrawalAdmin(ModelAdmin):
    list_display = ('withdrawal_number', 'date', 'amount', 'account')

    class Meta:
        verbose_name = "مسحوب"
        verbose_name_plural = "المسحوبات"


@admin.register(OutstandingItem)
class OutstandingItemAdmin(ModelAdmin):
    list_display = ('item_type', 'item_number', 'amount', 'status', 'date')

    class Meta:
        verbose_name = "عنصر معلق"
        verbose_name_plural = "العناصر المعلقة"


@admin.register(DepositDiscrepancy)
class DepositDiscrepancyAdmin(ModelAdmin):
    list_display = ('discrepancy_number', 'deposit', 'recorded_amount', 'actual_amount', 'resolved')

    class Meta:
        verbose_name = "فرق الإيداع"
        verbose_name_plural = "فروق الإيداعات"

@admin.register(Entity)
class EntityAdmin(ModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name = "الجهات التابعة"
        verbose_name_plural = "الجهات التابعة"
