from base_objects.input_object import InputObj


class StringValueInp(InputObj):
    def matches_query(self, gets_inp):
        if gets_inp is not None:
            if gets_inp.full_match:
                if gets_inp.case_sensitive:
                    return self.value == gets_inp.value
                else:
                    return self.value.lower() == gets_inp.value.lower()
            else:
                if gets_inp.case_sensitive:
                    return gets_inp.value in self.value
                else:
                    return gets_inp.value.lower() in self.value.lower()
        return True