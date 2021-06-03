# Generated by Django 3.2.2 on 2021-05-07 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('keywords', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='category')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='ProductApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('keywords', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('new_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount', models.IntegerField(default=0)),
                ('min_amount', models.IntegerField(default=2)),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=50)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=264)),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.product')),
            ],
        ),
    ]
