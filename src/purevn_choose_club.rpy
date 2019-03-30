label purevn_choose_club:

    call purevn_full_stats

    # swim_morale
    # kendo_morale
    # science_morale
    # studentcouncil_practice

    if month == 1:
        if week == 1:
            if day % 2 == 0:
                jump science_morale
            else:
                jump kendo_morale
        if week == 3:
            if day < 5:
                jump kendo_morale
            if day < 7:
                jump studentcouncil_practice
            else:
                jump kendo_morale
        if week == 4:
            jump swim_morale
        if week == 5:
            jump studentcouncil_practice
    if month == 2:
        if week == 2:
            if day % 2 == 0:
                jump science_morale
            else:
                jump kendo_morale
        if week == 4:
            jump swim_morale
    if month == 3:
        if week == 1:
            jump science_morale
        if week == 3:
            jump kendo_morale
        if week == 4:
            jump science_morale
        if week == 5:
            jump kendo_morale






    # Default club
    jump kendo_morale
