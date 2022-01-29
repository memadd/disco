import pandas as pd

#Read csv file
csv_file = pd.DataFrame(pd.read_csv("Movie-Dataset-Latest.csv", sep = ",", header = 0, index_col = False))

# To JSON
csv_file.to_json("data.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)