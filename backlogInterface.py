from replit import db
from debug import reset_db, export_db

class ProductBacklog():
  
  def add_item(self):
    name = input("Item Name: ")
    desc = input("Item Description: ")
    est = input("Item Estimate: ")
    db[name] = [desc, est]
    export_db()
    return

  def export(self):
    export_db()
    return
  def reset(self):
    reset_db()
    return
    
  def options_menu(self):
    print("\nOptions:\n1: Add Item\n2: Export Database\n3: Reset Database\n4: Exit")
    choice = int(input("> "))
    match choice:
      case 1:
        self.add_item()
        return False
      case 2:
        self.export()
        return False
      case 3:
        self.reset()
        return False
      case 4:
        return True
    
    

def createProductBacklog(name):
  file = open(name, "w+")
  return file


def createSprintBacklog(name):
  file = open(name, "w+")
  return file


#Adding comment to test github connection