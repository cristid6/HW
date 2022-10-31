"""6. Afiseaza cate zile au trecut de la nasterea ta."""

from datetime import datetime

birthday_date = "30/04/1986"
delta_time = datetime.now()-datetime.strptime(birthday_date, "%d/%m/%Y")
print(delta_time.total_seconds()/3600/24)