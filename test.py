def calculate_hours(s_hours, d_hours, dd_pref, n_hours=0):

    res = int(s_hours) + int(d_hours) + n_hours
    if res > 12:
        print("Gotcha", dd_pref)
        pref_d = 0
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

start_input = "1:55 AM"
duration_input = "4:00"

print(calculate_hours(2, 48, 1, 0))
# print(calculate_hours(duration_input))