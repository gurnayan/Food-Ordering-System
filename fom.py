import os
import csv
from datetime import datetime
# -------------------------------------------------------
# MENU DATA
# -------------------------------------------------------

menu_hotspot = [
    ["HOTSPOT"],
    ["Indian_veg"],
    ["Mix_veg", "130"], ["Dal_makhni", "90"], ["Dal_butter_fry", "75"],
    ["Paneer_butter_masala", "75"], ["kadai_paneer", "150"],
    ["Chana_masala", "105"], ["Kashmiri_aludam", "115"],
    ["Nabaratana_korma", "175"], ["Sahi_paneer", "180"],

    ["Indian_rice"],
    ["Steam_rice", "70"], ["Jeera_rice", "85"], ["Veg_pulao", "135"],
    ["Kashmiri_pulao", "185"], ["Paneer_pulao", "160"],

    ["Chinese_veg"],
    ["Paneer_tikka", "160"], ["Chilli_potato", "100"],
    ["Chilly_chowmein", "120"], ["Momos", "65"],
    ["Honey_chilly_potato", "110"],

    ["Roti"],
    ["Tandoori_roti", "15"], ["Butter_tandoori_roti", "20"],
    ["Plain_roti", "35"], ["Butter_naan", "40"], ["Masala_kulcha", "50"],

    ["Non_veg"],
    ["Chicken_kasa", "150"], ["Handi_mutton", "190"],
    ["Chicken_bharta", "160"], ["Chicken_patiala", "270"],
    ["Mutton_biryani", "180"], ["Chicken_biryani", "180"]
]

menu_infinity = [
    ["INFINITY_FOOD_PARADISE"],
    ["BURGERS"],
    ["Tikki_burger", "75"], ["Egg_burger", "55"], ["Cheese_burger", "150"],
    ["Crunchy_cheese_burger", "110"], ["Paneer_spicy_burger", "140"],
    ["Ham_burger", "250"], ["Chicken_burger", "120"],
    ["Infinity_special_burger", "170"],

    ["DRINKS"],
    ["Mineral_water", "20"], ["Cola", "40"], ["Cold_coffee", "70"],
    ["Lemon_soda", "30"], ["Lassi", "50"], ["Mango_shake", "70"]
]

menu_snapeats = [
    ["snapeats_restaurant"],
    ["Soup"],
    ["Veg_sweet_corn_soup", "80"], ["Chicken_hot_soup", "120"],

    ["Rice"],
    ["Veg_fried_rice", "120"], ["Chicken_fried_rice", "150"],

    ["Chinese"],
    ["Chilli_paneer", "150"], ["Garlic_chicken", "170"]
]

menu_southern_stories = [
    ["SOUTHERN_STORIES_INDIAN_FOOD"],
    ["BREAKFAST"],
    ["Idly", "15"], ["Medhu_vada", "20"], ["Dosa", "80"],

    ["LUNCH"],
    ["Curd_rice", "45"], ["Veg_biriyani", "50"], ["Mini_meals", "65"],

    ["DRINKS"],
    ["Tea", "20"], ["Coffee", "20"], ["Milk", "20"]
]

# -------------------------------------------------------
# CSV FUNCTIONS
# -------------------------------------------------------

