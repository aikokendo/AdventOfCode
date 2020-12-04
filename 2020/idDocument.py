import re

class IdDocument:
    def __init__(self, inputs, mandatory_fields, optional_fields,rules):
        self.mandatory = set(mandatory_fields)
        self.optional = set(optional_fields)
        self.fields = [i for i in str.replace(inputs,'\n',' ').split()]
        self.avail_fields = dict([i.split(':') for i in self.fields])
        self.avail_fields = set(list(self.avail_fields.keys()))
        self.rules = rules

    def checkAllFieldsValid(self):
        for field in self.fields:
            if not re.match(self.rules,field):
                return False
        return True

    def checkAllFieldsPresent(self):
        return self.mandatory.issubset(self.avail_fields)

    def checkValid(self):
        return self.checkAllFieldsValid() and self.checkAllFieldsPresent()
