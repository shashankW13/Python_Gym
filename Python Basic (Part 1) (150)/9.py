import datetime

exam_st_date = (11, 12, 2014)
format = "%d/%m/%Y"
d, m, y = exam_st_date
exam_date = datetime.date(y, m, d)
print(f'The examination will start from : {datetime.date.strftime(exam_date, format)}')
