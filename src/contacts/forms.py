from django import forms
from django.forms import ModelForm, Form
from django.contrib.contenttypes.generic import generic_inlineformset_factory as inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from contacts.models import Company, Person, Group, PhoneNumber, EmailAddress, WebSite, StreetAddress

class CompanyCreateForm(ModelForm):
	class Meta:
		model = Company
		fields = ('name', 'nickname', 'about')
	def __init__(self, *args, **kwargs):
		super(CompanyCreateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'
#  		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(
				'name','nickname', 'about',
				StrictButton('Add', type='submit', css_class='btn-default btn btn-primary col-lg-offset-2'),
)
class CompanyUpdateForm(ModelForm):
	class Meta:
		model = Company
		fields = ('name', )

	def __init__(self, *args, **kwargs):
		super(CompanyUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_class = 'form-inline'
  		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(Row(
				'name',
))



class PersonCreateForm(ModelForm):
	class Meta:
		model = Person
		fields = ('first_name', 'last_name', 'title', 'company', 'about')

	def __init__(self, *args, **kwargs):
		super(PersonCreateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'
#   		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(
				'title',
				'first_name',
				'last_name',
				'company',
				'about',
				StrictButton('Add', type='submit', css_class='btn-default btn btn-primary col-lg-offset-2'),
)


class PersonUpdateForm(ModelForm):
	class Meta:
		model = Person
		fields = ('first_name', 'last_name', 'title', 'company')
	
	def __init__(self, *args, **kwargs):
		super(PersonUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.error_text_inline = False
		self.helper.form_class = 'form-inline'
 		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(Row(
				'title',
				'first_name',
				'last_name',
				'company',
				'about',
))

class PhoneNumberForm(ModelForm):
	class Meta:
		model = PhoneNumber
		fields = ('phone_number', 'location')
	
	def __init__(self, *args, **kwargs):
		super(PhoneNumberForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.render_unmentioned_fields = True
		
		self.helper.form_class = 'form-inline'
 		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(Row(
				'phone_number',
				'location',
))

class EmailAddressForm(ModelForm):
	class Meta:
		model = EmailAddress
		fields = ('email_address', 'location')
	
	def __init__(self, *args, **kwargs):
		super(EmailAddressForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.render_unmentioned_fields = True
		
		self.helper.form_class = 'form-inline'
 		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(Row(
				'email_address',
				'location',
))

class WebSiteForm(ModelForm):
	class Meta:
		model = WebSite
		fields = ('url', 'location')
	
	def __init__(self, *args, **kwargs):
		super(WebSiteForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.render_unmentioned_fields = True
		self.helper.form_class = 'form-inline'
 		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(Row(
				'url',
				'location',
))

class StreetAddressForm(ModelForm):
	class Meta:
		model = StreetAddress
		fields = ('street',
				'street2', 'city',
				'province', 'postal_code',
				'country',
				 'location')
	
	def __init__(self, *args, **kwargs):
		super(StreetAddressForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.render_unmentioned_fields = True
		self.helper.error_text_inline = False
		self.helper.form_class = 'form-horizontal'
  		self.helper.field_template = 'bootstrap3/layout/inline_field.html' # needs to show errors otherwise...
		self.helper.layout = Layout(Row(
				'street',
				'street2', 'city',
				'province', 'postal_code',
				'country',
				'location',
))



class GroupCreateForm(ModelForm):
	class Meta:
		model = Group
		fields = ('name', 'about')

class GroupUpdateForm(ModelForm):
	class Meta:
		model = Group
		exclude = ('slug',)

PhoneNumberFormSet = inlineformset_factory(PhoneNumber, form=PhoneNumberForm, extra=1)
EmailAddressFormSet = inlineformset_factory(EmailAddress, form=EmailAddressForm, extra=1)
WebSiteFormSet = inlineformset_factory(WebSite, form=WebSiteForm, extra=1)
StreetAddressFormSet = inlineformset_factory(StreetAddress, form=StreetAddressForm, extra=1)