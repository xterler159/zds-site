# Generated by Django 4.2.16 on 2024-10-18 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tutorialv2", "0041_remove_must_reindex"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contentsuggestion",
            options={"verbose_name": "Suggestion de publication", "verbose_name_plural": "Suggestions de publication"},
        ),
        migrations.AlterField(
            model_name="contentsuggestion",
            name="publication",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="publication",
                to="tutorialv2.publishablecontent",
                verbose_name="Publication",
            ),
        ),
    ]
