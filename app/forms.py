# coding:utf-8
from django import forms
from DjangoUeditor.widgets import UEditorWidget
from DjangoUeditor.forms import UEditorField, UEditorModelForm
from models import News


class TestUEditorForm(forms.Form):
    title = forms.CharField(label=u'标题')
    content = UEditorField(label=u"内容",widget=UEditorWidget({"width":600, "height":100, "imagePath":'aa', "filePath":'bb', "toolbars":"full"}))
    author = forms.CharField()
    time = forms.DateTimeField()
    read_count = forms.IntegerField()


class UEditorTestModelForm(UEditorModelForm):
    class Meta:
        model = News
        fields = '__all__'
