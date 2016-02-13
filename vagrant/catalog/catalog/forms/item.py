from catalog.forms import CSRFForm

from wtforms import Form, TextField, TextAreaField, SelectField, FileField, validators

class ItemForm(CSRFForm):

    name = TextField("Name", [validators.Required(), validators.Length(min = 5, max = 120)])

    description = TextAreaField("Description", [validators.Required(), validators.Length(min = 10)])

    category_id = SelectField("Category", coerce = int)

    image = FileField("Image")
