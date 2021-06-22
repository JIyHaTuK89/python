import re

class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
         cls.date = date
         pattern = r'(?:[0-9]{4})|(?:[0-9]{2})'
         int_date = re.findall(pattern, date)
         result = map(int, int_date)
         return tuple(result)
         #Ниже вариант через datetime, не знаю как лучше
         #cls.date = date
         #dt = DT.datetime.strptime(date, '%d-%m-%Y')
         #return dt.strftime('%d-%m-%Y')

    @staticmethod
    def is_valid_date(day, month, year):
        days_31 = [1, 3, 5, 7, 8, 10, 12]
        days_30 = [4, 6, 9, 11]
        days_28_29 = [2]
        assert month > 0 or month <= 12
        if month in days_31:
            if day < 0 or day >= 31:
                return False
        if month in days_30:
            if day < 0 or day >= 30:
                return False
        if month in days_28_29 and year % 4:
            if day < 0 or day >= 28:
                return False
            elif day < 0 or day >= 29:
                return False
        return True
        #Переписал еще под assert, тоже не знаю какой нужен
        # def is_valid_date(day, month, year):
        #     days_31 = [1, 3, 5, 7, 8, 10, 12]
        #     days_30 = [4, 6, 9, 11]
        #     days_28_29 = [2]
        #     assert 0 < month <= 12
        #     if month in days_31:
        #         assert 0 < day <= 31
        #     elif month in days_30:
        #         assert 0 < day <= 30
        #     elif month in days_28_29 and year % 4:
        #         assert 0 < day <= 28
        #     else:
        #         assert 0 < day <= 29


if __name__ == '__main__':
    a = Date('29-02-1996')
    b = Date.date_to_int('29-02-1996')
    print(b)
    print(Date.is_valid_date(*b))