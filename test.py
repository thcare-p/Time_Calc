# def calculate_hours(s_hours, d_hours, start_from_prefix, n_hours=0):

#     res = int(s_hours) + int(d_hours) + n_hours
#     if res > 12:
#         print("Gotcha", start_from_prefix)
#         if res % 12 == 0:
#             final_hours = 12
#         else:
#             final_hours = res % 12
#         final_days = (res) // 12

#         if final_days % 2 == 0:
#             final_prefix = "PM"
#         else:
#             final_prefix = "AM"
#         if final_days > 2:
#             final_days = (start_from_prefix + final_days) // 2
        
#         return final_prefix, str(final_hours), final_days
    
#     if start_from_prefix % 2== 0:
#         final_days = "PM"
#     else:
#         final_days = "AM"

#     return final_days, str(res)

# start_input = "1:55 AM"
# duration_input = "4:00"

# print(calculate_hours(11, 3, 1, 1), "финальный префикс, часы, кол-вод ней")
# # print(calculate_hours(duration_input))
days_later = 1
exact_day = "saTurday"
days = {
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wendsday": "Wendsday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday"
    }
digit_day = {
    1:'Monday',
    2:'Tuesday',
    3: 'Wendsday',
    4:'Thursday',
    5: 'Friday',
    6: 'Saturday',
    0: 'Sunday'
}
day = days[exact_day.lower()]
count = 0
for i in range(len(digit_day)):
    if day == digit_day[i]:
        exact_day = i
res = (exact_day + days_later) % 7
print(digit_day[res])
print(res)