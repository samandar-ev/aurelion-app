
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_category_product_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='packaging_condition',
            field=models.CharField(blank=True, choices=[('Pristine', 'Pristine / Like New'), ('Complete', 'Complete - Minor Wear'), ('Partial', 'Partial - Missing Components'), ('Worn', 'Worn / Damaged')], max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='provenance_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='variant_material',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
