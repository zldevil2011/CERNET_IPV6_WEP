# coding:utf-8
from django import forms
from DjangoUeditor.widgets import UEditorWidget
from DjangoUeditor.forms import UEditorField, UEditorModelForm
from models import News


class TestUEditorForm(forms.Form):
    title = forms.CharField(label=u'标题')
    # content = UEditorField(label=u"内容",widget=UEditorWidget({"width":1000, "height":100, "imagePath":'aa', "filePath":'bb', "toolbars":"full"}))
    content=UEditorField("描述",initial="abc",width=500,height=100,filePath="images/itemImages/")
    author = forms.CharField()
    time = forms.DateTimeField()
    read_count = forms.IntegerField()


class UEditorTestModelForm(UEditorModelForm):
    class Meta:
        model = News
        fields = '__all__'
