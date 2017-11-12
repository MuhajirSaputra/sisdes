# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nik_id', models.CharField(unique=True, max_length=16, verbose_name=b'NIK')),
                ('first_name', models.CharField(max_length=20, verbose_name=b'Nama Depan')),
                ('last_name', models.CharField(max_length=20, verbose_name=b'Nama Belakang')),
                ('birth_place', models.CharField(max_length=15, verbose_name=b'Tempat Lahir')),
                ('birth_date', models.DateField(verbose_name=b'Tanggal Lahir')),
                ('religion', models.CharField(max_length=8, verbose_name=b'Agama', choices=[(b'I', b'ISLAM'), (b'K', b'KRISTEN'), (b'H', b'HINDU'), (b'B', b'BUDHA')])),
                ('maried_state', models.CharField(max_length=6, verbose_name=b'Status Kawin', choices=[(b'BK', b'Belum Kawin'), (b'KW', b'Kawin'), (b'JM', b'Janda Mati'), (b'JC', b'Janda Cerai'), (b'DM', b'Duda Mati'), (b'DC', b'Duda Cerai')])),
                ('family_type', models.CharField(max_length=6, verbose_name=b'Hubungan Keluarga', choices=[(b'S', b'SUAMI'), (b'I', b'ISTRI'), (b'A', b'ANAK')])),
                ('blood', models.CharField(max_length=3, verbose_name=b'Golongan Darah', choices=[(b'A', b'A'), (b'B', b'B'), (b'O', b'O'), (b'AB', b'AB')])),
                ('national', models.CharField(max_length=20, verbose_name=b'Warga Negara', choices=[(b'WNI', b'INDONESIA'), (b'WNA', b'ASING')])),
                ('migrasi', models.CharField(max_length=20, verbose_name=b'Data Migrasi', choices=[(b'PASPORT', b'PASPORT'), (b'KITAS', b'KITAS')])),
            ],
            options={
                'verbose_name': 'Family Member',
                'verbose_name_plural': 'Family Member',
            },
        ),
        migrations.CreateModel(
            name='IdFams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kk_id', models.CharField(unique=True, max_length=16, verbose_name=b'ID KK')),
                ('kk_head', models.CharField(max_length=20, verbose_name=b'Nama Kepala Keluarga')),
                ('dusun', models.CharField(max_length=15, verbose_name=b'Alamat Dusun')),
                ('desa', models.CharField(max_length=15, verbose_name=b'Desa / Kelurahan')),
                ('kecamatan', models.CharField(max_length=15, verbose_name=b'Kecamatan / Kota')),
                ('kabupaten', models.CharField(max_length=15, verbose_name=b'kabupaten')),
                ('provinsi', models.CharField(max_length=15, verbose_name=b'Provinsi')),
                ('member', models.ForeignKey(to='idfams.FamilyMember')),
            ],
            options={
                'verbose_name': 'Kartu Keluarga',
                'verbose_name_plural': 'Kartu Keluarga',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=15, verbose_name=b'nama')),
                ('deskripsi', models.TextField(max_length=50, verbose_name=b'Keterangan', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=5, verbose_name=b'RT')),
                ('deskripsi', models.TextField(max_length=20, verbose_name=b'Keterangan', blank=True)),
            ],
            options={
                'verbose_name': 'RT',
                'verbose_name_plural': 'RT',
            },
        ),
        migrations.CreateModel(
            name='Rwe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=5, verbose_name=b'RW')),
                ('deskripsi', models.TextField(max_length=20, verbose_name=b'keterangan', blank=True)),
            ],
            options={
                'verbose_name': 'RW',
                'verbose_name_plural': 'RW',
            },
        ),
        migrations.AddField(
            model_name='familymember',
            name='profesi',
            field=models.ForeignKey(to='idfams.JobType'),
        ),
    ]
