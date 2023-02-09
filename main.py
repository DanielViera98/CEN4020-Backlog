# import tabulate
from productBacklog import ProductBacklog
from sprintBacklog import SprintBacklog
from debug import reset_db, export_db

product = ProductBacklog()
sprint = SprintBacklog()
exit = False
while exit == False:
  print("\n\033[4mMain Menu\033[0m")
  choice = input("1: Product Backlog Menu\n2: Sprint Backlog Menu\n3: Reset Database\n4: Export Database\n5: Exit\n> ")
  match choice:
    case "1":
      product.options_menu()
    case "2":
      sprint.options_menu()
    case "3":
      choice = input("Are You Sure? Type Yes to Delete: ")
      if choice == "Yes":
        reset_db()
    case "4":
      export_db()
    case "5":
      exit = True
    case _:
      print("Invalid Input")
  # match

