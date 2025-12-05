
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='loyalty_tier',
            field=models.CharField(blank=True, choices=[('REGULAR', 'Regular'), ('SILVER', 'Silver'), ('GOLD', 'Gold'), ('PLATINUM', 'Platinum')], default='REGULAR', max_length=20),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(blank=True, help_text='Optional promo code', max_length=50, null=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('promo_type', models.CharField(choices=[('PERCENTAGE', 'Percentage Off'), ('FIXED', 'Fixed Amount Off'), ('BOGO', 'Buy X Get Y Free'), ('TIERED', 'Tier-Based Discount'), ('BUNDLE', 'Bundle Discount')], default='PERCENTAGE', max_length=20)),
                ('discount_value', models.DecimalField(decimal_places=2, default=0, help_text='Percentage (0-100) or fixed amount', max_digits=10)),
                ('buy_quantity', models.PositiveIntegerField(default=2, help_text='Buy X items...')),
                ('get_quantity', models.PositiveIntegerField(default=1, help_text='...get Y free (cheapest item)')),
                ('silver_discount', models.DecimalField(decimal_places=2, default=5, max_digits=5)),
                ('gold_discount', models.DecimalField(decimal_places=2, default=10, max_digits=5)),
                ('platinum_discount', models.DecimalField(decimal_places=2, default=15, max_digits=5)),
                ('applies_to', models.CharField(choices=[('ALL', 'All Products'), ('CATEGORY', 'Specific Category'), ('BRAND', 'Specific Brand'), ('PRODUCTS', 'Selected Products')], default='ALL', max_length=20)),
                ('category', models.CharField(blank=True, choices=[('Bags', 'Bags'), ('Shoes', 'Shoes'), ('Accessories', 'Accessories'), ('Clothing', 'Clothing'), ('Jewelry', 'Jewelry'), ('Watches', 'Watches'), ('Eyewear', 'Eyewear'), ('Fragrance', 'Fragrance')], max_length=50)),
                ('brand', models.CharField(blank=True, max_length=100)),
                ('customer_tier', models.CharField(choices=[('ALL', 'All Customers'), ('SILVER', 'Silver & Above'), ('GOLD', 'Gold & Above'), ('PLATINUM', 'Platinum Only')], default='ALL', max_length=20)),
                ('min_purchase', models.DecimalField(decimal_places=2, default=0, help_text='Minimum cart value to apply', max_digits=10)),
                ('min_items', models.PositiveIntegerField(default=0, help_text='Minimum items in cart')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('max_uses', models.PositiveIntegerField(default=0, help_text='0 = unlimited')),
                ('used_count', models.PositiveIntegerField(default=0)),
                ('max_uses_per_customer', models.PositiveIntegerField(default=0, help_text='0 = unlimited')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PromotionUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('used_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='core.promotion')),
            ],
        ),
        migrations.CreateModel(
            name='PromotionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='core.product')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_links', to='core.promotion')),
            ],
            options={
                'unique_together': {('promotion', 'product')},
            },
        ),
    ]
