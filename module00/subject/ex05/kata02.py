import datetime

kata = (2019, 9, 25, 3, 30)
kata_time = datetime.datetime(*kata)

print(f"{kata_time:%m/%d/%Y %H:%M}")