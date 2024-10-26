def time_split(start_s, prefix=False):
    hours = ""
    minutes = ""
    if not prefix:
        for i in start_s:
            if i != ":":
                hours += str(i)
            else:
                index = start_s.index(":")
                break
        for i in range(index + 1, len((start_s))):
            minutes += start_s[i]
        return hours, minutes
    else:
        start_split = start_s.split()#мы делим начальную строку на лист по пробелу
        for i in start_split[0]:
            if i != ":":
                hours += str(i)
            else:
                index = start_split[0].index(":")
                break
        for i in range(index + 1, len((start_split[0]))):
            minutes += start_split[0][i]
        start_prefix = start_split[1]
        if start_prefix == "AM":
            digit_prefix = 1
        else:
            digit_prefix = 2
        return hours, minutes, digit_prefix

#функция для сложения минут
def calculate_minutes(s_min, d_min):
    res = int(s_min) + int(d_min)
    new_hours = 0
    if res >= 60:
        new_min = res % 60 
        new_hours = 1
        if new_min < 10:
            new_min = "0" + str(new_min)
        return new_hours, str(new_min)
    if res == 0:
        res = "0" + str(res)
    return new_hours, str(res)

def calculate_hours(s_hours, d_hours, start_from_prefix, n_hours=0):

    res = int(s_hours) + int(d_hours) + n_hours
    
    if res >= 12:
        if res % 12 == 0:
            final_hours = 12
        else:
            final_hours = res % 12
        final_days = (res // 12) + start_from_prefix

        if final_days % 2 == 0:
            final_prefix = "PM"
        else:
            final_prefix = "AM"
        
        output_days = 0
        if final_days > 2:
            output_days = final_days // 2
        
        return final_prefix, str(final_hours), output_days
    
    if start_from_prefix % 2== 0:
        final_days = "PM"
    else:
        final_days = "AM"

    return final_days, str(res)

def count_days(exact_day, amount_days_after):
    days = {
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday"
    }
    digit_day = {
        1:'Monday',
        2:'Tuesday',
        3: 'Wednesday',
        4:'Thursday',
        5: 'Friday',
        6: 'Saturday',
        0: 'Sunday'
    }
    day = days[exact_day.lower()]
    for i in range(len(digit_day)):
        if day == digit_day[i]:
            exact_day = i
    res = (exact_day + amount_days_after) % 7
    return digit_day[res]
    
def output(hours, minutes, prefix, days_later, add_day=''):
    res = hours + ":" + minutes 
    res += " "+"".join(prefix)
    if add_day:
        res += ", " + count_days(add_day, days_later)
    if days_later == 1:
        res += " " + "".join("(next day)")
    elif days_later > 1:
        res += " " + "".join(f"({days_later} days later)")
    return res

#основная функция
def add_time(start, duration, day=""):
    count_dpr = 0
    start_hours, start_minutes, start_prefix = time_split(start, True)
    duration_hours, duration_minutes = time_split(duration)
    check_list = [(calculate_minutes(start_minutes, duration_minutes))]
    add_hours = check_list[0][0]
    final_minutes = check_list[0][1]
    check_list1 = [(calculate_hours(start_hours, duration_hours, start_prefix, add_hours))]
    # print(check_list1, "первый - перфикс, второй часы")
    start_from_prefixix_digit = check_list1[0][0]
    final_hours = check_list1[0][1]
    if len(check_list1[0]) > 2:
        count_dpr = check_list1[0][2]
    
    new_time = output(final_hours, final_minutes, start_from_prefixix_digit, count_dpr, day) #часы, минуты, префикс(AM/PM), количество дней 
    
    return new_time

def main():
    start_input = input("Enter start time: ")
    duration_input = input("Enter duration time: ")
    answer = input("Would like to count days?(yes/no): ")
    if answer == "yes":
        day_input = input()
        print(add_time(start_input, duration_input, day_input))
        return
    else:
        print(add_time(start_input, duration_input))
        return

main()