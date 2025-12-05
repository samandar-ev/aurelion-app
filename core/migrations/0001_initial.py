
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('prefers_communication', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_active', models.BooleanField(default=True)),
                ('requires_manager_approval', models.BooleanField(default=False)),
                ('min_points_required', models.IntegerField(default=0)),
                ('applicable_to_tier', models.CharField(blank=True, choices=[('REGULAR', 'Regular'), ('VIP', 'VIP'), ('VVIP', 'VVIP'), ('STAFF', 'Staff')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
                ('is_store', models.BooleanField(default=True)),
                ('is_warehouse', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('collection', models.CharField(blank=True, max_length=100)),
                ('season', models.CharField(blank=True, max_length=50)),
                ('base_sku', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('material', models.CharField(blank=True, max_length=100)),
                ('is_limited_edition', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('OWNER', 'Owner'), ('MANAGER', 'Store Manager'), ('ASSOCIATE', 'Sales Associate'), ('STOCK', 'Stock Controller')], default='ASSOCIATE', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_balance', models.IntegerField(default=0)),
                ('tier', models.CharField(choices=[('REGULAR', 'Regular'), ('VIP', 'VIP'), ('VVIP', 'VVIP'), ('STAFF', 'Staff')], default='REGULAR', max_length=20)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loyalty_account', to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='DRAFT', max_length=20)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_discount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('loyalty_points_earned', models.IntegerField(default=0)),
                ('loyalty_points_redeemed', models.IntegerField(default=0)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.location')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.discountrule')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='core.order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=20)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='core.product')),
            ],
            options={
                'unique_together': {('product', 'color', 'size')},
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('line_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.order')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.productvariant')),
            ],
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('barcode_type', models.CharField(choices=[('EAN13', 'EAN-13'), ('UPC', 'UPC'), ('CODE128', 'Code 128'), ('INTERNAL', 'Internal')], default='INTERNAL', max_length=20)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcodes', to='core.productvariant')),
            ],
        ),
        migrations.CreateModel(
            name='StockMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('movement_type', models.CharField(choices=[('IN', 'In'), ('OUT', 'Out'), ('ADJUST', 'Adjustment'), ('TRANSFER', 'Transfer')], max_length=20)),
                ('reason', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('from_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movements_from', to='core.location')),
                ('to_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movements_to', to='core.location')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productvariant')),
            ],
        ),
        migrations.CreateModel(
            name='StockLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_on_hand', models.IntegerField(default=0)),
                ('quantity_reserved', models.IntegerField(default=0)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_levels', to='core.location')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_levels', to='core.productvariant')),
            ],
            options={
                'unique_together': {('variant', 'location')},
            },
        ),
    ]
