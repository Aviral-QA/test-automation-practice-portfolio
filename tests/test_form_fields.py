from pages.form_page import FormPage

def test_fill_name_field(page):
    form = FormPage(page)
    form.goto()
    form.fill_name("Aviral Gupta")
    assert form.name_field.input_value() == "Aviral Gupta"

def test_fill_email_field(page):
    form = FormPage(page)
    form.goto()
    form.fill_name("aviral@outlook.com")
    assert form.name_field.input_value() == "aviral@outlook.com"

def test_check_tuesday_checkbox(page):
    form = FormPage(page)
    form.goto()
    form.check_tuesday()
    assert form.tuesday_checkbox.is_checked()

