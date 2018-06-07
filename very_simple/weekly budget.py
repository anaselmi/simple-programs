def weekly_budget(hours, overtime=0, pay=15):
    number = (hours * pay) + (overtime * (pay + pay / 2))
    print("You made %d$ this week." % number)
