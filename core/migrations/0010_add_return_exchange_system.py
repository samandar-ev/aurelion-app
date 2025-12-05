
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_product_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='parent_order',
            field=models.ForeignKey(blank=True, help_text='For RETURN/EXCHANGE orders, this points to the original SALE order', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child_orders', to='core.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('SALE', 'Sale'), ('RETURN', 'Return'), ('EXCHANGE', 'Exchange')], db_index=True, default='SALE', max_length=20),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='qty_returned',
            field=models.PositiveIntegerField(default=0, help_text='Total quantity returned or exchanged from this line item'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('CANCELLED', 'Cancelled'), ('COMPLETED', 'Completed'), ('PARTIALLY_RETURNED', 'Partially Returned'), ('FULLY_RETURNED', 'Fully Returned'), ('REFUNDED', 'Refunded'), ('REFUND_PENDING', 'Refund Pending')], default='DRAFT', max_length=25),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.CheckConstraint(condition=models.Q(('qty_returned__lte', models.F('quantity'))), name='qty_returned_lte_quantity'),
        ),
    ]
