import csv
from pyrogram_app.config import CSV_PATH
import datetime


class Employees:
    def __init__(self) -> None:
        self.employees = []
        actual_employee = {
                'name': '',
                'shifts': {}
                }
        employees_list = self.get_employer_list(CSV_PATH) 
        # Creating 2/2 employees list
        for employee in employees_list:
            for current_employee in employee:
                if len(employee[current_employee]) > 2:
                    actual_employee['name'] = employee[current_employee]
                else:
                    actual_employee['shifts'][current_employee] = employee[current_employee]
            self.employees.append(actual_employee)
            actual_employee = {
                'name': '',
                'shifts': {}
            }

    def is_on_work(self, name: str) -> list:
        today_datetime = datetime.datetime.now()
        current_day = str(today_datetime.day)
        result_datetime = None
        result = [False, {'date': result_datetime, 'shift': None}]
        for current_employee in self.employees:
            if current_employee['name'] == name:
                if current_employee['shifts'][current_day] != '':
                    result[0] = True
                else:
                    last_month_day = len(current_employee['shifts']) + 1 
                    for next_day in range(int(current_day), last_month_day):
                        next_shift = current_employee['shifts'][str(next_day)]
                        if next_shift != '' and result_datetime is None:
                            result_datetime = datetime.datetime(
                                    year=today_datetime.year,
                                    month=today_datetime.month,
                                    day=next_day
                            )
                            result[1]['date'] = result_datetime
                            result[1]['shift'] = next_shift[0]
                return result

    @staticmethod
    def get_employer_list(path:str) -> list:
        with open(path, encoding = 'utf-8-sig') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=';')
            employer_list = list(csv_reader)
            return employer_list

