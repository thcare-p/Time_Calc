#в какой-то из функции необходимо будет делать рекурсию, так как при значениях, где увеличивается сразу несколько дней, должны меняться знаки AM/PM.
#Хотя возможен вариант подсчёта количства изменений и в последствии примитивного обозначения времени
#Дни надо будет закинуть в dict{}
def time_split(start_s, prefix=False):
    if not prefix:
        # _list = list(start_s)
        # print(_list)
        hours = start_s[0]
        minutes = start_s[2] + start_s[3]
        return hours, minutes
    else:
        start_split = start_s.split()#мы делим начальную строку на лист по пробелу, а потом по :
        print(start_split)
        start_prefix = start_split[1]
        if start_prefix == "AM":
            digit_prefix = 1
        else:
            digit_prefix = 2
        start_s_split = start_split[0].split(":")
        hours = start_s_split[0]
        minutes = start_s_split[1]

        return hours, minutes, digit_prefix
        
            
#функция для проверки присваемого значения AM/PM   
def reset_time(hours):
    pass
#функция для смены дня в последствии сочетания 
def change_day(n, n1, prefix):
    #как-то надо обдумать какую-никакую рекурсию
    pass

#основная функция
def add_time(start, duration):
    start_hours, start_minutes, start_prefix = time_split(start, True)
    duration_hours, duration_minutes = time_split(duration)
    return start_hours, start_minutes, start_prefix,  duration_hours, duration_minutes

start_input = "3:00 PM"
duration_input = "3:00"

# start_input = input("Add start time: ")
# duration_input = input("Write amount of hours: ")

print(add_time(start_input, duration_input))