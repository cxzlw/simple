# Code by cxzlw

import datetime
import random
import re

import colors
import httpx

title = "Where Is My Teacher?"
description = "Find your teacher at SCIE using advanced technology."


def get_classroom(session):
    splited_lesson = session.split("(", maxsplit=1)
    classroom_and_teacher = splited_lesson[1]
    classroom = classroom_and_teacher.split(")(", maxsplit=1)[0]
    return classroom


def main():
    banner_str = (' _       ____                      ____        __  ___     \n| |     / / /_  ___  ________     /  _/'
                  '____   /  |/  /_  __\n| | /| / / __ \\/ _ \\/ ___/ _ \\    / // ___/  / /|_/ / / / /\n| |/ |/ / / /'
                  ' /  __/ /  /  __/  _/ /(__  )  / /  / / /_/ / \n|__/|__/_/ /_/\\___/_/   \\___/  /___/____/  /_/  '
                  '/_/\\__, /  \n                                                  /____/   \n  ______                _'
                  '_                 ___ \n /_  __/__  ____ ______/ /_  ___  _____   /__ \\\n  / / / _ \\/ __ `/ ___/ _'
                  '_ \\/ _ \\/ ___/    / _/\n / / /  __/ /_/ / /__/ / / /  __/ /       /_/  \n/_/  \\___/\\__,_/\\___/_'
                  '/ /_/\\___/_/       (_)   \n                                               \n'
                  )
    print(
        "".join(random.choice(
            (colors.CYAN, colors.DARK_CYAN, colors.RED, colors.GREEN, colors.DARK_GREEN, colors.YELLOW,
             colors.RESTORE,)) + x
                for x in banner_str))

    print(f"{colors.GREEN}Introduction:")
    print("Find your teacher at SCIE using advanced technology.")
    print("With this tool, you can know where your teacher is, \n"
          "    or predict where your teacher will be.")
    print("Datas are from SCIE Names(https://names.cxzlw.top).")
    print(f"{colors.RESTORE}")

    teacher_query = input(f"{colors.CYAN}Input your teachers name: {colors.RESTORE}")
    while not teacher_query:
        print(f"{colors.RED}Illegal input, please re-enter. {colors.RESTORE}")
        teacher_query = input(f"{colors.CYAN}Input your teachers name: {colors.RESTORE}")

    query_page = httpx.get(f"https://names.cxzlw.top/?query={teacher_query}").text
    teachers_and_profiles = re.findall(
        '<div class="relative p-4 bg-gray-100 rounded-lg shadow-xl dark:bg-gray-800 hover:left-0.5 hover:bottom-0.5 hover:shadow-2xl text-center">\n'
        ' {16}<p class="text-xl align-middle text-center font-bold">(.*?)</p>\n'
        ' {16}<p>Short Name: .*?</p>\n'
        ' {16}<p>Teacher ID: .*?</p>\n'
        ' {16}<a href="(.*?)" class="btn btn-outline mx-auto">View his/her profile\n'
        ' {20}here</a>\n'
        ' {12}</div>',
        query_page)

    print("Here is the list of relevant teachers: ")
    for i, (name, _) in enumerate(teachers_and_profiles):
        print(f"\t{i + 1}.\t{name}")

    def get_user_choice():
        inputed = input(
            f"{colors.CYAN}Please choose the teacher you want to find (1~{len(teachers_and_profiles)}): {colors.RESTORE}")
        while not (inputed.isnumeric() and 1 <= int(inputed) <= len(teachers_and_profiles)):
            print(f"{colors.RED}Illegal choice, please re-enter. {colors.RESTORE}")
            inputed = input(
                f"{colors.CYAN}Please choose the teacher you want to find (1~{len(teachers_and_profiles)}): {colors.RESTORE}")
        return int(inputed)

    teacher_and_profile = teachers_and_profiles[get_user_choice() - 1]
    print(f"{colors.GREEN}You chose {teacher_and_profile[0]}.")

    profile_page = httpx.get("https://names.cxzlw.top" + teacher_and_profile[1]).text
    periods = re.findall(
        '<tr>\n'
        ' {24}<th>(.*?)</th>\n'
        ' {24}<td class="border-2 w-fit">(.*?)</td>\n'
        ' {24}<td class="border-2 w-fit">(.*?)</td>\n'
        ' {24}<td class="border-2 w-fit">(.*?)</td>\n'
        ' {24}<td class="border-2 w-fit">(.*?)</td>\n'
        ' {24}<td class="border-2 w-fit">(.*?)</td>\n'
        ' {20}</tr>', profile_page)
    days = [[], [], [], [], [], [], []]

    for day in range(5):
        for period in periods:
            days[day].append((period[0], period[day + 1],))

    day_of_week = datetime.datetime.now().weekday()
    periods_of_day = days[day_of_week]

    periods_of_day_dict = {}
    for x in periods_of_day:
        if not x[1]:
            continue
        periods_of_day_dict[x[0]] = x[1]

    time_of_day = datetime.datetime.now().time()

    if time_of_day >= datetime.time(21):
        now_period = None
    elif time_of_day >= datetime.time(20):
        now_period = '14'
    elif time_of_day >= datetime.time(18, 30):
        now_period = '13'
    elif time_of_day >= datetime.time(17, 30):
        now_period = '12'
    elif time_of_day >= datetime.time(16, 30):
        now_period = '11'
    elif time_of_day >= datetime.time(15, 50):
        now_period = '10'
    elif time_of_day >= datetime.time(15):
        now_period = '9'
    elif time_of_day >= datetime.time(14, 20):
        now_period = '8'
    elif time_of_day >= datetime.time(13, 30):
        now_period = '7'
    elif time_of_day >= datetime.time(13, 10):
        now_period = 'Pastoral'
    elif time_of_day >= datetime.time(12, 30):
        now_period = 'Lunchtime'
    elif time_of_day >= datetime.time(11, 50):
        now_period = '6'
    elif time_of_day >= datetime.time(10, 50):
        now_period = '5'
    elif time_of_day >= datetime.time(10, 10):
        now_period = '4'
    elif time_of_day >= datetime.time(9, 20):
        now_period = '3'
    elif time_of_day >= datetime.time(8, 40):
        now_period = '2'
    elif time_of_day >= datetime.time(8):
        now_period = '1'
    else:
        now_period = None

    print()

    if now_period and now_period in periods_of_day_dict:
        print(
            f"{colors.GREEN}{teacher_and_profile[0]} is at classroom {get_classroom(periods_of_day_dict[now_period])} now.{colors.RESTORE}")
    else:
        print(f"{colors.RED}We don't know where {teacher_and_profile[0]} is now.{colors.RESTORE}")

    print()
    print(f"{colors.CYAN}{teacher_and_profile[0]} will be these classrooms today:{colors.RESTORE}")

    periods_id = ["1", "2", "3", "4", "5", "6", "Lunchtime", "Pastoral", "7", "8", "9", "10", "11", "12", "13", "14"]
    after_flag = False
    for x in periods_id:
        if after_flag and x in periods_of_day_dict:
            print(f"Period\t{x}\t{get_classroom(periods_of_day_dict[x])}")
        if x == now_period:
            after_flag = True


if __name__ == '__main__':
    main()
