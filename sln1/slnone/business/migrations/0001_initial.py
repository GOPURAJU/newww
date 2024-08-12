# Generated by Django 5.0.6 on 2024-08-11 14:28

import business.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='busbasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[business.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[business.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField(validators=[business.models.validate_date])),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.DecimalField(decimal_places=2, max_digits=50, validators=[business.models.validate_amount])),
                ('terms_accepted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('pan_card_number', models.CharField(max_length=10, unique=True)),
                ('aadhar_card_number', models.CharField(max_length=12, unique=True)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widowed')], max_length=1)),
                ('email_id', models.EmailField(max_length=254)),
                ('current_address', models.TextField()),
                ('current_address_pincode', models.IntegerField()),
                ('aadhar_address', models.TextField()),
                ('aadhar_pincode', models.IntegerField()),
                ('running_emis_amount_per_month', models.DecimalField(decimal_places=2, max_digits=15)),
                ('net_income_per_month', models.DecimalField(decimal_places=2, max_digits=15)),
                ('business_name', models.CharField(max_length=200)),
                ('business_type', models.CharField(choices=[('Sole Proprietorship', 'Sole Proprietorship'), ('Partnership', 'Partnership'), ('Private Limited Company', 'Private Limited Company'), ('Public Limited Company', 'Public Limited Company'), ('LLP', 'Limited Liability Partnership'), ('Others', 'Others')], max_length=50)),
                ('business_establishment_date', models.DateField()),
                ('has_gst_certificate', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('gst_number', models.CharField(blank=True, max_length=15, null=True)),
                ('mother_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('nature_of_business', models.CharField(max_length=200)),
                ('turnover_in_lakhs_per_year', models.DecimalField(decimal_places=2, max_digits=15)),
                ('business_address', models.TextField()),
                ('business_address_pincode', models.IntegerField()),
                ('required_loan_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ref_1_person_name', models.CharField(max_length=100)),
                ('ref_1_person_mobile_number', models.CharField(max_length=15)),
                ('ref_2_person_name', models.CharField(max_length=100)),
                ('ref_2_person_mobile_number', models.CharField(max_length=15)),
                ('own_house', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('remarks', models.TextField()),
                ('application_id', models.CharField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('messgae', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_detail_verifaction', models.CharField(blank=True, max_length=50)),
                ('documents_upload_verification', models.CharField(blank=True, max_length=50)),
                ('documents_verification', models.CharField(blank=True, max_length=50)),
                ('eligibility_check_verification', models.CharField(blank=True, max_length=50)),
                ('bank_login_verification', models.CharField(blank=True, max_length=50)),
                ('kyc_and_document_verification', models.CharField(blank=True, max_length=50)),
                ('enach_verification', models.CharField(blank=True, max_length=50)),
                ('disbursment_verification', models.CharField(blank=True, max_length=50)),
                ('verification_status', models.CharField(blank=True, max_length=100)),
                ('loan', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationverification', to='business.businessloan')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessLoanDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_card_front', models.ImageField(upload_to='BussinessLoandocuments/aadhar/')),
                ('aadhar_card_back', models.ImageField(upload_to='BussinessLoandocuments/aadhar/')),
                ('pan_card', models.ImageField(upload_to='BussinessLoandocuments/pan/')),
                ('customer_photo', models.ImageField(upload_to='BussinessLoandocuments/customer_photos/')),
                ('business_proof_1', models.FileField(upload_to='BussinessLoandocuments/business_proofs/')),
                ('business_proof_2', models.FileField(upload_to='BussinessLoandocuments/business_proofs/')),
                ('latest_12_months_bank_statement', models.FileField(upload_to='BussinessLoandocuments/bank_statements/')),
                ('business_office_photo', models.ImageField(upload_to='BussinessLoandocuments/business_office_photos/')),
                ('latest_3_yrs_itr_1', models.FileField(upload_to='BussinessLoandocuments/itr/')),
                ('latest_3_yrs_itr_2', models.FileField(upload_to='BussinessLoandocuments/itr/')),
                ('latest_3_yrs_itr_3', models.FileField(upload_to='BussinessLoandocuments/itr/')),
                ('current_address_proof', models.FileField(upload_to='BussinessLoandocuments/address_proofs/')),
                ('other_document_1', models.FileField(upload_to='BussinessLoandocuments/other/')),
                ('other_document_2', models.FileField(upload_to='BussinessLoandocuments/other/')),
                ('loan', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='BussinessLoandocuments', to='business.businessloan')),
            ],
        ),
    ]
