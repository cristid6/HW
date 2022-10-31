"""5. Afiseaza cate ore au trecut din acest an."""

from datetime import datetime

initial_date = "01/01/2022"
delta_time = datetime.now()-datetime.strptime(initial_date, "%d/%m/%Y")
print(delta_time.total_seconds()/3600)