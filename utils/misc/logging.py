import logging
import xlsxwriter
import datetime as dt
workbook = xlsxwriter.Workbook('users.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Data')
worksheet.write(0, 1, 'Time')
worksheet.write(0, 2, 'User')
worksheet.write(0, 3, 'User ID')


def log_user_info(user_id, first_name, last_name, count, sheet):
    sheet.write(count, 0, str(dt.datetime.now().date()))
    sheet.write(count, 1, str(dt.datetime.now().time())[0:8])
    sheet.write(count, 2, f'{first_name} {last_name}')
    sheet.write(count, 3, f'{user_id}')


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )
