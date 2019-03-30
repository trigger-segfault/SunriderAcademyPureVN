label purevn_choose_lunch:

    call purevn_full_stats

    if month == 1:
        if week == 1:
            if day % 2 == 0:
                jump eat_cafeteria
            else:
                jump eat_courtyard
        if week == 4:
            jump eat_courtyard
    if month == 2:
        if "m2w5_librarysola" in seen_labels:
            $ haveitem_holo = True
            $ gift_item = 2
            jump m3w1_solaholo
        if week == 4:
            # Any is valid
            if day % 3 == 0:
                jump eat_cafeteria
            if day % 3 == 1:
                jump eat_courtyard
            if day % 3 == 2:
                jump eat_classroom
    if month == 3:
        if week == 4:
            jump eat_courtyard






    # Default location
    jump eat_cafeteria
