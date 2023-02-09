from replit import db
from tabulate import tabulate
def export_db():
  file = open("Database.txt", "w+")
  file.write("Product Backlog\n")
  table = [["Item", "Description", "Estimate"]]
  line = []
  keys = db.prefix("P-")
  for key in keys:
    line = [[key, db[key][0], db[key][1]]]
    table = table + line
  file.write(tabulate(table, headers='firstrow'))
  
  file.write("\n\n-----------------------------------------------")
  
  file.write("\n\nSprint Backlog\n")
  table = [["Item", "Description", "Estimate"]]
  line = []
  for key in db.prefix("S-"):
    line = [[key, db[key][0], db[key][1]]]
    table = table + line
  file.write(tabulate(table, headers='firstrow'))
  
def reset_db():
  for key in db.keys():
    del db[key]
  export_db()