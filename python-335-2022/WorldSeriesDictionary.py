input_file = open('python-335-2022/WorldSeriesWinners.txt', 'r')

start_year = 1902

teams = {}
years = {}

for line in input_file:
    line = line.strip()
    teams[line] = teams.get(line, 0) + 1

input_file.seek(0)

for line in input_file:
    line = line.strip()
    start_year += 1

    if start_year == 1904 or start_year == 1994:
        start_year += 1

    years.update({start_year:line})

user_input = int(input("Input Year between 1902 and 2021: "))

if user_input == 1904 or user_input == 1994:
    print("World Series did not have a winner in 1904 or 1994.")
else:
    if user_input in years:
        team = years[user_input]
        print(f"The winner of the World Series in {user_input} was {team}.")
    else:
        print("Invalid year or no data available for the input year.")