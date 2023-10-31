# Code by cxzlw

import applications
import colors

print(
    colors.CYAN +
    '   _____ _                 __   \n  / ___/(_)___ ___  ____  / /__ \n  \\__ \\/ / __ `__ \\/ __ \\/ / _ \\\n'
    ' ___/ / / / / / / / /_/ / /  __/\n/____/_/_/ /_/ /_/ .___/_/\\___/ \n                /_/             \n'
    + colors.RESTORE
)
print(f"{colors.DARK_CYAN}Welcome to Simple. {colors.RESTORE}")

print()

print("We have those applications: ")
for i, app in enumerate(applications.modules):
    print(f"\t{i + 1}.\t{app.title}:\t{app.description}")


def get_user_choice():
    inputed = input(
        f"{colors.CYAN}Please choose application you want to use (1~{len(applications.modules)}): {colors.RESTORE}")
    while not (inputed.isnumeric() and 1 <= int(inputed) <= len(applications.modules)):
        print(f"{colors.RED}Illegal choice, please re-enter. {colors.RESTORE}")
        inputed = input(
            f"{colors.CYAN}Please choose application you want to use (1~{len(applications.modules)}): {colors.RESTORE}")
    return int(inputed)


user_choice = get_user_choice()
app = applications.modules[user_choice - 1]

print()

app.main()
