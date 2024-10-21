#в какой-то из функции необходимо будет делать рекурсию, так как при значениях, где увеличивается сразу несколько дней, должны меняться знаки AM/PM.
#Хотя возможен вариант подсчёта количства изменений и в последствии примитивного обозначения времени
#Дни надо будет закинуть в dict{}
def time_split(start_s, prefix=False):
    if not prefix:
        hours = start_s[0]
        minutes = start_s[2] + start_s[3]
        return hours, minutes
    else:
        start_split = start_s.split()#мы делим начальную строку на лист по пробелу, а потом по :
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
  
#функция для сложения минут
def calculate_minutes(s_min, d_min):
    res = int(s_min) + int(d_min)
    if res >= 60:
        new_min = res % 60 
        new_hours = res // 60
        return new_hours, new_min
    return res

def calculate_hours(s_hours, d_hours, n_hours = 0):
    res = int(s_hours) + int(d_hours) + int(n_hours)
    if res > 12:
        f_hours = res % 12
        pref_d = res // 12
        return f_hours, pref_d
    return res

#основная функция
def add_time(start, duration):
    
    start_hours, start_minutes, start_prefix = time_split(start, True)
    duration_hours, duration_minutes = time_split(duration)
    print(start_minutes, duration_minutes)
    check_list = [(calculate_minutes(start_minutes, duration_minutes))]
    print(check_list)
    
    if len(check_list) > 1:
        add_hours = check_list[0]
        final_minutes = check_list[1]
    else:
        final_minutes = check_list[0]
    
    check_list1 = [(calculate_hours(start_hours, duration_hours))]
    print(check_list1)
    if len(check_list1) > 1:
        final_hours = check_list1[0]
        add_prefix_digit = check_list1[1]
    else:
        final_hours = check_list1[0]
        
    return final_hours, final_minutes


start_input = "3:10 PM"
duration_input = "3:30"

# start_input = input("Add start time: ")
# duration_input = input("Write amount of hours: ")

print(add_time(start_input, duration_input))