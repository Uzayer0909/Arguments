def total_calculation(bill_amount,tip_perc):
    total = bill_amount*(1+tip_perc*0.01)
    total = round(total,2)
    print(f"PLease pay BDT{total}")



total_calculation(678,16)