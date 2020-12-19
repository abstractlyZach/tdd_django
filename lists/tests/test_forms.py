import pytest

from lists.forms import EMPTY_ITEM_ERROR
from lists.forms import ItemForm


def test_form_item_input_has_placeholder_and_css_classes():
    form = ItemForm()
    assert 'placeholder="Enter a to-do item"' in form.as_p()
    assert 'class="form-control input-lg"' in form.as_p()


def test_form_validation_for_blank_items():
    form = ItemForm(data={"text": ""})
    assert not form.is_valid()
    assert form.errors["text"] == [EMPTY_ITEM_ERROR]