def create_menu_csv(filename, data):
    with open(filename + ".csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def read_menu_csv(filename):
    with open(filename + ".csv", "r") as file:
        reader = csv.reader(file)

        print("\n---------------- MENU ----------------")
        for row in reader:
            if len(row) == 1:
                print("\n" + "*" * 60)
                print(row[0].center(60))
                print("*" * 60)
            else:
                print(row[0].ljust(45), row[1])



def search_menu_item(filename, item):
    try:
        with open(filename + ".csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 2 and row[0].lower() == item.lower():
                    return [row[0], int(row[1])]

        return [item + " Not Found", 0]
    except:
        return [item + " Not Found", 0]


# -------------------------------------------------------
# FIRST TIME FILE SETUP
# -------------------------------------------------------

check = input("Are you running this program for the First time? (y/n): ")

if check.lower() == "y":
    create_menu_csv("HOTSPOT", menu_hotspot)
    create_menu_csv("INFINITY_FOOD_PARADISE", menu_infinity)
    create_menu_csv("snapeats_restaurant", menu_snapeats)
    create_menu_csv("SOUTHERN_STORIES_INDIAN_FOOD", menu_southern_stories)

    with open("Admin.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["admin", "12345"])

    with open("Customer.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Gender", "Phone", "Address"])

    with open("daily_profit.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Total_Sales", "Total_Cost", "Total_Profit"])


    with open("Feedback.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Feedback"])

    with open("res_names.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["HOTSPOT"])
        writer.writerow(["INFINITY_FOOD_PARADISE"])
        writer.writerow(["snapeats_restaurant"])
        writer.writerow(["SOUTHERN_STORIES_INDIAN_FOOD"])

    print("All CSV files created successfully!")

# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------

print("\nNOTE 1: Use underscore (_) instead of spaces.")
print("NOTE 2: All input is case-sensitive.\n")
ad=True
while ad == True:
    print("\n" * 2)
    print("**" * 58)
    print("\n")
    print(" " * 50 + "Food Ordering System")
    print("\n")
    print("**" * 58)
    print("**" * 58)
    print("\n")
    print("\n1. Admin Login")
    print("2. Customer Login")
    print("3. Exit")

    ch = input("Enter choice: ")

    # ---------------- ADMIN ----------------
    if ch == "1":
        user = input("Enter Admin ID: ")
        pwd = input("Enter Password: ")

        valid = False

        with open("Admin.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user and row[1] == pwd:
                    valid = True
                    break

        if not valid:
            print(" Invalid Admin Login!")
            continue

        while valid:
            print("\n Admin Login Successful")
            print("1 : View Customers")
            print("2 : View Feedback")
            print("3 : Update a Menu Card")
            print("4 : Delete a Menu Card")
            print("5 : Calculate Profit")
            print("6 : Back To Main Menu")
            print("7 : Exit")

            a = input("Enter : ")

        


            if a == "1":
                with open("Customer.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(row)

            elif a == "2":
                with open("Feedback.csv", "r") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(row)
            
            elif a == "3":

                stp = []
                try:
                    with open("res_names.csv", "r", newline="") as f20:
                        reader = csv.reader(f20)
                        print("************* Select From The Given List **************\n")

                        stp = list(reader)

                        for i in stp[1:]:   # skipping header
                            print(i[0])

                except FileNotFoundError:
                    print("res_names.csv not found!")
                    continue

                print("\n")
                select = input("Enter the name of restaurant : ").strip()

                restaurant_names = [i[0] for i in stp]

                if select in restaurant_names:
                    read_menu_csv(select)   # your menu display function

                    sty = []
                    try:
                        with open(select + ".csv", "r", newline="") as f80:
                            reader = csv.reader(f80)
                            sty = list(reader)

                    except FileNotFoundError:
                        print(f"Menu file {select}.csv not found!")
                        continue

                    print("\n")
                    foo1 = input("Enter the name of the food that you want to update : ").strip()

                    a_found = False
                    for row in sty:
                        if row and row[0] == foo1:
                            a_found = True
                            break

                    if not a_found:
                        print("............ Food item not found .............")

                    else:
                        foo2 = input("Enter new name : ").strip()
                        pr4 = input("Enter new price : ").strip()

                        with open("new_file.csv", "w", newline="") as f15:
                            writer = csv.writer(f15)

                            for row in sty:
                                if row and row[0] == foo1:
                                    writer.writerow([foo2, pr4])
                                else:
                                    writer.writerow(row)

                        print(".......... MENU CARD UPDATED .............")

                        os.remove(select + ".csv")
                        os.rename("new_file.csv", select + ".csv")

                else:
                    print(".......... Restaurant cannot be found ............")


            elif a == "4":

                st = []
                try:
                    with open("res_names.csv", "r", newline="") as f45:
                        reader = csv.reader(f45)
                        print("************* Select From The Given List **************\n")

                        st = list(reader)

                        # Skip header while displaying
                        for i in st[1:]:
                            print(i[0])

                except FileNotFoundError:
                    print("res_names.csv not found!")
                    continue

                print("\n")
                delete = input("Enter the name of restaurant : ").strip()

                restaurant_names = [i[0] for i in st]

                if delete in restaurant_names:

                    #  Delete Restaurant Menu File
                    try:
                        os.remove(delete + ".csv")
                    except FileNotFoundError:
                        print(f" {delete}.csv not found, but removing from restaurant list.")

                    #  Update Restaurant List File
                    with open("new_file.csv", "w", newline="") as f10:
                        writer = csv.writer(f10)

                        for row in st:
                            if row and row[0] != delete:
                                writer.writerow(row)

                    os.remove("res_names.csv")
                    os.rename("new_file.csv", "res_names.csv")

                    print("............. Menu card successfully deleted ............")

                else:
                    print(".......... Restaurant cannot be found ............")



            elif a == "5":

                print("\n-------- DAILY PROFIT REPORT --------\n")

                try:
                    with open("daily_profit.csv", "r") as f:
                        reader = csv.reader(f)
                        for row in reader:
                            print(row[0].ljust(15), row[1].ljust(15), row[2].ljust(15), row[3])

                except FileNotFoundError:
                    print("Daily profit file not found!")
                    
            elif a == "6":
                    valid = False
                    break

            elif a == "7":
                print(" Thanks for coming ")
                valid = False
                ad = False
                break
                        
                        
        else:
            print(" Invalid Admin Login!")

    # ---------------- CUSTOMER ----------------
    elif ch == "2":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")

        with open("Customer.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, age, gender, phone, address])

        print("\nAvailable Restaurants:")
        with open("res_names.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row[0])

        res = input("Select Restaurant: ")
        read_menu_csv(res)

        cart = []
        while True:
            item = input("Enter Item Name: ")
            cart.append(search_menu_item(res, item))

            more = input("More items? (y/n): ")
            if more.lower() != "y":
                break

        total = 0
        print("\n------------ BILL ------------")
        for i in cart:
            print(i[0].ljust(40), i[1])
            total += i[1]
        print("\nTOTAL = ₹", total)

        fb = input("Enter Feedback: ")
        with open("Feedback.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, fb])
        

        today = datetime.now().strftime("%d-%m-%Y")

        cost = total * 0.60
        profit = total * 0.40

        found = False
        rows = []

        # Read existing data
        with open("daily_profit.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)

        # Update today's profit if already exists
        for row in rows[1:]:
            if row[0] == today:
                row[1] = str(float(row[1]) + total)
                row[2] = str(float(row[2]) + cost)
                row[3] = str(float(row[3]) + profit)
                found = True
                break

        # If today's entry not found, add new
        if not found:
            rows.append([today, total, cost, profit])

        # Write back updated data
        with open("daily_profit.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)


    elif ch == "3":
        print(" Program Closed")
        break