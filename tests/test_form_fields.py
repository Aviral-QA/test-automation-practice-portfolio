from pages.form_page import FormPage

def test_fill_name_field(page):
    form = FormPage(page)
    form.goto()
    form.fill_name("Aviral Sharma")
    assert form.name_field.input_value() == "Aviral Sharma"

def test_check_tuesday_checkbox(page):
    form = FormPage(page)
    form.goto()
    form.check_tuesday()
    assert form.tuesday_checkbox.is_checked()