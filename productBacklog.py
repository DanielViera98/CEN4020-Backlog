from replit import db
from debug import export_db

class ProductBacklog():

  def add_item(self):
    #Gets name, description, and estimate of product and adds it to DB with prefix P-
    name = input("\nItem Name: ")
    key = "P-" + name
    desc = input("Item Description: ")
    est = input("Item Estimate: ")
    db[key] = [desc, est]
    export_db()

  def remove_item(self):
    name = input("\nItem Name: ")
    if db.get("P-" + name) is not None:
      del db["P-" + name]
      export_db()
    else:
      print("No Product Backlog item by that name.\n")

  def reset(self):
    #Resets Product DB
    choice = input("Are You Sure? Type Yes to Delete: ")
    if choice == "Yes":
      #Deletes all DB items belonging to Product Backlog
      for i in db.prefix("P-"):
        del db[i]
      export_db()
    return

  def options_menu(self):
    #Displays Options Menu
    print("\n\033[4mProduct Menu\033[0m")
    print("Options:\n1: Add Item\n2: Remove Item\n3: Export Database\n4: Reset Product Database\n5: Exit")
    choice = input("> ")
    match choice:
      case "1":
        self.add_item()
        self.options_menu()
      case "2":
        self.remove_item()
        self.options_menu()
      case "3":
        export_db()
        self.options_menu()
      case "4":
        self.reset()
        self.options_menu()
      case "5":
        return 
      case _:
        print("Invalid Input\n")
        self.options_menu()