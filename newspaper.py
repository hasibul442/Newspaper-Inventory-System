day = []
random_digit_for_type_of_newsday = []
type_of_newsday = []
random_digit_for_demand = []
demand = []
revenue_for_sell = []
lost_profit_from_excess_demand = []
salvage_from_sell_of_scrap = []
daily_profit = []

day_number = int(input("Please Input Day Number: "))

for i in range(int(day_number)):
    RD_Type_Newsday = input('Random Digit For Type of Newsday: ' )
    random_digit_for_type_of_newsday.append(int(RD_Type_Newsday))
    day.append(i+1)

for i in range(int(day_number)):
    if random_digit_for_type_of_newsday[i] >= 1 and random_digit_for_type_of_newsday[i] <= 35:
        type_of_newsday.append("Good")
    elif random_digit_for_type_of_newsday[i] >= 36 and random_digit_for_type_of_newsday[i] <= 80:
        type_of_newsday.append("Fair")
    elif random_digit_for_type_of_newsday[i] >= 81 and random_digit_for_type_of_newsday[i] <= 99 or random_digit_for_type_of_newsday[i] == 0:
        type_of_newsday.append("Poor")
    else:
        print("Please Input Less Then 100")

print("\n")
for i in range(int(day_number)):
    RD_for_Demand = int(input("Random Digit For Demand: "))
    random_digit_for_demand.append(RD_for_Demand)

for i in range(int(day_number)):
    if type_of_newsday[i] == "Good":
        if random_digit_for_demand[i] >= 1 and random_digit_for_demand[i] <= 3:
            demand.append(40)
        elif random_digit_for_demand[i] >= 4 and random_digit_for_demand[i] <= 8:
            demand.append(50)
        elif random_digit_for_demand[i] >= 9 and random_digit_for_demand[i] <= 23:
            demand.append(60)
        elif random_digit_for_demand[i] >= 24 and random_digit_for_demand[i] <= 43:
            demand.append(70)
        elif random_digit_for_demand[i] >= 44 and random_digit_for_demand[i] <= 78:
            demand.append(80)
        elif random_digit_for_demand[i] >= 79 and random_digit_for_demand[i] <= 93:
            demand.append(90)
        elif random_digit_for_demand[i] >= 94 and random_digit_for_demand[i] <= 100 or random_digit_for_demand[i] == 0:
            demand.append(100)
        else:
            print("Please Enter Valid Number")
            break

    elif type_of_newsday[i] == "Fair":
        if random_digit_for_demand[i] >= 1 and random_digit_for_demand[i] <= 10:
            demand.append(40)
        elif random_digit_for_demand[i] >= 11 and random_digit_for_demand[i] <= 28:
            demand.append(50)
        elif random_digit_for_demand[i] >= 29 and random_digit_for_demand[i] <= 68:
            demand.append(60)
        elif random_digit_for_demand[i] >= 69 and random_digit_for_demand[i] <= 88:
            demand.append(70)
        elif random_digit_for_demand[i] >= 89 and random_digit_for_demand[i] <= 96:
            demand.append(80)
        elif random_digit_for_demand[i] >= 97 and random_digit_for_demand[i] <=100 or random_digit_for_demand[i] == 0:
            demand.append(90)
        else:
            print("Please Enter Valid Number")
            break

    elif type_of_newsday[i] == "Poor":
        if random_digit_for_demand[i] >= 1 and random_digit_for_demand[i] <= 44:
                demand.append(40)
        elif random_digit_for_demand[i] >= 45 and random_digit_for_demand[i] <= 66:
                demand.append(50)
        elif random_digit_for_demand[i] >= 67 and random_digit_for_demand[i] <= 82:
                demand.append(60)
        elif random_digit_for_demand[i] >= 83 and random_digit_for_demand[i] <= 94:
                demand.append(70)
        elif random_digit_for_demand[i] >= 95 and random_digit_for_demand[i] <= 100 or random_digit_for_demand[i]==0:
                demand.append(80)
        else:
            print("Please Enter Valid Number")
            break

for i in range(int(day_number)):
    if demand[i] >= 10 and demand[i] <=70:
        R_f_s =  demand[i] * .50
        revenue_for_sell.append(R_f_s)
    else:
        R_f_s = 70 * .50
        revenue_for_sell.append(R_f_s)

for i in range(int(day_number)):
    if demand[i]<=70:
        lost_profit_from_excess_demand.append(0)
    else:
        L_P_F_E_D = (demand[i] - 70)*.17
        lost_profit_from_excess_demand.append(L_P_F_E_D)

for i in range(int(day_number)):
    if demand[i]<70:
        S_F_S_F_O_S = (70 - demand[i])*.05
        salvage_from_sell_of_scrap.append(S_F_S_F_O_S)
    else:
        salvage_from_sell_of_scrap.append(0)

for i in range(day_number):
    D_P = revenue_for_sell[i] - (70*.33) - lost_profit_from_excess_demand[i] + salvage_from_sell_of_scrap[i]
    daily_profit.append(D_P)

print("\n\n")
print("_______________________________________________________________________________________________________________")
print("||     || RanDom Digit  ||  Type   ||  Random    ||        || Revenues || Lost Profit || Salvage   || Daily  ||")
print("|| Day || For Type OF   ||   of    ||  Digit For || Demand ||   From   || From Excess || From Sale || Profit ||")
print("||     ||   Newsday     || Newsday ||  Demand    ||        ||   Sell   ||    Demand   || Of Scrap  ||        ||")
print("---------------------------------------------------------------------------------------------------------------")


for i in range(day_number):
    print("  ",day[i],"\t     ",random_digit_for_type_of_newsday[i],"\t        ", type_of_newsday[i],"\t    ",random_digit_for_demand[i],"\t      ",demand[i],"\t    ","%.2f" %revenue_for_sell[i],"\t     ","%.2f" %lost_profit_from_excess_demand[i],"\t       ","%.2f" %salvage_from_sell_of_scrap[i],"\t    ","%.2f" %daily_profit[i])
    
