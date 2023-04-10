from importlib.metadata import distribution
from pyexpat import model
from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def nominee_proof_directory_path(instance, filename):
    return 'nominee_proof_{0}/{1}'.format(instance.user.id, filename)

panvalidate = RegexValidator("[A-Z]{5}[0-9]{4}[A-Z]{1}")
pincode_regex = RegexValidator(regex=r'^\d{6}$', message="Pin code must be entered in the format: 110049")

# Create your models here.

class Country(models.Model):
    name                    = models.CharField(max_length=100)
    code                    = models.CharField(max_length=5)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name                    = models.CharField(max_length=100)
    code                    = models.CharField(max_length=5)
    country                 = models.ForeignKey(Country, on_delete=models.CASCADE)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class City(models.Model):
    state                   = models.ForeignKey(State, on_delete=models.CASCADE)
    country                 = models.ForeignKey(Country, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=100)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Clientmaster(models.Model):
    dob_regex = RegexValidator(regex=r'^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$', message="Date of birth must be entered in the format: 'DD/MM/YYYY'")
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    )
    BLOOD_GROUP = (
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    )
    OCCUPATION = (
        ('01', 'Business'),
        ('02', 'Services'),
        ('03', 'Professional'),
        ('04', 'Agriculture'),
        ('05', 'Retired'),
        ('06', 'Housewife'),
        ('07', 'Student'),
        ('08', 'Others'),
    )
    INCOMESLAB = (
        (31, 'Below 1 Lakh'),
        (32, '> 1 <=5 Lacs'),
        (33, '>5 <=10 Lacs'),
        (34, '>10 <= 25 Lacs'),
        (35, '> 25 Lacs < = 1 Crore'),
        (36, 'Above 1 Crore'),
    )
    CLIENT_HOLDING = (
        ('SI', 'Single'),
        ('JO', 'Joint'),
        ('AS', 'Anyone or Survivor'),
    )
    CLIENT_TAX_STATUS = (
        ('01', 'Individual'),
        ('02', 'On behalf of minor'),
        ('03', 'HUF'),
        ('04', 'Company'),
        ('21', 'NRE'),
        ('24', 'NRO'),
        ('23', 'FII'),
        ('12', 'DFI'),
        ('08', 'TRUST'),
        ('05', 'AOP'),
        ('47', 'LLP'),
        ('10', 'Others'),
        ('06', 'Partnership Firm'),
    )
    COMMUNICATION_MODE = (
        ('P', 'Physical'),
        ('E', 'Electronic'),
    )
    DIVIDENT_PAY_MODE = (
        ('01', 'Cheque'),
        ('02', 'Direct Credit'),
        ('03', 'ECS'),
        ('04', 'ECS'),
        ('05', 'RTGS'),
    )
    KYC_TYPE = (
        ('K', 'KRA Compliant'),
        ('C', 'CKYC Compliant'),
        ('B', 'BIOMETRIC KYC'),
        ('E', 'Aadhaar Ekyc PAN'),
    )
    PAPERLESS_FLAG = (
        ('P', 'Paper'),
        ('Z', 'paperless'),
    )

    client_code               = models.CharField(max_length=10, unique=True)
    client_holding            = models.CharField(max_length=2, choices= CLIENT_HOLDING, blank=True)
    client_tax_status         = models.CharField(max_length=2, choices= CLIENT_TAX_STATUS, blank=True)
    client_occupation_code    = models.CharField(max_length=2, choices= OCCUPATION, blank=True)
    first_name                = models.CharField(max_length=35)
    middle_name               = models.CharField(max_length=35)
    last_name                 = models.CharField(max_length=35)
    date_of_birth             = models.CharField(max_length=10, validators=[dob_regex], blank=True)
    gender                    = models.CharField(max_length=2, choices= GENDER, blank=True)
    father_first_name         = models.CharField(max_length=35, help_text='Father/ Husband/ Guardian Name')
    father_last_name          = models.CharField(max_length=35, null=True, blank=True)
    pan_number                = models.CharField(max_length=10, validators=[panvalidate])
    email                     = models.EmailField()
    communication_mode        = models.CharField(max_length=1, default='E')
    divident_pay_mode         = models.CharField(max_length=2, choices= DIVIDENT_PAY_MODE, blank=True)
    first_holder_ckyc_number  = models.CharField(max_length=14, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
    first_holder_kyc_type     = models.CharField(max_length=2, choices= KYC_TYPE, blank=True)
    second_holder_ckyc_number = models.CharField(max_length=14, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
    second_holder_kyc_type    = models.CharField(max_length=2, choices= KYC_TYPE, blank=True)
    third_holder_ckyc_number  = models.CharField(max_length=14, blank=True, validators=[RegexValidator(r'^\d{1,10}$')])
    third_holder_kyc_type     = models.CharField(max_length=2, choices= KYC_TYPE, blank=True)
    aadhar_updated            = models.CharField(max_length=1, blank=True)
    paperless_flag            = models.CharField(max_length=2, choices= PAPERLESS_FLAG, blank=True)
    # dp                      = models.CharField(max_length=4, default='0000000', editable=False)
    # dp_id                   = models.CharField(max_length=8, default='0000000', editable=False)
    # dp_client_id            = models.CharField(max_length=16, default='0000000', editable=False)
    # arn_no                  = models.CharField(max_length=15, default='E')

    cancel_check              = models.ImageField(upload_to = user_directory_path)
    aadhar_number             = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{1,12}$')])

    anniversary_date          = models.DateField(null=True, blank=True)
    mobile                    = models.PositiveIntegerField(validators=[MaxValueValidator(1999999999)])
    phone                     = models.PositiveIntegerField(null=True, blank=True)
    broker_code               = models.IntegerField(null=True, blank=True)
    emfi_code                 = models.CharField(max_length=20, null=True, blank=True)

    family_group_code         = models.CharField(max_length=6, null=True, blank=True)
    is_active                 = models.BooleanField(default=True)
    marital_status            = models.CharField(max_length=2, choices= MARITAL_STATUS)

    blood_group               = models.CharField(max_length=3, choices= BLOOD_GROUP, blank=True)
    income_slab               = models.CharField(max_length=2, choices= INCOMESLAB, blank=True)

    created                   = models.DateTimeField(auto_now=True)
    updated                   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

class Nomineemaster(models.Model):
    CLIENT_NOMINEE_RELATION = (
        ('01', 'Mother'),
        ('02', 'Father'),
        ('03', 'Wife'),
        ('04', 'Husband'),
        ('05', 'Son'),
        ('06', 'Mother'),
        ('07', 'Daughter'),
        ('08', 'Nephews'),
        ('09', 'Uncle'),
        ('10', 'Aunt'),
    )

    client                    = models.ForeignKey(Clientmaster, on_delete=models.CASCADE)
    first_name                = models.CharField(max_length=35)
    middle_name               = models.CharField(max_length=35)
    last_name                 = models.CharField(max_length=35)
    date_of_birth             = models.DateField()
    client_nominee_relation   = models.CharField(max_length=3, choices= CLIENT_NOMINEE_RELATION)
    share_appicable           = models.DecimalField(max_digits=5, decimal_places=2)
    mobile                    = models.PositiveIntegerField(validators=[MaxValueValidator(1999999999)])
    email                     = models.EmailField()
    nominee_proof             = models.ImageField(upload_to = nominee_proof_directory_path)

    created                   = models.DateTimeField(auto_now=True)
    updated                   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name


class Address(models.Model):
    pincode_regex = RegexValidator(regex=r'^\d{6}$', message="Pin code must be entered in the format: 110049")
    ADDRESS_TYPE = (
        ('01', 'Home'),
        ('02', 'Office'),
    )

    address_type            = models.CharField(max_length=2, choices= ADDRESS_TYPE, blank=True)
    address1                = models.CharField(max_length=40)
    address2                = models.CharField(max_length=40)
    address3                = models.CharField(max_length=40, null=True, blank=True)
    pincode                 = models.CharField(max_length=6, validators=[pincode_regex], help_text='sample: 110049', blank=True)
    city                    = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    state                   = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    country                 = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    is_primary              = models.BooleanField()
    client                  = models.ForeignKey(Clientmaster, on_delete=models.CASCADE, null=True, blank=True)
    nominee                  = models.ForeignKey(Nomineemaster, on_delete=models.CASCADE, null=True, blank=True)

class Demat(models.Model):
    client                  = models.ForeignKey(Clientmaster, on_delete=models.CASCADE, null=True, blank=True)
    dp_details              = models.CharField(max_length=100)
    dp_name                 = models.CharField(max_length=100)
    dp_id                   = models.CharField(max_length=16)
    benificary_acc_no       = models.CharField(max_length=30)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dp_name

class Branchmaster(Address):
    branch_code             = models.AutoField(primary_key=True)
    branch_name             = models.CharField(max_length=100)
    branch_contact          = models.CharField(max_length=20)
    branch_email            = models.EmailField()
    location                = models.CharField(max_length=100)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name

class Designation(models.Model):
    name                    = models.CharField(max_length=50, unique=True)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employeemaster(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
    )
    BLOOD_GROUP = (
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    )

    first_name              = models.CharField(max_length=100)
    last_name               = models.CharField(max_length=100)
    middle_name             = models.CharField(max_length=100)
    reporting_aurthority    = models.ForeignKey('self', on_delete=models.CASCADE)
    designation             = models.ForeignKey(Designation, on_delete=models.CASCADE)
    branch                  = models.ForeignKey(Branchmaster, on_delete=models.CASCADE)
    date_of_birth           = models.DateField()
    email                   = models.EmailField()
    emp_id                  = models.CharField(max_length=6)
    is_active               = models.BooleanField(default=True)
    blood_group             = models.CharField(max_length=3, choices= BLOOD_GROUP, blank=True)
    marital_status          = models.CharField(max_length=2, choices= MARITAL_STATUS)
    gender                  = models.CharField(max_length=2, choices= GENDER, blank=True)
    anniversary_date        = models.DateField(null=True, blank=True)
    aadhar_number           = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{1,12}$')])
    mobile                  = models.PositiveIntegerField(validators=[MaxValueValidator(1999999999)])
    phone                   = models.PositiveIntegerField(null=True, blank=True)
    joining_date            = models.DateField()
    releaving_date          = models.DateField(null=True, blank=True)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name


class Superdistributor(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
    )
    BLOOD_GROUP = (
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    )
    first_name              = models.CharField(max_length=35)
    middle_name             = models.CharField(max_length=35)
    last_name               = models.CharField(max_length=35)
    branch                  = models.ForeignKey(Branchmaster, on_delete=models.CASCADE)
    super_distributor       = models.ForeignKey('self', on_delete=models.CASCADE)
    broker_code             = models.IntegerField(null=True, blank=True)
    joining_date            = models.DateField()
    releaving_date          = models.DateField(null=True, blank=True)
    mobile_number           = models.PositiveIntegerField(validators=[MaxValueValidator(1999999999)])
    phone_number            = models.PositiveIntegerField(null=True, blank=True)
    pancard                 = models.CharField(max_length=10, validators=[panvalidate])
    email                   = models.EmailField()
    date_of_birth           = models.DateField()
    anniversy               = models.DateField(null=True, blank=True)
    address                 = models.TextField()
    pincode                 = models.CharField(max_length=6, validators=[pincode_regex], help_text='sample: 110049', blank=True)
    city                    = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    state                   = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    country                 = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    blood_group             = models.CharField(max_length=3, choices= BLOOD_GROUP, blank=True)
    marital_status          = models.CharField(max_length=2, choices= MARITAL_STATUS)
    gender                  = models.CharField(max_length=2, choices= GENDER, blank=True)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
    

class Distributor(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
    )
    BLOOD_GROUP = (
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    )
    first_name              = models.CharField(max_length=35)
    middle_name             = models.CharField(max_length=35)
    last_name               = models.CharField(max_length=35)
    branch                  = models.ForeignKey(Branchmaster, on_delete=models.CASCADE)
    super_distributor       = models.ForeignKey(Superdistributor, on_delete=models.CASCADE)
    broker_code             = models.IntegerField(null=True, blank=True)
    joining_date            = models.DateField()
    releaving_date          = models.DateField(null=True, blank=True)
    mobile_number           = models.PositiveIntegerField(validators=[MaxValueValidator(1999999999)])
    phone_number            = models.PositiveIntegerField(null=True, blank=True)
    pancard                 = models.CharField(max_length=10, validators=[panvalidate])
    email                   = models.EmailField()
    date_of_birth           = models.DateField()
    anniversy               = models.DateField(null=True, blank=True)
    address                 = models.TextField()
    pincode                 = models.CharField(max_length=6, validators=[pincode_regex], help_text='sample: 110049', blank=True)
    city                    = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    state                   = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    country                 = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    blood_group             = models.CharField(max_length=3, choices= BLOOD_GROUP, blank=True)
    marital_status          = models.CharField(max_length=2, choices= MARITAL_STATUS)
    gender                  = models.CharField(max_length=2, choices= GENDER, blank=True)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

class Referencemaster(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
    )
    BLOOD_GROUP = (
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    )
    first_name              = models.CharField(max_length=35)
    middle_name             = models.CharField(max_length=35)
    last_name               = models.CharField(max_length=35)
    branch                  = models.ForeignKey(Branchmaster, on_delete=models.CASCADE)
    broker_code             = models.IntegerField(null=True, blank=True)
    joining_date            = models.DateField()
    releaving_date          = models.DateField(null=True, blank=True)
    mobile_number           = models.PositiveIntegerField(validators=[MaxValueValidator(1999999999)])
    phone_number            = models.PositiveIntegerField(null=True, blank=True)
    pancard                 = models.CharField(max_length=10, validators=[panvalidate])
    email                   = models.EmailField()
    date_of_birth           = models.DateField()
    anniversy               = models.DateField(null=True, blank=True)
    address                 = models.TextField()
    pincode                 = models.CharField(max_length=6, validators=[pincode_regex], help_text='sample: 110049', blank=True)
    city                    = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    state                   = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    country                 = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    blood_group             = models.CharField(max_length=3, choices= BLOOD_GROUP, blank=True)
    marital_status          = models.CharField(max_length=2, choices= MARITAL_STATUS)
    gender                  = models.CharField(max_length=2, choices= GENDER, blank=True)
    distribution            = models.ForeignKey(Distributor, on_delete=models.CASCADE)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

class Bankmaster(models.Model):
    ACCOUNTTYPE = (
        ('SB', 'Savings'),
        ('CB', 'Current'),
        ('NE', 'NRE'),
        ('NO', 'NRO'),
    )
    
    ifsc_code_regex = RegexValidator(regex=r'^[A-Z]{4}0[A-Z0-9]{6}$', message="IFSC code must be in the format: HDFC0000291")
    micr_code_regex = RegexValidator(regex=r'^\w{9}$', message="MICR code must be entered in the format: 110240212")
    account_number_regex = RegexValidator(regex=r'^\d{9,16}$', message="Account number must be between 9 and 16 chars long")
    pincode_regex = RegexValidator(regex=r'^\d{6}$', message="Pin code must be entered in the format: 110049")

    client                  = models.ForeignKey(Clientmaster, on_delete=models.CASCADE, related_name='client', blank=True, null=True)
    distribution            = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='distribution', blank=True, null=True)
    Superdistributor        = models.ForeignKey(Superdistributor, on_delete=models.CASCADE, related_name='Superdistributor', blank=True, null=True)
    employee                = models.ForeignKey(Employeemaster, on_delete=models.CASCADE, related_name='Employeemaster', blank=True, null=True)
    reference               = models.ForeignKey(Referencemaster, on_delete=models.CASCADE, related_name='Employeemaster', blank=True, null=True)
    name                    = models.CharField(max_length=40)
    branch_name             = models.CharField(max_length=40)
    branch_city             = models.CharField(max_length=35)
    account_type            = models.CharField(max_length=2, choices=ACCOUNTTYPE, default='SB', blank=False)
    account_number          = models.CharField(max_length=20, validators=[account_number_regex], blank=False)

    ifsc_code               = models.CharField(max_length=11, validators=[ifsc_code_regex], blank=False, unique=True)
    micr_code               = models.CharField(max_length=9, validators=[micr_code_regex], blank=True)
    anr_no                  = models.CharField(max_length=15, blank=True, null=True)
    anr_valid               = models.DateField(null=True, blank=True)

    created                 = models.DateTimeField(auto_now=True)
    updated                 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name