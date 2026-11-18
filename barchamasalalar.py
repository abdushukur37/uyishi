# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust","Sentabr","Oktabr","Noyabr", "Dekabr"]
#     def __init__(self,day,month,year):
#         self.__day=day
#         self.__month=month
#         self.__year=year
#     def nextDay(self):
#         self.__day += 1
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(15, 6, 2023)
# sana.nextDay()
# print(sana)
# 2-----------
# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self, day, month, year):
#         self.__day=day
#         self.__month=month
#         self.__year=year
#     def nextDay(self):
#         if self.__day==30:
#             self.__day=1
#             self.__month += 1
#         else:
#             self.__day += 1
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(30, 4, 2023)
# sana.nextDay()
# print(sana)
# 3------------
# class MyDate:
#     MONTHS=["Yanvar","Fevral","Mart","Aprel","May","Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self,day,month,year):
#         self.__day=day
#         self.__month=month
#         self.__year=year
#     def nextDay(self):
#         if self.__day==31 and self.__month == 12:
#             self.__day=1
#             self.__month=1
#             self.__year+=1
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(31, 12, 2023)
# sana.nextDay()
# print(sana)
# 4----------
# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def previousDay(self):
#         self.__day = 30
#         self.__month -= 1
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(1, 5, 2023)
# sana.previousDay()
# print(sana)
# 5-------------
# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def isLeapYear(self, year):
#         return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
#     def nextDay(self):
#         if self.__month == 2 and self.isLeapYear(self.__year):
#             self.__day = 29
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(28, 2, 2024)
# sana.nextDay()
# print(sana)
# 6-------------
# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def nextDay(self):
#         self.__day = 1
#         self.__month = 3
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(29, 2, 2024)
# sana.nextDay()
# print(sana)
# 7----------
# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def nextDay(self):
#         self.__day = 1
#         self.__month = 3
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(28, 2, 2023)
# sana.nextDay()
# print(sana)
# 8----------
# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def previousDay(self):
#         self.__day = 31
#         self.__month = 12
#         self.__year -= 1
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(1, 1, 2023)
# sana.previousDay()
# print(sana)
# 9-----------
# class MyDate:
#     def __init__(self, day, month, year):
#         if year < 1 or year > 9999:
#             raise ValueError("Noto'g'ri sana kiritildi!")
#         self.__day = day
#         self.__month = month
#         self.__year = year
# try:
#     sana = MyDate(15, 6, 10000)
# except ValueError as e:
#     print(e)
# 10---------
# class MyDate:
#     def __init__(self, day, month, year):
#         if month < 1 or month > 12:
#             raise ValueError("Noto'g'ri sana kiritildi!")
#         self.__day = day
#         self.__month = month
#         self.__year = year
# try:
#     sana = MyDate(15, 13, 2023)
# except ValueError as e:
#     print(e)
# 11--------
# class MyDate:
#     def __init__(self, day, month, year):
#         if day < 1 or day > 31:
#             raise ValueError("Noto'g'ri sana kiritildi!")
#         self.__day = day
#         self.__month = month
#         self.__year = year
# try:
#     sana = MyDate(32, 5, 2023)
# except ValueError as e:
#     print(e)
# 12----------
# class MyDate:
#     MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
#               "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def setDate(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def __str__(self):
#         return f"{self.__day:02d}-{self.MONTHS[self.__month-1]} {self.__year} yil"
# sana = MyDate(15, 6, 2023)
# sana.setDate(5, 7, 2023)
# print(sana)
# 13---------
# class MyDate:
#     def __init__(self, day, month, year):
#         self.__day = day
#         self.__month = month
#         self.__year = year
#     def setDate(self, day, month, year):
#         if month == 4 and day > 30:
#             raise ValueError("Noto'g'ri sana kiritildi!")
#         self.__day = day
#         self.__month = month
#         self.__year = year
# try:
#     sana = MyDate(15, 6, 2023)
#     sana.setDate(31, 4, 2023)
# except ValueError as e:
#     print(e)