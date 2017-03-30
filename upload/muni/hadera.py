from muni import AbstractMuni
from fields import AmountField, CodeField, DescriptionField

class HaderaMuni(AbstractMuni):
    fields = {0: CodeField,
              1: DescriptionField,
              3: AmountField}  # TODO: make sure this is the right column number.

    fields_2016 = {0: CodeField,
                   1: DescriptionField,
                   2: AmountField}

    years = {2016: fields_2016,
             2015: fields,
             2014: fields}
    MUNI = 'hadera'

    def __init__(self,**kwargs):
        super(HaderaMuni, self).__init__(**kwargs)
        self.start_in_row.add_value(3)

