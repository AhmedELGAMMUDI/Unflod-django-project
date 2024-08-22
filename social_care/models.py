from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الجهة")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "الجهات التابعة"
        verbose_name_plural = "الجهات التابعة"

        
class Advance(models.Model):
    advance_number = models.CharField(max_length=50, unique=True, verbose_name="رقم السلفة")
    date = models.DateField(verbose_name="التاريخ")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    recipient = models.CharField(max_length=255, verbose_name="المستفيد")
    recipient_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name="الجهة تابع لها - المستفيد" ,related_name='recipient')
    recipient_id = models.CharField(max_length=255, verbose_name="المستفيد - رقم الوطني")
    guarantor = models.CharField(max_length=255, verbose_name="الضامن",unique=True)
    guarantor_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name="الجهة تابع لها - الضامن",related_name='guarantor')
    guarantor_id = models.CharField(max_length=255, verbose_name="الضامن - رقم الوطني",unique=True)
    purpose = models.TextField(verbose_name="الغرض")
    approved_by = models.CharField(max_length=255, blank=True, null=True, verbose_name="المعتمد")

    def __str__(self):
        return f"Advance {self.advance_number} - {self.amount} {self.recipient}"

    class Meta:
        verbose_name = "سلفة"
        verbose_name_plural = "السلف"

class Grant(models.Model):
    grant_number = models.CharField(max_length=50, unique=True, verbose_name="رقم الإعانة")
    date = models.DateField(verbose_name="التاريخ")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    recipient = models.CharField(max_length=255, verbose_name="المستفيد")
    recipient_entity = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name="الجهة تابع لها - المستفيد" ,related_name='recipient_id')
    recipient_id = models.CharField(max_length=255, verbose_name="رقم الوطني للمستفيد")
    purpose = models.TextField(verbose_name="الغرض")
    approved_by = models.CharField(max_length=255, blank=True, null=True, verbose_name="المعتمد")

    def __str__(self):
        return f"Grant {self.grant_number} - {self.amount} {self.recipient}"

    class Meta:
        verbose_name = "إعانة"
        verbose_name_plural = "الإعانات"




class PaymentVoucher(models.Model):
    voucher_number = models.CharField(max_length=20, verbose_name="رقم الإذن")
    date = models.DateField(verbose_name="التاريخ")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    payee = models.CharField(max_length=100, verbose_name="المستفيد")
    description = models.TextField()
    approved_by = models.CharField(max_length=100, verbose_name="المعتمد")

    class Meta:
        verbose_name = "إذن صرف"
        verbose_name_plural = "إذونات الصرف"

class ReconciliationMemo(models.Model):
    memo_number = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name="رقم المذكرة"
    )
    date = models.DateField(
        verbose_name="التاريخ"
    )
    account = models.CharField(
        max_length=255, 
        verbose_name="الحساب"
    )

    # Balances
    beginning_balance = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="رصيد دفتر بداية الشهر"
    )
    deposits_during_month = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="الإيداع خلال الشهر"
    )
    withdrawals_during_month = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="المسحوبات خلال الشهر"
    )
    ending_balance = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="رصيد دفتر نهاية الشهر"
    )

    # Reconciliation with bank statement
    statement_balance = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="رصيد كشف حساب"
    )
    # checks_not_recorded = models.DecimalField(
    #     max_digits=10, 
    #     decimal_places=2, 
    #     default=0.00, 
    #     verbose_name="صكوك لم تسجل في الدفتر"
    # )
    # checks_not_cleared = models.DecimalField(
    #     max_digits=10, 
    #     decimal_places=2, 
    #     default=0.00, 
    #     verbose_name="صكوك لم تظهر"
    # )
    unrecorded_revenues = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="إيرادات لم تسجل في الدفتر"
    )
    additional_bank_entries = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="إضافة مبالغ في كشف الحساب"
    )

    # Differences
    withdrawal_discrepancies = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="فروقات سحب"
    )
    deposit_discrepancies = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="فروقات إيداع"
    )

    # Final reconciled balance
    reconciled_balance = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="الرصيد الدفتري بعد التسوية"
    )

    def __str__(self):
        return f"Reconciliation Memo {self.memo_number} - {self.account} - {self.date}"


    class Meta:
        verbose_name = "مذكرة تسوية"
        verbose_name_plural = "مذكرات التسوية"

class Deposit(models.Model):
    deposit_number = models.CharField(max_length=50, unique=True, verbose_name="رقم الإيداع")
    date = models.DateField(verbose_name="التاريخ")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    account = models.CharField(max_length=255, verbose_name="الحساب")
    description = models.TextField(verbose_name="الوصف")
    reconciliation_memo = models.ForeignKey(
        ReconciliationMemo, 
        on_delete=models.CASCADE, 
        related_name='deposits', 
        verbose_name="مذكرة التسوية",
        blank=True, 
        null=True,
        editable=False  # This hides the field from forms and admin
    )

    def __str__(self):
        return f"Deposit {self.deposit_number} - {self.amount}"

    class Meta:
        verbose_name = "إيداع"
        verbose_name_plural = "الإيداعات"

