grades = [98,38,69]
max_grades = [100,50,75]

#list for later percent list of assignemnts added
earned_perc = []

#number out of 100 for grade and grey space
final_percent = 0
grey_percent = 0

#function to calculate percentages from two lists, one of earned points, and one of max points
def calc_perc (grades, max_grades):
    i = 0
    while i < len(grades):
        earned_perc.append(grades[i]/max_grades[i])
        i += 1

    return earned_perc

#function to calculate average of all percentages from calc_perc
def calc_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

final_percent = round((calc_average(calc_perc(grades, max_grades))), 2)
final_percent *= 100

#function to calculate grey space from what is left from calc_average
def calc_grey (final_percent):
    return 100 - final_percent

grey_percent = calc_grey(final_percent)

#outputs for debug, one for grey space, one for percentage
print("final percent " + str(final_percent))
print("grey percent " + str(grey_percent))
