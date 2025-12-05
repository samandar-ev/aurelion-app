
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_order_order_code_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(choices=[('CHANGED_MIND', 'Changed my mind'), ('DEFECTIVE', 'Defective / Damaged'), ('WRONG_SIZE', 'Wrong size'), ('WRONG_ITEM', 'Wrong item delivered'), ('OTHER', 'Other')], default='OTHER', max_length=50)),
                ('action', models.CharField(choices=[('REFUND', 'Refund'), ('EXCHANGE', 'Exchange')], default='REFUND', max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('original_order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='returns', to='core.order')),
                ('refund_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='refund_source', to='core.order')),
                ('replacement_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replacement_source', to='core.order')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('reason', models.CharField(blank=True, choices=[('CHANGED_MIND', 'Changed my mind'), ('DEFECTIVE', 'Defective / Damaged'), ('WRONG_SIZE', 'Wrong size'), ('WRONG_ITEM', 'Wrong item delivered'), ('OTHER', 'Other')], max_length=50, null=True)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.orderitem')),
                ('return_process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.return')),
            ],
        ),
    ]
