from mptt.forms import MoveNodeForm

from django import forms

from qualitio.execute.models import TestRunDirectory, TestRun


class TestRunDirectoryForm(forms.ModelForm):
    class Meta:
        model = TestRunDirectory


class TestRunForm(forms.ModelForm):
    class Meta:
        model = TestRun

