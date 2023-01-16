s = input()

# Get hour
hour = int(s[:2])
restOfTime = s[2:8]

# AM or PM
if (s[-2] == 'P') and (hour != 12):
    hour += 12
elif (s[-2] == 'A') and (hour == 12):
    hour -= 12
    
# Format hour with 2 digits
if hour > 10:
    hour = f'{hour}'
else:
    hour = f'0{hour}'

# Return hour plus minutes and seconds
print(f'{hour}{restOfTime}')
