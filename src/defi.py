import requests

query = str(input("Qual a palavra?: "))

url = "https://www.google.com/search?sxsrf=ALeKk025nAfafFQHRaOzdj_bbVi-e1O5Ug%3A1601488198474&ei=RsV0X7OyHNLC5OUP6I2-yAo&q=defini%C3%A7%C3%A3o+" + query + "&oq=defini%C3%A7%C3%A3o+&gs_lcp=CgZwc3ktYWIQAxgAMgQIIxAnMgQIIxAnMgQIIxAnMgQIABBDMgQIABBDMgIIADIFCAAQsQMyAggAMgIIADICCAA6BAgAEEc6BAguECc6CAgAELEDEIMBOgcILhAnEJMCOgUILhCxA1DwjQFYuK0BYIW6AWgBcAR4AIABoAGIAZILkgEEMC4xMZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab"

r = requests.get(url)

r.encoding = "utf-8"