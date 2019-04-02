init python:
    def hologift_check():
        return "m2w5_librarysola" in seen_labels and "m3w1_solaholo" not in seen_labels and haveitem_holo == True

label purevn_choose_afterschool:

    call purevn_full_stats from _call_afterschool_purevn_full_stats

    # Shop events
    if month == 3 and week == 5 and asagabirthdaygift == False and purevn.asaga_get_present == False:
        $ purevn.asaga_get_present = True
        call visit_shop from _call_visit_shop_purevn_1
    if month == 4 and week == 1 and day < 3 and asagabirthdaygift == False and purevn.asaga_get_present == False:
        $ purevn.asaga_get_present = True
        call visit_shop from _call_visit_shop_purevn_2

    if month == 5 and week == 3 and maraybirthdaygift == False and purevn.maray_get_present == False:
        $ purevn.maray_get_present = True
        call visit_shop from _call_visit_shop_purevn_3
    if month == 5 and week == 4 and day < 3 and maraybirthdaygift == False and purevn.maray_get_present == False:
        $ purevn.maray_get_present = True
        call visit_shop from _call_visit_shop_purevn_4

    if month == 6 and week == 5 and avabirthdaygift == False and purevn.ava_get_present == False:
        $ purevn.ava_get_present = True
        call visit_shop from _call_visit_shop_purevn_5

    # Sola's route has scripted purchases for both Chigara AND Sola, don't break continuity buy buying a second present
    if month == 8 and week == 5 and "m4_solastart" not in seen_labels and chigarabirthdaygift == False and purevn.chigara_get_present == False:
        $ purevn.chigara_get_present = True
        call visit_shop from _call_visit_shop_purevn_6
    if month == 9 and week == 1 and day < 3 and "m4_solastart" not in seen_labels and chigarabirthdaygift == False and purevn.chigara_get_present == False:
        $ purevn.chigara_get_present = True
        call visit_shop from _call_visit_shop_purevn_7

    if month == 9 and week == 2 and "m4_solastart" not in seen_labels and solabirthdaygift == False and purevn.sola_get_present == False:
        $ purevn.sola_get_present = True
        call visit_shop from _call_visit_shop_purevn_8
    if month == 9 and week == 3 and day == 1 and "m4_solastart" not in seen_labels and solabirthdaygift == False and purevn.sola_get_present == False:
        $ purevn.sola_get_present = True
        call visit_shop from _call_visit_shop_purevn_9

    # Sola Holo
    if "m2w5_librarysola" in seen_labels and "m3w1_solaholo" not in seen_labels and purevn.sola_get_holo == False and haveitem_holo == False:
        $ purevn.sola_get_holo = True
        call purevn_store_hologift from _call_purevn_store_hologift

    # Make sure to give Sola her Holo if you bought one
    if hologift_check():
        jump purevn_give_hologift

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
    
    # Sola Route
    if "m4_solastart" in seen_labels:
        if month == 4:
            jump visit_shrine
        if month == 5:
            if week < 3:
                jump library_study
            if week == 3:
                jump visit_park
            if week == 4:
                jump visit_arcade
            if week > 4:
                jump visit_shrine
        if month == 6 and week == 2:
            jump library_study

    # Chigara Route
    if "m3w4_afterlab" in seen_labels:
        if month == 5:
            if week == 1 and day > 2:
                jump library_study
            if week == 3:
                jump visit_shrine

    # Asaga Route
    if "m4_asagamobchase" in seen_labels:
        if month == 5:
            jump library_study
        if month == 9:
            jump library_study

    # Ava Route
    # It's all automatic!
    #if "m4_avastart" in seen_labels:


    # Random activity
    jump purevn_random_afterschool

label purevn_random_afterschool:
    # If we're doing random afterschool, it means there's no scene we need to hit. Just go home and stop wasting the player's time
    if hour == 6:
        jump gohome

    $ purevn.rng = renpy.random.randint(1,11)

    if purevn.rng == 1:
        jump library_study
    if purevn.rng == 2:
        jump visit_museum
    if purevn.rng == 3:
        jump visit_arcade
    if purevn.rng == 4:
        jump visit_park
    if purevn.rng == 5:
        jump visit_shrine
    if purevn.rng == 6:
        jump gym_exercise

    if purevn.rng == 7:
        jump job_museum
    if purevn.rng == 8:
        jump job_arcade
    if purevn.rng == 9:
        jump job_park
    if purevn.rng == 10:
        jump job_shrine
    if purevn.rng == 11:
        jump job_shop

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
        $ haveitem_holo = False
        "I don't have enough money to buy a Holo..."
        
    if stat_money >= 40:
        $ haveitem_holo = True
        $ stat_money -= 40
        
        "I bought Sola a Holo so she can get work done."
        
    window hide
    return
        
label purevn_store_hologift_decline:
    $ haveitem_holo = False
    
    window hide
    return

label purevn_give_hologift:
    if lunch == True:
        scene bg courtyard with dissolve
    else: # afterschool
        scene bg shrine_evening with dissolve
    $ haveitem_holo = False
    jump m3w1_solaholo
    return