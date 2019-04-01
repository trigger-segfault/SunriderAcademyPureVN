label purevn_choose_lunch:

    call purevn_full_stats from _call_lunch_purevn_full_stats

    # Always eat in the classroom after aquiring lovebento
    if lovebento == True and "asagaluncheat" not in seen_labels and "acceptasagalunch" in seen_labels:
        jump eat_classroom
    if lovebento == True and "chigaraluncheat" not in seen_labels and "acceptchigarafood" in seen_labels:
        jump eat_classroom

    # Make sure to give Sola her Holo if you bought one
    if hologift_check():
        jump purevn_give_hologift

    if month == 1:
        if week == 1:
            if day % 2 == 0:
                jump eat_cafeteria
            else:
                jump eat_courtyard
        if week == 4:
            jump eat_courtyard
    if month == 2:
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

    # Sola Route
    if "m4_solastart" in seen_labels:
        if month == 4:
            jump eat_courtyard

    # Chigara Route
    # No required lunches
    #if "m3w4_afterlab" in seen_labels:

    # Asaga Route
    # No required lunches
    #if "m4_asagamobchase" in seen_labels:

    # Ava Route
    # It's all automatic!
    #if "m4_avastart" in seen_labels:

    # Random lunch
    jump purevn_random_lunch

label purevn_random_lunch:
    $ purevn.rng_start = 1
    if lovebento == True:
        $ purevn.rng_start = 0

    $ purevn.rng = renpy.random.randint(purevn.rng_start,2)

    if purevn.rng == 0:
        jump eat_classroom
    if purevn.rng == 1:
        jump eat_courtyard
    if purevn.rng == 2:
        jump eat_cafeteria