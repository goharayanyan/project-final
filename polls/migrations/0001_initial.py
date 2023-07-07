# Generated by Django 4.1.6 on 2023-04-04 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BidRequest",
            fields=[
                (
                    "external_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("imp_banner_w", models.IntegerField()),
                ("imp_banner_h", models.IntegerField()),
                ("click_prob", models.FloatField()),
                ("conv_prob", models.FloatField()),
                ("site_domain", models.CharField(max_length=255)),
                ("ssp_id", models.CharField(max_length=255)),
                ("user_id", models.CharField(max_length=255)),
                ("bcat", models.JSONField(default=list)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Campaign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("budget", models.IntegerField()),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("status", models.CharField(blank=True, max_length=255, null=True)),
                ("targeting", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("impressions_total", models.IntegerField()),
                (
                    "auction_type",
                    models.IntegerField(
                        choices=[
                            (1, "First Price Auction"),
                            (2, "Second Price Auction"),
                        ]
                    ),
                ),
                (
                    "mode",
                    models.CharField(
                        choices=[("free", "Free"), ("script", "Script")], max_length=10
                    ),
                ),
                ("budget", models.FloatField()),
                ("impression_revenue", models.IntegerField()),
                ("click_revenue", models.IntegerField()),
                ("conversion_revenue", models.IntegerField()),
                ("frequency_capping", models.IntegerField()),
                (
                    "game_goal",
                    models.CharField(
                        choices=[("CPC", "cpc"), ("revenue", "Revenue")],
                        default="revenue",
                        max_length=50,
                    ),
                ),
                ("total_revenue", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "external_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("win", models.BooleanField(default=False)),
                ("price", models.FloatField()),
                ("click", models.BooleanField()),
                ("conversion", models.BooleanField()),
                ("revenue", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Creative",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("external_id", models.CharField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="creative/"),
                ),
                ("url", models.CharField(blank=True, max_length=255, null=True)),
                ("width", models.IntegerField(blank=True, null=True)),
                ("height", models.IntegerField(blank=True, null=True)),
                (
                    "campaign",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polls.campaign",
                    ),
                ),
                ("category", models.ManyToManyField(to="polls.category")),
            ],
        ),
        migrations.CreateModel(
            name="BidResponse",
            fields=[
                (
                    "external_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("bid", models.FloatField()),
                (
                    "bid_req",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polls.bidrequest",
                    ),
                ),
                (
                    "creative",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.creative"
                    ),
                ),
            ],
        ),
    ]