class Withdrawal(models.Model):
    withdrawal_number = models.CharField(max_length=50, unique=True, verbose_name="رقم المسحوب")
    date = models.DateField(verbose_name="التاريخ")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    account = models.CharField(max_length=255, verbose_name="الحساب")
    description = models.TextField(verbose_name="الوصف")
    reconciliation_memo = models.ForeignKey(
        ReconciliationMemo, 
        on_delete=models.CASCADE, 
        related_name='withdrawals', 
        verbose_name="مذكرة التسوية",
        blank=True, 
        null=True,
        editable=False  # This hides the field from forms and admin
    )

    def __str__(self):
        return f"Withdrawal {self.withdrawal_number} - {self.amount}"

    class Meta:
        verbose_name = "مسحوب"
        verbose_name_plural = "المسحوبات"

class OutstandingItem(models.Model):
    item_type = models.CharField(max_length=50, choices=[('Cheque', 'شيك'), ('Deposit', 'إيداع')], verbose_name="نوع العنصر")
    item_number = models.CharField(max_length=50, verbose_name="رقم العنصر")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    status = models.CharField(max_length=50, choices=[('Pending', 'معلق'), ('Cleared', 'تم تسويته')], verbose_name="الحالة")
    date = models.DateField(verbose_name="التاريخ")
    reconciliation_memo = models.ForeignKey(
        ReconciliationMemo, 
        on_delete=models.CASCADE, 
        related_name='outstanding_items', 
        verbose_name="مذكرة التسوية",
        blank=True, 
        null=True,
        editable=False  # This hides the field from forms and admin
        
    )

    def __str__(self):
        return f"Outstanding Item {self.item_number} - {self.amount} - {self.status}"

    class Meta:
        verbose_name = "عنصر معلق"
        verbose_name_plural = "العناصر المعلقة"

class DepositDiscrepancy(models.Model):
    discrepancy_number = models.CharField(max_length=50, unique=True, verbose_name="رقم الفرق")
    # deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, verbose_name="الإيداع")
    recorded_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ المسجل")
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ الفعلي")
    description = models.TextField(verbose_name="الوصف")
    resolved = models.BooleanField(default=False, verbose_name="تم التسوية")
    reconciliation_memo = models.ForeignKey(
        ReconciliationMemo, 
        on_delete=models.CASCADE, 
        related_name='deposit_discrepancy', 
        verbose_name="مذكرة التسوية",
        blank=True, 
        null=True,
        editable=False  # This hides the field from forms and admin
        
    )
    def __str__(self):
        return f"Discrepancy {self.discrepancy_number} - {self.recorded_amount} vs {self.actual_amount}"

    class Meta:
        verbose_name = "فرق الإيداع"
        verbose_name_plural = "فروق الإيداعات"



class UnregisteredBond(models.Model):
    bond_number = models.CharField("رقم الصك", max_length=100, unique=True)
    bond_date = models.DateField("تاريخ الصك")
    bond_value = models.DecimalField("قيمة الصك", max_digits=20, decimal_places=2)
    issuer = models.CharField("الجهة المصدرة", max_length=255)
    reason_not_registered = models.TextField("سبب عدم التسجيل", blank=True, null=True)
    notes = models.TextField("ملاحظات", blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإدخال", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    reconciliation_memo = models.ForeignKey(
        ReconciliationMemo, 
        on_delete=models.CASCADE, 
        related_name='unregistered_bond', 
        verbose_name="صك غير مسجل",
        blank=True, 
        null=True,
        editable=False  # This hides the field from forms and admin
        
    )
    class Meta:
        verbose_name = "صك غير مسجل"
        verbose_name_plural = "صكوك غير مسجلة"

    def __str__(self):
        return f"صك رقم {self.bond_number} - {self.issuer}"


class UnlistedBond(models.Model):
    bond_number = models.CharField("رقم الصك", max_length=100, unique=True)
    bond_date = models.DateField("تاريخ الصك")
    bond_value = models.DecimalField("قيمة الصك", max_digits=20, decimal_places=2)
    issuer = models.CharField("الجهة المصدرة", max_length=255)
    reason_not_listed = models.TextField("سبب عدم الظهور", blank=True, null=True)
    detected_on = models.DateField("تاريخ اكتشاف الصك", null=True, blank=True)
    notes = models.TextField("ملاحظات", blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإدخال", auto_now_add=True)
    updated_at = models.DateTimeField("تاريخ التحديث", auto_now=True)
    reconciliation_memo = models.ForeignKey(
        ReconciliationMemo, 
        on_delete=models.CASCADE, 
        related_name='unlisted_bond', 
        verbose_name="صك لم يظهر",
        blank=True, 
        null=True,
        editable=False  # This hides the field from forms and admin
        
    )
    class Meta:
        verbose_name = "صك لم يظهر"
        verbose_name_plural = "صكوك لم تظهر"

    def __str__(self):
        return f"صك رقم {self.bond_number} - {self.issuer}"