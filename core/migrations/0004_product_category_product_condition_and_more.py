
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_product_brand_alter_product_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Bags', 'Bags'), ('Shoes', 'Shoes'), ('Accessories', 'Accessories'), ('Clothing', 'Clothing'), ('Jewelry', 'Jewelry'), ('Watches', 'Watches'), ('Eyewear', 'Eyewear'), ('Fragrance', 'Fragrance')], default='Accessories', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Display', 'Display'), ('Vintage', 'Vintage'), ('Like New', 'Like New')], default='New', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='country_of_origin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='display_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='has_box',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_care_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_dust_bag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_extras',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='has_warranty_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='internal_tags',
            field=models.TextField(blank=True, help_text='Comma-separated tags'),
        ),
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='packaging_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='release_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_product_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='authentication_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('UZS', 'UZS')], default='USD', max_length=3),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='edition_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='hardware_type',
            field=models.CharField(blank=True, choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Palladium', 'Palladium'), ('Rose Gold', 'Rose Gold'), ('Ruthenium', 'Ruthenium'), ('Brass', 'Brass'), ('None', 'None')], max_length=50),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='initial_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='minimum_stock_level',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='storage_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.location'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='serial_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/gallery/')),
                ('is_primary', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='core.product')),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
    ]
