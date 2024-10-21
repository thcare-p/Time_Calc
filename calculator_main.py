#в какой-то из функции необходимо будет делать рекурсию, так как при значениях, где увеличивается сразу несколько дней, должны меняться знаки AM/PM.
#Хотя возможен вариант подсчёта количства изменений и в последствии примитивного обозначения времени
#Дни надо будет закинуть в dict{}
def time_split(start_s, prefix):
    if not prefix:
        _list = list(start_s)
        start_split = _list[0].split(":")
        for time in start_split:
            hours, minutes = time
        return hours, minutes
    else:
        start_split = start_s.split()#мы делим начальную строку на лист по пробелу, а потом по :
        start_prefix = start_split[1]
        if start_prefix == "AM":
            digit_prefix = 1
        else:
            digit_prefix = 2
        start_s_split = start_split[0].split[":"]
        for time in start_s_split:
            hours, minutes = time 
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
    start_hours, start_minutes = time_split(start, True)
    duration_hours, duration_minutes = time_split(duration)
    return start_hours, start_minutes

start_input = "3:10 PM"
duration_input = "3:00"

# start_input = input("Add start time: ")
# duration_input = input("Write amount of hours: ")

print(add_time(start_input, duration_input))