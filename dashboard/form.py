from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from .models import toDoList, patient, case
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class patientRegForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(patientRegForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['Gender'] = '1'
        self.initial['Age'] = '18-24'
        # self.initial['Pallor'] = '0'
        # self.initial['Icterus'] = '0'
        # self.initial['Cyanosis'] = '0'
        # self.initial['Clubbing'] = '0'
        # self.initial['Lymphadenopathy'] = '0'
        # self.initial['ThyroidE'] = '0'
        # self.initial['PeripheralP'] = '0'
        # self.initial['Csign'] = '0'
        # self.initial['Tsign'] = '0'
        # self.initial['Petechiae'] = '0'
        # self.initial['Purpura'] = '0'
        # self.initial['Acanthosis'] = '0'
        # self.initial['SkinTags'] = '0'

    YESNO_CHOICES = ((1, 'Yes'), (0, 'No'))
    GENDER_CHOICES = ((1, 'Male'), (0, 'Female'))
    HEIGHT_CHOICES = (
    # ('ftin','ft in'),
    ('in', 'inches'),
    ('cm','cms'),
    )
    WEIGHT_CHOICES = (
    ('kg','kg'),
    ('lb', 'lb'),
    )
    THYROID_CHOICES = ((1, 'Diffuse'), (0, 'Nodular'))
    AGE_CHOICES = (
    ('0-2','0-2 years'),
    ('3-6', '3-6 years'),
    ('7-12','7-12 years'),
    ('13-17','13-17 years'),
    ('18-24','18-24 years'),
    ('25-34','25-34 years'),
    ('35-44','35-44 years'),
    ('45-54','45-54 years'),
    ('55-64','55-64 years'),
    ('65above','65 years and above'),
    )

    #patientId = forms.CharField(label='Patient Id')

    Gender = forms.TypedChoiceField(
                     choices=GENDER_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Age = forms.ChoiceField(choices=AGE_CHOICES)

    Pulse = forms.FloatField(label='Pulse', widget=forms.NumberInput(attrs={'type':'number'}))
    BloodP = forms.FloatField(label='Blood Pressure', widget=forms.NumberInput(attrs={'type':'number'}))
    RespirationR = forms.FloatField(label='Respiration Rate', widget=forms.NumberInput(attrs={'type':'number'}))
    Height = forms.FloatField(label='Height', widget=forms.NumberInput(attrs={'type':'number'}))
    HeightUnits = forms.ChoiceField(choices=HEIGHT_CHOICES)
    Weight = forms.FloatField(label='Weight', widget=forms.NumberInput(attrs={'type':'number'}))
    WeightUnits = forms.ChoiceField(choices=WEIGHT_CHOICES)
    # BMI = forms.CharField(label='BMI')

    Pallor = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )


    Icterus = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Cyanosis = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Clubbing = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Lymphadenopathy = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    ThyroidE = forms.TypedChoiceField(
                     choices=THYROID_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    PeripheralP = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Csign = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Tsign = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Petechiae = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Purpura = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    Acanthosis = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )

    SkinTags = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), coerce=int
                )


    # email = forms.EmailField(required = True)
    # first_name = forms.CharField(required = False)
    # last_name = forms.CharField(required = False)
    # birtday = forms.DateField(required = False)



    class Meta:
        model = case
        fields = ('Pulse','Gender') 
    # def save(self,commit = True):   
    #     user = super(patientRegForm, self).save(commit = False)
    #     user.email = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.birthday = self.cleaned_data['birthday']


    #     if commit:
    #         user.save()

    #     return user

class toDoListForm(forms.ModelForm):
    toDoPost = forms.CharField(label='Add new task')

    class Meta:
        model = toDoList
        fields = ('toDoPost',)

class openCaseForm(forms.ModelForm):
    openPatientId = forms.CharField(label='')

    class Meta:
        model = patient
        fields = ('openPatientId',)