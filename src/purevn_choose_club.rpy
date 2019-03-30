label purevn_choose_club:

    call purevn_full_stats from _call_club_purevn_full_stats

    # swim_morale
    # kendo_morale
    # science_morale
    # studentcouncil_practice

    if month == 1:
        if week == 1:
            if day % 2 == 0:
                jump purevn_random_science
            else:
                jump purevn_random_kendo
        if week == 3:
            if day < 5:
                jump purevn_random_kendo
            if day < 7:
                jump studentcouncil_practice
            else:
                jump purevn_random_kendo
        if week == 4:
            jump purevn_random_swim
        if week == 5:
            jump studentcouncil_practice
    if month == 2:
        if week == 2:
            if day % 2 == 0:
                jump purevn_random_science
            else:
                jump purevn_random_kendo
        if week == 4:
            jump purevn_random_swim
    if month == 3:
        if week == 1:
            jump purevn_random_science
        if week == 3:
            jump purevn_random_kendo
        if week == 4:
            jump purevn_random_science
        if week == 5:
            jump purevn_random_kendo

    # Sola Route
    if "m4_solastart" in seen_labels:
        if month == 4:
            if day % 2 == 0:
                jump purevn_random_science
            else:
                jump purevn_random_swim

    # Chigara Route
    if "m3w4_afterlab" in seen_labels:
        if month >= 4 and month <= 8:
            jump purevn_random_science

    # Asaga Route
    if "m4_asagamobchase" in seen_labels:
        if month == 4:
            if day % 2 == 0:
                jump purevn_random_kendo
            else:
                jump studentcouncil_practice
        if month == 5:
            jump purevn_random_kendo
        if month >= 6 and month <= 7:
            if day % 2 == 0:
                jump purevn_random_kendo
            else:
                jump purevn_random_science
        if month == 9:
            jump purevn_random_kendo

    # Ava Route
    # It's all automatic!
    #if "m4_avastart" in seen_labels:

    # Random club
    jump purevn_random_club

label purevn_random_kendo:
    $ purevn_rng = renpy.random.randint(1,2)
    if purevn_rng == 1:
        jump kendo_practice
    else:
        jump kendo_morale
        
label purevn_random_swim:
    $ purevn_rng = renpy.random.randint(1,2)
    if purevn_rng == 1:
        jump swim_practice
    else:
        jump swim_morale
        
label purevn_random_science:
    $ purevn_rng = renpy.random.randint(1,2)
    if purevn_rng == 1:
        jump science_practice
    else:
        jump science_morale

label purevn_random_club:
    $ purevn_rng = renpy.random.randint(1,4)

    if purevn_rng == 1:
        jump purevn_random_kendo
    if purevn_rng == 2:
        jump purevn_random_swim
    if purevn_rng == 3:
        jump purevn_random_science
    if purevn_rng == 4:
        jump studentcouncil_practice