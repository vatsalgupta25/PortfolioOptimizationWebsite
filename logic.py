def data(age,amount):
    amount = 0
    monthyly_savings = 10000

# def InvestmentAmount(age, amount):
    # if (18<age<30):
    #     amount = 0.7*monthyly_savings
    # elif (31<age<50):
    #     amount = 0.5*monthyly_savings
    # elif (51<age<60):
    #     amount = 0.4*monthyly_savings
    # else:
    #     amount = 0.3* monthyly_savings

# def AreaOfInvestment(age, amount):
    if (18<age<30):
        t = "MF: Small and Flexi Cap\nBonds: Infrastrucure(PPP)\nGold: Digital Gold\nEquity: Small Cap\nCrpyto: AltCoins\n"
    elif (31<age<50):
        t = "MF: Medium and Flexi Cap\nBonds: Infrastrucure(PPP)\nGold: Digital Gold\nEquity: Small Cap\nCrpyto: StableCoins\n"
    elif (51<age<60):
        t = "MF: Large and Flexi Cap\nBonds: Govt. \nGold: Physical Gold\nEquity: medium Cap\nCrpyto: - \n"
    else:
        t = "MF: Large Cap\nBonds: Govt. \nGold: Physical Gold\nEquity: Large Cap\nCrpyto: - \n"
    return t

