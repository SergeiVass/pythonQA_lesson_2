def is_year_leap(year):
   if year % 4 == 0:
      x = "true"
   else:
      x = "false"
   print("Год " + str(year) + ": " + x)
is_year_leap(2017)

