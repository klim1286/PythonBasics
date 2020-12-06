class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_in(cls, str_date):
        try:
            date = str_date
            m = list(map(int, date.split('-')))
            if len(m) == 3:
                return cls(m)
            else:
                return print('Ошибка!')
        except ValueError:
            return print('Ошибка!')

    @staticmethod
    def date_check(obj):
        if 31 >= obj.date[0] > 0:
            if 12 >= obj.date[1] > 0:
                if 2999 >= obj.date[2] > 999:
                    return True
                return False
            else:
                return False
        else:
            return False


d_now = Date.date_in('03-18-2019')
print(d_now.date_check(d_now))
