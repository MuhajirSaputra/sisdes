from django.db import models

class JobType(models.Model):
	nama = models.CharField(verbose_name='nama', max_length=15)
	deskripsi = models.TextField(verbose_name='Keterangan', max_length=50, blank=True)

	def __unicode__(self):
		return self.nama


class Rte(models.Model):
	nama = models.CharField(verbose_name='RT', max_length=5)
	deskripsi = models.TextField(verbose_name='Keterangan', max_length=20, blank=True)

	class Meta:
		verbose_name = 'RT'
		verbose_name_plural = 'RT'

	def __unicode__(self):
		return self.nama


class Rwe(models.Model):
	nama = models.CharField(verbose_name='RW', max_length=5)
	deskripsi = models.TextField(verbose_name='keterangan', max_length=20, blank=True)

	class Meta:
		verbose_name = 'RW'
		verbose_name_plural = 'RW'

	def __unicode__(self):
		return self.nama


class FamilyMember(models.Model):
	BLOOD_TYPE_CHOICES = (
		('A', 'A'),
		('B', 'B'),
		('O', 'O'),
		('AB', 'AB')
		)

	RELIGION_TYPE_CHOICES = (
		('I', 'ISLAM'),
		('K', 'KRISTEN'),
		('H', 'HINDU'),
		('B', 'BUDHA')
		)

	EDUCATION_TYPE_CHOICES = (
		('1', 'SD'),
		('2', 'SMP'),
		('3', 'SMA'),
		('4', 'D-1'),
		('5', 'D-2'),
		('6', 'D-3'),
		('7', 'S-1'),
		('8', 'S-2'),
		('9', 'S-3')
		)

	MARIED_TYPE_CHOICES = (
		('BK', 'Belum Kawin'),
		('KW', 'Kawin'),
		('JM', 'Janda Mati'),
		('JC', 'Janda Cerai'),
		('DM', 'Duda Mati'),
		('DC', 'Duda Cerai')
		)

	FAMILY_TYPE_CHOICES = (
		('S', 'SUAMI'),
		('I', 'ISTRI'),
		('A', 'ANAK')
		)

	NATIONAL_TYPE_CHOICES = (
		('WNI', 'INDONESIA'),
		('WNA', 'ASING')
		)

	MIGRASI_TYPE_CHOICES = (
		('PASPORT', 'PASPORT'),
		('KITAS', 'KITAS')
		)

	nik_id = models.CharField(verbose_name='NIK', max_length=16, unique=True)
	first_name = models.CharField(verbose_name='Nama Depan', max_length=20)
	last_name = models.CharField(verbose_name='Nama Belakang', max_length=20)
	birth_place = models.CharField(verbose_name='Tempat Lahir', max_length=15)
	birth_date = models.DateField(verbose_name='Tanggal Lahir')
	religion = models.CharField(verbose_name='Agama', max_length=8, choices=RELIGION_TYPE_CHOICES)
	maried_state = models.CharField(verbose_name='Status Kawin', max_length=6, choices=MARIED_TYPE_CHOICES)
	family_type = models.CharField(verbose_name='Hubungan Keluarga', max_length=6,choices=FAMILY_TYPE_CHOICES)
	blood = models.CharField(verbose_name='Golongan Darah', max_length=3, choices=BLOOD_TYPE_CHOICES)
	profesi = models.ForeignKey(JobType)
	national = models.CharField(verbose_name='Warga Negara', max_length=20, choices=NATIONAL_TYPE_CHOICES)
	migrasi = models.CharField(verbose_name='Data Migrasi', max_length=20, choices=MIGRASI_TYPE_CHOICES)

	class Meta:
		verbose_name = 'Family Member'
		verbose_name_plural = 'Family Member'

	def __unicode__(self):
		return self.first_name


class IdFams(models.Model):
	kk_id = models.CharField(verbose_name='ID KK', max_length=16, unique=True)
	kk_head = models.CharField(verbose_name='Nama Kepala Keluarga', max_length=20)
	dusun = models.CharField(verbose_name='Alamat Dusun', max_length=15)
	desa = models.CharField(verbose_name='Desa / Kelurahan', max_length=15)
	kecamatan = models.CharField(verbose_name='Kecamatan / Kota', max_length=15)
	kabupaten = models.CharField(verbose_name='kabupaten', max_length=15)
	provinsi = models.CharField(verbose_name='Provinsi', max_length=15)
	member = models.ForeignKey(FamilyMember)

	class Meta:
		verbose_name = 'Kartu Keluarga'
		verbose_name_plural = 'Kartu Keluarga'

	def __unicode__(self):
		return self.kk_id

    # Create your models here.
