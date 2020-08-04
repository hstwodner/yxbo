from django import forms


class UploadFileForm(forms.Form):
    upfile = forms.FileField(label='文件')

