# Generated by Django 1.11 on 2019-02-22 17:17

import django.db.models.deletion
import django.utils.timezone
import enumfields.fields
from django.db import migrations, models

import checks.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ASRecord",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.PositiveIntegerField(unique=True)),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="BatchCustomView",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="BatchDomain",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(default="", max_length=255)),
                (
                    "status",
                    enumfields.fields.EnumIntegerField(db_index=True, default=0, enum=checks.models.BatchDomainStatus),
                ),
                ("status_changed", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="BatchMailTest",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ipv6_status", enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus)),
                ("ipv6_errors", models.PositiveSmallIntegerField(default=0)),
                ("dnssec_status", enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus)),
                ("dnssec_errors", models.PositiveSmallIntegerField(default=0)),
                ("auth_status", enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus)),
                ("auth_errors", models.PositiveSmallIntegerField(default=0)),
                ("tls_status", enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus)),
                ("tls_errors", models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="BatchRequest",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("submit_date", models.DateTimeField(auto_now_add=True)),
                ("finished_date", models.DateTimeField(null=True)),
                ("type", enumfields.fields.EnumIntegerField(enum=checks.models.BatchRequestType)),
                (
                    "status",
                    enumfields.fields.EnumIntegerField(db_index=True, default=0, enum=checks.models.BatchRequestStatus),
                ),
                (
                    "request_id",
                    models.CharField(db_index=True, default=checks.models.batch_request_id, max_length=32, unique=True),
                ),
                ("report_file", models.FileField(upload_to="batch_results/")),
            ],
        ),
        migrations.CreateModel(
            name="BatchUser",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255, null=True)),
                ("organization", models.CharField(max_length=255, null=True)),
                ("email", models.EmailField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="BatchWebTest",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ipv6_status", enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus)),
                ("ipv6_errors", models.PositiveSmallIntegerField(default=0)),
                ("dnssec_status", enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus)),
                ("dnssec_errors", models.PositiveSmallIntegerField(default=0)),
                ("tls_status", enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus)),
                ("tls_errors", models.PositiveSmallIntegerField(default=0)),
                (
                    "appsecpriv_status",
                    enumfields.fields.EnumIntegerField(default=0, enum=checks.models.BatchTestStatus),
                ),
                ("appsecpriv_errors", models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="ConnectionTest",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("report", checks.models.ListField(default="")),
                ("reportdnssec", checks.models.ListField(default="")),
                (
                    "test_id",
                    models.CharField(db_index=True, default=checks.models.conn_test_id, max_length=32, unique=True),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("ipv4_addr", models.CharField(default="", max_length=16)),
                ("ipv4_owner", models.CharField(default="", max_length=255)),
                ("ipv4_reverse", models.CharField(default="", max_length=255)),
                ("ipv6_addr", models.CharField(default="", max_length=40)),
                ("ipv6_owner", models.CharField(default="", max_length=255)),
                ("ipv6_reverse", models.CharField(default="", max_length=255)),
                ("aaaa_ipv6", models.BooleanField(default=False)),
                ("addr_ipv6", models.BooleanField(default=False)),
                ("resolv_ipv6", models.BooleanField(default=False)),
                ("slaac_without_privext", models.BooleanField(default=False)),
                ("dnssec_val", models.BooleanField(default=False)),
                ("score_ipv6", models.IntegerField(null=True)),
                ("score_ipv6_max", models.IntegerField(null=True)),
                ("score_dnssec", models.IntegerField(null=True)),
                ("score_dnssec_max", models.IntegerField(null=True)),
                ("finished", models.BooleanField(default=False)),
                (
                    "ipv4_origin_as",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ipv4_connection_tests",
                        to="checks.ASRecord",
                    ),
                ),
                (
                    "ipv6_origin_as",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ipv6_connection_tests",
                        to="checks.ASRecord",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DomainTestAppsecpriv",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(default="", max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("server_reachable", models.BooleanField(default=True)),
                ("score", models.IntegerField(null=True)),
                ("x_frame_options_enabled", models.NullBooleanField(default=False)),
                ("x_frame_options_values", models.TextField(default="")),
                ("x_frame_options_score", models.IntegerField(null=True)),
                ("x_xss_protection_enabled", models.NullBooleanField(default=False)),
                ("x_xss_protection_values", models.TextField(default="")),
                ("x_xss_protection_score", models.IntegerField(null=True)),
                ("referrer_policy_enabled", models.NullBooleanField(default=False)),
                ("referrer_policy_values", models.TextField(default="")),
                ("referrer_policy_score", models.IntegerField(null=True)),
                ("content_security_policy_enabled", models.NullBooleanField(default=False)),
                ("content_security_policy_values", models.TextField(default="")),
                ("content_security_policy_score", models.IntegerField(null=True)),
                ("x_content_type_options_enabled", models.NullBooleanField(default=False)),
                ("x_content_type_options_values", models.TextField(default="")),
                ("x_content_type_options_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DomainTestDnssec",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("status", enumfields.fields.EnumField(default=0, enum=checks.models.DnssecStatus, max_length=10)),
                ("log", models.TextField(default="", null=True)),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DomainTestIpv6",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("web_simhash_distance", models.IntegerField(null=True)),
                ("web_simhash_score", models.IntegerField(null=True)),
                ("web_score", models.IntegerField(null=True)),
                ("mx_score", models.IntegerField(null=True)),
                ("ns_score", models.IntegerField(null=True)),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DomainTestReport",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(default="", max_length=255)),
                ("registrar", models.CharField(default="", max_length=255)),
                ("score", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DomainTestTls",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(default="", max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("port", models.IntegerField(null=True)),
                ("server_reachable", models.NullBooleanField(default=True)),
                ("tls_enabled", models.NullBooleanField(default=False)),
                ("tls_enabled_score", models.IntegerField(null=True)),
                ("could_not_test_smtp_starttls", models.BooleanField(default=False)),
                ("dane_log", models.TextField(default="", null=True)),
                ("dane_score", models.IntegerField(null=True)),
                ("dane_status", enumfields.fields.EnumField(default=2, enum=checks.models.DaneStatus, max_length=10)),
                ("dane_records", models.TextField(default=[])),
                ("dane_rollover", models.BooleanField(default=False)),
                ("dh_param", models.CharField(default="", max_length=255, null=True)),
                ("ecdh_param", models.CharField(default="", max_length=255, null=True)),
                ("fs_bad", checks.models.ListField(null=True)),
                ("fs_score", models.IntegerField(null=True)),
                ("ciphers_bad", checks.models.ListField(null=True)),
                ("ciphers_score", models.IntegerField(null=True)),
                ("protocols_bad", checks.models.ListField(null=True)),
                ("protocols_score", models.IntegerField(null=True)),
                ("compression", models.NullBooleanField(default=False)),
                ("compression_score", models.IntegerField(null=True)),
                ("secure_reneg", models.NullBooleanField(default=False)),
                ("secure_reneg_score", models.IntegerField(null=True)),
                ("client_reneg", models.NullBooleanField(default=False)),
                ("client_reneg_score", models.IntegerField(null=True)),
                (
                    "forced_https",
                    enumfields.fields.EnumField(default=0, enum=checks.models.ForcedHttpsStatus, max_length=10),
                ),
                ("forced_https_score", models.IntegerField(null=True)),
                ("http_compression_enabled", models.NullBooleanField(default=False)),
                ("http_compression_score", models.IntegerField(null=True)),
                ("hsts_enabled", models.NullBooleanField(default=False)),
                ("hsts_policies", models.TextField(default="")),
                ("hsts_score", models.IntegerField(null=True)),
                ("cert_chain", checks.models.ListField(null=True)),
                ("cert_trusted", models.IntegerField(null=True)),
                ("cert_trusted_score", models.IntegerField(null=True)),
                ("cert_pubkey_bad", checks.models.ListField(null=True)),
                ("cert_pubkey_score", models.IntegerField(null=True)),
                ("cert_signature_bad", checks.models.ListField(null=True)),
                ("cert_signature_score", models.IntegerField(null=True)),
                ("cert_hostmatch_bad", checks.models.ListField(null=True)),
                ("cert_hostmatch_score", models.IntegerField(null=True)),
                ("score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MailTestAuth",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("dkim_score", models.IntegerField(null=True)),
                ("dkim_available", models.BooleanField(default=False)),
                ("dmarc_score", models.IntegerField(null=True)),
                ("dmarc_available", models.BooleanField(default=False)),
                ("dmarc_record", models.TextField(default="")),
                (
                    "dmarc_policy_status",
                    enumfields.fields.EnumIntegerField(enum=checks.models.DmarcPolicyStatus, null=True),
                ),
                ("dmarc_policy_score", models.IntegerField(null=True)),
                ("spf_score", models.IntegerField(null=True)),
                ("spf_available", models.BooleanField(default=False)),
                ("spf_record", models.TextField(default="")),
                (
                    "spf_policy_status",
                    enumfields.fields.EnumIntegerField(enum=checks.models.SpfPolicyStatus, null=True),
                ),
                ("spf_policy_score", models.IntegerField(null=True)),
                ("spf_policy_records", checks.models.ListField(null=True)),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MailTestDnssec",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(default="", max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MailTestIpv6",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("mx_score", models.IntegerField(null=True)),
                ("ns_score", models.IntegerField(null=True)),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MailTestReport",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("domain", models.CharField(default="", max_length=255)),
                ("registrar", models.CharField(default="", max_length=255)),
                ("score", models.IntegerField(null=True)),
                (
                    "auth",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestAuth"),
                ),
                (
                    "dnssec",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestDnssec"
                    ),
                ),
                (
                    "ipv6",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestIpv6"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MailTestTls",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(default="", max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MxDomain",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(max_length=255)),
                ("v6_good", checks.models.ListField()),
                ("v6_bad", checks.models.ListField()),
                ("v4_good", checks.models.ListField()),
                ("v4_bad", checks.models.ListField()),
                ("score", models.IntegerField(null=True)),
                (
                    "mailtestipv6",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestIpv6"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NsDomain",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(max_length=255)),
                ("v6_good", checks.models.ListField()),
                ("v6_bad", checks.models.ListField()),
                ("v4_good", checks.models.ListField()),
                ("v4_bad", checks.models.ListField()),
                ("score", models.IntegerField(null=True)),
                (
                    "domaintestipv6",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.DomainTestIpv6"
                    ),
                ),
                (
                    "mailtestipv6",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestIpv6"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Ranking",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="", max_length=255)),
                ("type", models.IntegerField()),
                ("score", models.FloatField()),
                ("timestamp", models.DateTimeField()),
                ("permalink", models.CharField(default="/", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Resolver",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("address", models.CharField(max_length=40)),
                ("owner", models.CharField(max_length=255)),
                ("reverse", models.CharField(max_length=255)),
                (
                    "connectiontest",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="checks.ConnectionTest"),
                ),
                (
                    "origin_as",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resolvers",
                        to="checks.ASRecord",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WebDomain",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(max_length=255)),
                ("v6_good", checks.models.ListField()),
                ("v6_bad", checks.models.ListField()),
                ("v4_good", checks.models.ListField()),
                ("v4_bad", checks.models.ListField()),
                ("score", models.IntegerField(null=True)),
                (
                    "domaintestipv6",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.DomainTestIpv6"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WebTestAppsecpriv",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(default="", max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WebTestTls",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("domain", models.CharField(default="", max_length=255)),
                ("report", checks.models.ListField(default="")),
                ("score", models.IntegerField(null=True)),
                ("max_score", models.IntegerField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="mailtestreport",
            name="tls",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestTls"),
        ),
        migrations.AddField(
            model_name="domaintesttls",
            name="maildomain",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, related_name="testset", to="checks.MailTestTls"
            ),
        ),
        migrations.AddField(
            model_name="domaintesttls",
            name="webdomain",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="webtestset",
                to="checks.WebTestTls",
            ),
        ),
        migrations.AddField(
            model_name="domaintestreport",
            name="appsecpriv",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.WebTestAppsecpriv"
            ),
        ),
        migrations.AddField(
            model_name="domaintestreport",
            name="dnssec",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.DomainTestDnssec"
            ),
        ),
        migrations.AddField(
            model_name="domaintestreport",
            name="ipv6",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.DomainTestIpv6"),
        ),
        migrations.AddField(
            model_name="domaintestreport",
            name="tls",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.WebTestTls"),
        ),
        migrations.AddField(
            model_name="domaintestdnssec",
            name="maildomain",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="testset",
                to="checks.MailTestDnssec",
            ),
        ),
        migrations.AddField(
            model_name="domaintestappsecpriv",
            name="webdomain",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="webtestset",
                to="checks.WebTestAppsecpriv",
            ),
        ),
        migrations.AddField(
            model_name="batchwebtest",
            name="appsecpriv",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.WebTestAppsecpriv"
            ),
        ),
        migrations.AddField(
            model_name="batchwebtest",
            name="dnssec",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.DomainTestDnssec"
            ),
        ),
        migrations.AddField(
            model_name="batchwebtest",
            name="ipv6",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.DomainTestIpv6"),
        ),
        migrations.AddField(
            model_name="batchwebtest",
            name="report",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.DomainTestReport"
            ),
        ),
        migrations.AddField(
            model_name="batchwebtest",
            name="tls",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.WebTestTls"),
        ),
        migrations.AddField(
            model_name="batchrequest",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="batch_requests", to="checks.BatchUser"
            ),
        ),
        migrations.AddField(
            model_name="batchmailtest",
            name="auth",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestAuth"),
        ),
        migrations.AddField(
            model_name="batchmailtest",
            name="dnssec",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestDnssec"),
        ),
        migrations.AddField(
            model_name="batchmailtest",
            name="ipv6",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestIpv6"),
        ),
        migrations.AddField(
            model_name="batchmailtest",
            name="report",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestReport"),
        ),
        migrations.AddField(
            model_name="batchmailtest",
            name="tls",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.MailTestTls"),
        ),
        migrations.AddField(
            model_name="batchdomain",
            name="batch_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="domains", to="checks.BatchRequest"
            ),
        ),
        migrations.AddField(
            model_name="batchdomain",
            name="mailtest",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.BatchMailTest"),
        ),
        migrations.AddField(
            model_name="batchdomain",
            name="webtest",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="checks.BatchWebTest"),
        ),
        migrations.AddField(
            model_name="batchcustomview",
            name="users",
            field=models.ManyToManyField(related_name="custom_views", to="checks.BatchUser"),
        ),
    ]
