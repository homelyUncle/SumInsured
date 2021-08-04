import datetime as dt
from termcolor import colored


def get_date(str_date: str) -> dt.datetime:
    """
    get the date as a string,
    return it as a datetime format
    """
    return dt.datetime.strptime(str_date, '%d-%m-%Y')


def calc_days(start_date: dt.date, end_date: dt.date) -> int:
    """
    returns diffrent in days by integer
    """
    return (end_date - start_date).days


def calc(sum_insurance: int, percent: float, days: int) -> float:
    """
    function calculate sum insured 
    by the end of insurance contract
    and returns sum in float type
    """
    while days > 0:
        sum_insurance -= sum_insurance * (percent / 100)
        days -= 1
    return round(sum_insurance, 2)


def get_sum_insurance() -> int:
    """
    get the value of the car,
    return the sum as a number
    """
    sum_insured = 0
    input_text = input('Input the sum insured represented in insurance contract\n'
                       '(you can use spaces for your convenience): ')
    try:
        sum_insured = int(input_text.replace(' ', ''))
    except ValueError:
        print('Please enter numbers and not letters!')
        get_sum_insurance()
    return sum_insured


def get_percent() -> float:
    """
    get the percent represented in insurance contract
    """
    percent = 0.0
    input_text = input('Input the percent of decreasing sum '
                       'insured represented in insurance contract: ')
    try:
        percent = float(input_text)
    except ValueError:
        print('Please enter numbers and not letters!')
        get_percent()
    return percent


def get_start_date() -> str:
    input_text = input('Input the estimated start date of the insurance contract in format [DD-MM-YYYY]: ')
    if check_date(input_text):
        return input_text
    else:
        get_start_date()


def get_end_date() -> str:
    input_text = input('Input the estimated end date of the insurance contract in format [DD-MM-YYYY]: ')
    if check_date(input_text):
        return input_text
    else:
        get_end_date()


def check_date(input_text: str) -> bool:
    splitted_text = input_text.split('-')
    for text in splitted_text:
        try:
            int(text)
        except:
            print('\nPlease input correct format date\n')
            return False
    return True


sum_insured = get_sum_insurance()       # получаем сумму страховки в виде целого числа

decrease_percent = get_percent()        # получаем процент уменьшения суммы в виде числа с плавающей запятой

start_date = get_date(get_start_date())  # получаем дату начала действия страховки

end_date = get_date(get_end_date())     # получаем дату окончания страховки

days = calc_days(start_date, end_date)

sum_at_the_end = calc(sum_insured, decrease_percent, days)  # подсчёт остаточной стоимости автомобиля

print(' - - - - - - - - -'
      '\nSum insured by the end of insurance contract is', colored(sum_at_the_end, 'yellow'),
      '\nDiffrence is', colored(round(sum_insured - sum_at_the_end, 2), 'red'))
