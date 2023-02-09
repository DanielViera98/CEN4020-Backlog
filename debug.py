from replit import db

def export_db():
  file = open("Database.txt", "w+")
  file.write("Item, Description, Estimate\n")

  for i, j in db.items():
    file.write(f"{i} {j[0]} {j[1]} \n")

def reset_db():
  for key in db.keys():
    del db[key]
  export_db()