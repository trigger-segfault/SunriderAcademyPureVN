label purevn_choose_afterschool:

    call purevn_full_stats

    # Shop events
    if month == 3 and week == 5 and asagabirthdaygift == False:
        call visit_shop
    if month == 4 and week == 1 and day < 3 and asagabirthdaygift == False:
        call visit_shop
        
    if month == 5 and week == 3 and maraybirthdaygift == False:
        call visit_shop
    if month == 5 and week == 4 and day < 3 and maraybirthdaygift == False:
        call visit_shop
        
    if month == 6 and week == 5 and avabirthdaygift == False:
        call visit_shop

    if month == 9 and week == 2 and solabirthdaygift == False:
        call visit_shop
    if month == 9 and week == 3 and day == 1 and solabirthdaygift == False:
        call visit_shop

    if month == 8 and week == 5 and chigarabirthdaygift == False:
        call visit_shop
    if month == 9 and week == 1 and day < 3 and solabirthdaygift == False:
        call visit_shop

    # Sola Holo
    if "m2w5_librarysola" in seen_labels and "m3w1_solaholo" not in seen_labels and purevn_sola_holo == False:
        call purevn_store_hologift

    if month == 1:
        if week == 1:
            if day % 2 == 0:
                jump visit_arcade
            else:
                jump visit_park
        if week == 2:
            if day % 3 == 0:
                jump visit_shrine
            if day % 3 == 1:
                jump library_study
            if day % 3 == 2:
                jump visit_park
        if week == 5:
            jump library_study
    if month == 2:
        if week == 2:
            if day % 2 == 0:
                jump visit_park
            else:
                jump visit_arcade
        if week == 4:
            if day % 2 == 0:
                jump visit_shrine
            else:
                jump library_study
        if week == 5:
            jump library_study
    if month == 3:
        if week == 2:
            jump visit_shrine
        if week == 5:
            jump library_study
    



    # Default activity
    jump visit_park

label purevn_store_hologift:

    if hour <= 5:

        scene bg city_day with dissolve
        
    if hour > 5:
        
        scene bg city_night with dissolve

    window show
    
    "Sola is still doing all her work by hand."
    "Should I buy her a Holo?"
    
    $ choice1_text = "Yes! (40 Credits)"
    $ choice1_jump = "purevn_store_hologift_accept"

    $ choice2_text = "Maybe later..."
    $ choice2_jump = "purevn_store_hologift_decline"

    show screen decision
    
    pause
    
label purevn_store_hologift_accept:
    
    if stat_money < 40:
        
        $ purevn_sola_holo = True
        $ haveitem_holo = False
        "I don't have enough money to buy a Holo..."
        
    if stat_money >= 40:
        
        $ purevn_sola_holo = True
        $ haveitem_holo = True
        $ stat_money -= 40
        
        "I bought Sola a Holo so she can get work done."
        
    window hide
    return
        
label purevn_store_hologift_decline:
    
    $ purevn_sola_holo = True
    $ haveitem_holo = False
    
    window hide
    return