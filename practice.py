import pandas as pd
from pandas_profiling import ProfileReport
file = pd.read_csv("car_price.csv")

profile = ProfileReport(file)
profile.to_file(output_file="car.html")
