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
        print(digit_prefix)
        return hours, minutes, digit_prefix

def output(hours, minutes, prefix, days_later):
    res = hours + ":" + minutes 
    res += " "+"".join(prefix)
    if days_later == 1:
        res += " " + "".join("(next day)")
    elif days_later > 1:
        res += " " + "".join(f"({days_later} days later)")
    return res

#функция для сложения минут
def calculate_minutes(s_min, d_min):
    res = int(s_min) + int(d_min)
    new_hours = 0
    if res >= 60:
        new_min = res % 60 
        new_hours += res // 60
        if new_min < 10:
            new_min = "0" + str(new_min)
        return new_hours, str(new_min)
    return new_hours, str(res)

def calculate_hours(s_hours, d_hours, dd_pref, n_hours=0):

    res = int(s_hours) + int(d_hours) + n_hours
    if res > 12:
        print("Gotcha", dd_pref)
        pref_d = 0
        if res % 12 == 0:
            f_hours = 12
        else:
            f_hours = res % 12
        print(res)
        pref_d += res // 24

        if pref_d % 2 ==0:
            f_pref = "PM"
        else:
            f_pref = "AM"
        return f_pref, str(f_hours), pref_d
    
    if dd_pref % 2== 0:
        pref_d = "PM"
    else:
        pref_d = "AM"

    return pref_d, str(res)

#основная функция
def add_time(start, duration):
    count_dpr = 0
    start_hours, start_minutes, start_prefix = time_split(start, True)
    print(start_hours, start_minutes, start_prefix)
    duration_hours, duration_minutes = time_split(duration)
    print(duration_hours, duration_minutes)
    check_list = [(calculate_minutes(start_minutes, duration_minutes))]
    add_hours = check_list[0][0]
    final_minutes = check_list[0][1]
    print(check_list)
    check_list1 = [(calculate_hours(start_hours, duration_hours, start_prefix, add_hours))]
    # print(check_list1, "первый - перфикс, второй часы")
    add_prefix_digit = check_list1[0][0]
    final_hours = check_list1[0][1]
    print(len(check_list))
    if len(check_list1[0]) > 2:
        count_dpr = check_list1[0][2]
    
    new_time = output(final_hours, final_minutes, add_prefix_digit, count_dpr) #часы, минуты, префикс(AM/PM), количество дней 
    
    return new_time

start_input = "11:59 AM"
duration_input = "24:05"

print(add_time(start_input, duration_input))