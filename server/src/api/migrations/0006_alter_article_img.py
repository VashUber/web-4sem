# Generated by Django 4.2 on 2023-06-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_article_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="articlePreview"),
        ),
    ]
