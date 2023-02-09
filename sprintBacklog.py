from replit import db
from debug import export_db

class SprintBacklog():
  
  def add_item(self):
    #Gets name, description, and estimate of product and adds it to DB with prefix S-
    name = input("\nItem Name: ")
    key = "S-" + name
    desc = input("Item Description: ")
    est = input("Item Estimate: ")
    db[key] = [desc, est]
    export_db()

  def remove_item(self):
    name = input("\nItem Name: ")
    if db.get("S-" + name) is not None:
      del db["S-" + name]
      export_db()
    else:
      print("No Sprint Backlog item by that name.\n")
    
  def move_item(self):
    #Moves item from Product Backlog to Sprint Backlog
    name = input("Name of Item: ")
    key = "S-" + name
    db[key] = db["P-" + name]
    del db["P-" + name]
    export_db()
  
  def reset(self):
    #Resets Product DB
    choice = input("Are You Sure? Type Yes to Delete: ")
    if choice == "Yes":
      #Deletes all DB items belonging to Product Backlog
      for i in db.prefix("S-"):
        del db[i]
      export_db()
    return

  def options_menu(self):
    #Displays Options Menu
    print("\n\033[4mSprint Menu\033[0m")
    print("Options:\n1: Add Item\n2: Remove Item\n3: Move Item from Product Backlog to Sprint Backlog\n4: Export Database\n5: Reset Sprint Database\n6: Exit")
    choice = input("> ")
    match choice:
      case "1":
        self.add_item()
        self.options_menu()
      case "2":
        self.remove_item()
        self.options_menu()
      case "3":
        self.move_item()
        self.options_menu()
      case "4":
        export_db()
        self.options_menu()
      case "5":
        self.reset()
        self.options_menu()
      case "6":
        return
      case _:
        print("Invalid Input\n")
        self.options_menu()