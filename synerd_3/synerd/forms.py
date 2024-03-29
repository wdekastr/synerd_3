from django import forms

YEARS=[x for x in range(1920,2019)]

STATE_CHOICES=[
    ('', 'State'),
    ('AL', 'AL - Alabama'),('AK', 'AK - Alaska'),
    ('AZ', 'AZ - Arizona'),('AR', 'AR - Arkansas'),
    ('CA', 'CA - California'),('CO', 'CO - Colorado'),
    ('CT', 'CT - Connecticut'),('DE', 'DE - Delware'),
    ('FL', 'FL - Florida'),('GA', 'GA - Georgia'),
    ('HI', 'HI - Hawaii'),('ID', 'ID - Idaho'),
    ('IL', 'IL - Illinois'),('IN', 'IN - Indiana'),
    ('IA', 'IA - Iowa'),('KS', 'KS - Kansas'),
    ('KY', 'KY - Kentucky'),('LA', 'LA - Louisiana'),
    ('ME', 'ME - Maine'),('MD', 'MD - Maryland'),
    ('MA', 'MA - Massachusetts'),('MI', 'MI - Michigan'),
    ('MN', 'MN - Minnesota'),('MS', 'MS - Mississippi'),
    ('MO', 'MO - Missouri'),('MT', 'MT - Montana'),
    ('NE', 'NE - Nebraska'),('NV', 'NV - Nevada'),
    ('NH', 'NH - New Hampshire'),('NJ', 'NJ - New Jersey'),
    ('NM', 'NM - New Mexico'),('NY', 'NY - New York'),
    ('NC', 'NC - North Carolina'),('ND', 'ND - North Dakota'),
    ('OH', 'OH - Ohio'),('OK', 'OK - Oklahoma'),
    ('OR', 'OR - Oregon'),('PA', 'PA - Pennsylvania'),
    ('RI', 'RI - Rhode Island'),('SC', 'SC - South Carolina'),
    ('SD', 'SD - South Dakota'),('TN', 'TN - Tennessee'),
    ('TX', 'TX - Texas'),('UT', 'UT - Utah'),
    ('VT', 'VT - Vermont'),('VA', 'VA - Virginia'),
    ('WA', 'WA - Washington'),('WV', 'WV - West Virginia'),
    ('WI', 'WI - Wisconsin'),('WY', 'WY - Wyoming'),
        ]

class LoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Create a username..'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a password..', 'onkeyup': 'passwordCheck()'}))
    First_Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name..'}))
    Middle_Name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Middle name..'}))
    Last_Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name..'}))
    Address_Line_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Address Line 1..'}))
    Address_Line_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter Address Line 2..'}))
    City = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter City..'}))
    State = forms.CharField(widget=forms.Select(choices=STATE_CHOICES))
    Zip_Code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zip Code..'}))
    #Email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@domain.com'}))
    Email = forms.EmailField()
    Home_Phone_Number = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Cell Phone #..'}))
    Cell_Phone_Number = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Cell Phone #..'}))
    #Date_Of_Birth = forms.DateField(required=False, widget=forms.SelectDateWidget(empty_label=("Year", "Month", "Day",),years=YEARS,))
    Date_Of_Birth = forms.DateField(label='Date of Birth',
         widget=forms.DateInput(format='%m/%d/%Y',attrs={'placeholder': '03/31/1989'}),
         input_formats=['%m/%d/%Y',])

class OfficeForm(forms.Form):
    Office_Name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Office Name..'}))
    Office_Code = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Office Code..'}))
    Attribution = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Specify Attribution..'}))

class OfficerForm(forms.Form):
    Subscriber_ID = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Subscriber ID..'}))
    Office_Code = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Office Code..'}))
    Start_Date = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Start Date..'}))
    End_Date = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify End Date..'}))
    

class OrgForm(forms.Form):
    Organization_Code = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Organization Code..'}))
    Organization_Name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Organization Name..'}))
    Description = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter a description..'}))
    Date_Joined = forms.DateField(required=False, input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Date Joined..'}))
    Address_Line_1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter Address Line 1..'}))
    Address_Line_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter Address Line 2..'}))
    City = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter City..'}))
    State = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter State..'}))
    Zipcode = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter Zip..'}))
    Phone_Number = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone Number..'}))

class OrgMemForm(forms.Form):
    Organization_Code = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Organization Code..'}))
    Subscriber_ID = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Subscriber ID..'}))
    Membership_Start_Date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Membership Start Date..'}))
    Membership_End_Date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Membership End Date..'}))
    Native_Country = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter Native Country..'}))
    Delegate = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Yes / No'}))
    Delegate_For = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter Service Code If Delegate..'}))

class SubscriberForm(forms.Form):
    Subscriber_ID = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Subscriber ID..'}))
    Organization_Code = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Enter your Organization Code..'}))
    Service_Code = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Specify Service Code..'}))
    Subscription_Request_Date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Subscription Request Date..'}))
    Subscription_Start_Date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Subscription Start Date..'}))
    Subscription_End_Date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Subscription End Date..'}))
    Motif_Of_Cancellation = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': 'Specify Motif Of Cancellation..'}))

