from pages.form_page import FormPage

def test_select_country_dropdown(page):
    form = FormPage(page)
    form.goto()
    form.select_country("India")
    assert form.country_dropdown.input_value() == "india"