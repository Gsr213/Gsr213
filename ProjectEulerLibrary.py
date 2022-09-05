import math

class PE_Library():
        
    def sum_list(self, list_of_numbers):
        total = 0
        for n in list_of_numbers:
            if not self.check_int_or_float(n):
                print("ERROR: input is not a number!!")
                return
            total += n
        return total

    def check_int_or_float(self, n):
        if isinstance(n, int):
            return True
        if isinstance(n, float):
            return True
        return False