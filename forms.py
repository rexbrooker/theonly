from django import forms
from theonly.models import MenuModel, Brewery_Graphic, Brewery, Beverage_Style, Beverage_Serving_Size, Beverage, Beverage_Serving_Graphic
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button, Div, HTML
from crispy_forms.bootstrap import FormActions, AppendedText


class MenuForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_method = 'POST'
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Div(
                Div(
                    HTML('<h4 class="panel-title"><a data-toggle="collapse" data-parent="#accordion" href="#collapse{{forloop.counter}}">Tap {{forloop.counter}}{{ beverage }}'),
                    HTML('</a></h4>'),
                    css_class="panel-heading",
                ),
                Div(
                    HTML('<div id="collapse{{forloop.counter}}" class="panel-collapse collapse"><form method="post" action="">'),
                    HTML('{% csrf_token %}{{ form.id }}'),
                    Field('tap_number', css_class="tap_number", ),
                    Field('brewery_name', css_class='brewery_name'),
                    Field('beverage_name', css_class='beverage_name'),
                    Field('beverage_type', css_class='beverage_type'),
                    Div(
                        Div('beverage_price_1', css_class='col-md-6',),
                        Div('beverage_serving_size_1', css_class='col-md-6',),
                        css_class='row',
                    ),
                    Div(
                        css_class='beverage_serving_graphic_1',
                    ),
                    Div(
                        css_class='beverage_color_1',
                    ),
                    Field('two_serving_sizes', css_class='two_serving_sizes'),
                    Field('beverage_price_2', css_class='beverage_price_2'),
                    Div(
                        template='theonly/crispy-beverage_size.html',
                        css_class='beverage_serving_size_2',
                    ),
                    Div(
                        template='theonly/crispy-glass_size.html',
                        css_class='beverage_serving_graphic_2',
                    ),
                    Div(label="Select beverage color",
                        template='theonly/crispy-inline_color_picker.html',
                        css_class='beverage_color_2',
                        ),
                    Field('tap_number_subtext', css_class="tap_number_subtext"),
                    FormActions(
                        Submit('save', 'Save changes', css_class='button white'),
                        Button('cancel', 'Cancel'),
                    ),
                    HTML('</form></div>'),
                    css_class="panel-body",
                ),
                css_class="panel panel-default",
            ),
        )

    beverage_serving_size_1 = forms.IntegerField(widget=forms.HiddenInput())
    beverage_serving_size_2 = forms.IntegerField(widget=forms.HiddenInput())
    tap_number = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = MenuModel
        fields = [
            'tap_number',
            'brewery_name',
            'beverage_name',
            'beverage_type',
            'beverage_price_1',
            'beverage_serving_size_1',
            'two_serving_sizes',
            'beverage_price_2',
            'beverage_serving_size_2',
            'tap_number_subtext',
        ]
        # Field('brewery', css_class="brewery"),
        # Field('beverage', css_class="beverage"),
        # Field('beverage_serving_size', css_class="beverage_serving_size"),
        # Field('beverage_serving_graphic', css_class="beverage_serving_graphic"),

        # 'brewery',
        # 'beverage',
        # 'beverage_serving_size',
        # 'beverage_serving_graphic',


class Brewery_GraphicForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Brewery_GraphicForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Brewery_Graphic
        fields = [
            'brewery_graphic',
        ]


class BreweryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BreweryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Brewery
        fields = [
            'brewery_name',
            'brewery_graphic',
        ]


class Beverage_StyleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Beverage_StyleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Beverage_Style
        fields = [
            'beverage_style',
        ]


class Beverage_Serving_SizeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Beverage_Serving_SizeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Beverage_Serving_Size
        fields = [
            'beverage_serving_size',
        ]


class Beverage_Serving_GraphicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Beverage_Serving_GraphicForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Beverage_Serving_Graphic
        fields = [
            'beverage_serving_graphic',
        ]


class BeverageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BeverageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            'brewery',
            'beverage_name',
            'beverage_style',
            'beverage_color',
            AppendedText('beverage_abv', '%'),
        )

    class Meta:
        model = Beverage
        fields = [
            'brewery',
            'beverage_name',
            'beverage_style',
            'beverage_abv',
            'beverage_color',
        ]
