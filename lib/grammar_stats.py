class GrammarStats:
    def __init__(self):
        self._correct_text_amount = 0
        self._incorrect_text_amount = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text == "":
            raise Exception("Cannot check empty string")
        if text[0].isupper() and text[-1] == '.':
            self._correct_text_amount += 1
            return True
        self._incorrect_text_amount += 1
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        total_amount = self._correct_text_amount + self._incorrect_text_amount
        return int((self._correct_text_amount / total_amount) * 100)
