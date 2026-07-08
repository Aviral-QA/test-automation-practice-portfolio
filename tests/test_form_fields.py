from pages.form_page import FormPage

def test_fill_name_field(page):
    form = FormPage(page)
    form.goto()
    form.fill_name("Aviral Gupta")
    assert form.name_field.input_value() == "Aviral Gupta"

def test_fill_email_field(page):
    form = FormPage(page)
    form.goto()
    form.fill_email("aviral@gmail.com")
    assert form.fill_email.input_value() == "aviral@gmail.com"

def test_fill_phone_field(page):
    form = FormPage(page)
    form.goto()
    form.fill_phone("9639348524")
    assert form.fill_phone.input_value() == "9639348524"

def test_check_tuesday_checkbox(page):
    form = FormPage(page)
    form.goto()
    form.check_tuesday()
    assert form.tuesday_checkbox.is_checked()

