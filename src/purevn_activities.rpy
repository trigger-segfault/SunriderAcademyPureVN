init python:
    # PureVN Activities Override
    config.label_overrides['act_class'] = 'purevn_act_class'
    config.label_overrides['act_class_retry'] = 'purevn_act_class_retry'
    config.label_overrides['act_exam'] = 'purevn_act_exam'
    config.label_overrides['act_lunch'] = 'purevn_act_lunch'
    config.label_overrides['eat_courtyard'] = 'purevn_eat_courtyard'
    config.label_overrides['act_culturefest_science'] = 'purevn_act_culturefest_science'
    config.label_overrides['act_culturefest_swim'] = 'purevn_act_culturefest_swim'
    config.label_overrides['act_culturefest_kendo'] = 'purevn_act_culturefest_kendo'
    config.label_overrides['eat_classroom'] = 'purevn_eat_classroom'
    config.label_overrides['eat_cafeteria'] = 'purevn_eat_cafeteria'
    config.label_overrides['act_clubs'] = 'purevn_act_clubs'
    config.label_overrides['act_clubs2'] = 'purevn_act_clubs2'
    config.label_overrides['kendo_practice'] = 'purevn_kendo_practice'
    config.label_overrides['kendo_practice_retry'] = 'purevn_kendo_practice_retry'
    config.label_overrides['kendo_recruit'] = 'purevn_kendo_recruit'
    config.label_overrides['kendo_recruit_retry'] = 'purevn_kendo_recruit_retry'
    config.label_overrides['kendo_morale'] = 'purevn_kendo_morale'
    config.label_overrides['swim_practice'] = 'purevn_swim_practice'
    config.label_overrides['swim_practice_retry'] = 'purevn_swim_practice_retry'
    config.label_overrides['swim_recruit'] = 'purevn_swim_recruit'
    config.label_overrides['swim_recruit_retry'] = 'purevn_swim_recruit_retry'
    config.label_overrides['swim_morale'] = 'purevn_swim_morale'
    config.label_overrides['science_practice'] = 'purevn_science_practice'
    config.label_overrides['science_practice_retry'] = 'purevn_science_practice_retry'
    config.label_overrides['science_recruit'] = 'purevn_science_recruit'
    config.label_overrides['science_recruit_retry'] = 'purevn_science_recruit_retry'
    config.label_overrides['science_morale'] = 'purevn_science_morale'
    config.label_overrides['library_study'] = 'purevn_library_study'
    config.label_overrides['library_study_retry'] = 'purevn_library_study_retry'
    config.label_overrides['library_tutor'] = 'purevn_library_tutor'
    config.label_overrides['library_tutor_retry'] = 'purevn_library_tutor_retry'
    config.label_overrides['library_homework'] = 'purevn_library_homework'
    config.label_overrides['library_homework_retry'] = 'purevn_library_homework_retry'
    config.label_overrides['studentcouncil_practice'] = 'purevn_studentcouncil_practice'
    config.label_overrides['studentcouncil_practice_retry'] = 'purevn_studentcouncil_practice_retry'
    config.label_overrides['act_afterschool'] = 'purevn_act_afterschool'
    config.label_overrides['switchtocitymap'] = 'purevn_switchtocitymap'
    config.label_overrides['switchtoschoolmap'] = 'purevn_switchtoschoolmap'
    config.label_overrides['visit_museum'] = 'purevn_visit_museum'
    config.label_overrides['visit_museum_retry'] = 'purevn_visit_museum_retry'
    config.label_overrides['job_museum'] = 'purevn_job_museum'
    config.label_overrides['job_museum_retry'] = 'purevn_job_museum_retry'
    config.label_overrides['visit_arcade'] = 'purevn_visit_arcade'
    config.label_overrides['visit_arcade_retry'] = 'purevn_visit_arcade_retry'
    config.label_overrides['job_arcade'] = 'purevn_job_arcade'
    config.label_overrides['job_arcade_retry'] = 'purevn_job_arcade_retry'
    config.label_overrides['visit_park'] = 'purevn_visit_park'
    config.label_overrides['visit_park_retry'] = 'purevn_visit_park_retry'
    config.label_overrides['job_park'] = 'purevn_job_park'
    config.label_overrides['job_park_retry'] = 'purevn_job_park_retry'
    config.label_overrides['visit_shrine'] = 'purevn_visit_shrine'
    config.label_overrides['visit_shrine_retry'] = 'purevn_visit_shrine_retry'
    config.label_overrides['job_shrine'] = 'purevn_job_shrine'
    config.label_overrides['job_shrine_retry'] = 'purevn_job_shrine_retry'
    config.label_overrides['gym_exercise'] = 'purevn_gym_exercise'
    config.label_overrides['gym_exercise_retry'] = 'purevn_gym_exercise_retry'
    config.label_overrides['job_shop'] = 'purevn_job_shop'
    config.label_overrides['job_shop_retry'] = 'purevn_job_shop_retry'
    config.label_overrides['visit_shop'] = 'purevn_visit_shop'
    config.label_overrides['gohome'] = 'purevn_gohome'
    config.label_overrides['act_sleep'] = 'purevn_act_sleep'
    config.label_overrides['act_sleep_repeat'] = 'purevn_act_sleep_repeat'
    config.label_overrides['sleep_loss'] = 'purevn_sleep_loss'
    config.label_overrides['kendorounds'] = 'purevn_kendorounds'
    config.label_overrides['kendorounds_end'] = 'purevn_kendorounds_end'
    config.label_overrides['swimrounds'] = 'purevn_swimrounds'
    config.label_overrides['swimrounds_end'] = 'purevn_swimrounds_end'
    config.label_overrides['sciencerounds'] = 'purevn_sciencerounds'
    config.label_overrides['sciencerounds_end'] = 'purevn_sciencerounds_end'
    config.label_overrides['examresults_calc'] = 'purevn_examresults_calc'
    config.label_overrides['finalexamresults_calc'] = 'purevn_finalexamresults_calc'

label purevn_act_class:
    
    $ current_activity = "act_class_retry"
    $ retry = False
    
label purevn_act_class_retry:

    hide screen floating_stats
    hide screen activity_failure
    
    window hide
    
    scene bg classroom with dissolve
    
    if is_purevn():
        $ purevn.seen_count_before = len(seen_labels)

    if retry == False:
        call class_events from _call_class_events_purevn

    if is_purevn():
        $ purevn.seen_count_after = len(seen_labels)
        # Fade to show passage of time, just like in a montage
        if purevn.seen_count_before < purevn.seen_count_after:
            scene black with horizontalwipe
            scene bg classroom with horizontalwipe
        $ hour += 1
        window show
        return
    
    call diceroll from _call_diceroll_purevn

    $ tobeat = 10 + stat_stress + month*10 + week*2 - (stat_intelligence/4)
    
    if haveitem_minorstudycharm == True:
        $ tobeat -= 3
        
    if haveitem_studycharm == True:
        
        $ tobeat -= 5
        
    if haveitem_majorstudycharm == True:
        
        $ tobeat -= 10
    
    show activity_class_background
    
    show activity_class base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
        
    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind activity_class,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_class success onlayer screens
        
        if sick == True:
            show sickicon
        
        $ floatingstat = "+1 Intelligence\n+1 Stress"
        $ stat_intelligence += 1
        $ stat_stress += 1

        show screen floating_stats

    if roll < tobeat:

        play sound "Sounds/gabrielaraujo_fail.ogg"

        show screen activity_failure
        show activity_class fail onlayer screens

        if sick == True:
            show sickicon

        $ floatingstat = "+2 Stress"
        $ stat_stress += 2
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_class onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_class_background
    hide activity_success
    hide screen activity_failure
    hide activity_class onlayer screens
    hide screen floating_stats
    
    window show
        
    return
    
label purevn_act_exam:
    
    call class_events from _call_class_events_1_purevn
    
    if is_purevn():
        $ hour += 1
        return

    window hide
    
    scene bg classroom with dissolve
    
    call diceroll from _call_diceroll_1_purevn
        
    pause 0.5
    
    show activity_class_background
    
    show monthlyexam:
        xpos 1.5 ypos 0.25
        ease 0.5 xpos 0.5
    
    show activity_class base behind monthlyexam:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    pause 1.0

    $ floatingstat = "+3 Stress"
    $ stat_stress += 3
    
    show screen floating_stats
        
    $ hour += 1
    
    $ renpy.pause(3.0)
    
    show monthlyexam:
        ease 0.5 xpos -0.5
    show activity_class:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_class_background
    hide activity_class
    hide screen floating_stats
    
    window show
        
    return
    
label purevn_act_lunch:
    
    $ lunch = True

    if is_purevn():
        jump purevn_choose_lunch
        
    window hide
    scene bg campusmap
    show screen school_map
    with dissolve
    
    pause
    
label purevn_eat_courtyard:
    
    hide screen school_map
    
    $ lunch = False
    
    scene bg courtyard_day with dissolve
    
    if week >= 1 and day > 2 and month >= 1: 
        
        call courtyard_events from _call_courtyard_events_purevn
        
    if is_purevn():
        $ hour += 1
        window show
        return
                
    show activity_lunch_background
    
    call assist_enter from _call_assist_enter_purevn
    
    show activity_lunch_cafeteria:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
    
    $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    call assist_exit from _call_assist_exit_purevn
    
    show activity_lunch_cafeteria:
        ease 0.5 xpos -0.2

    pause 0.5

    hide activity_lunch_background
    hide activity_lunch_cafeteria

    window show

    return

label purevn_act_culturefest_science:
    
    hide screen school_map
    
    $ lunch = False
    
    scene bg courtyard_day with dissolve
                
    call culturefestival_events from _call_culturefestival_events_purevn
                
    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_background
        
    show festival_science:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
    
    $ hour += 1
    
    $ floatingstat = "+1 Stress"
    $ stat_stress += 1
    
    show screen floating_stats
    
    if quickact == False:
        $ renpy.pause(2.0)
        
    show festival_science:
        ease 0.5 xpos -0.2

    pause 0.5

    hide festival_science
    hide activity_background
    hide screen floating_stats

    window show

    return
    
label purevn_act_culturefest_swim:
    
    hide screen school_map
    
    $ lunch = False
    
    scene bg courtyard_day with dissolve
                
    call culturefestival_events from _call_culturefestival_events_1_purevn
               
    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_background
        
    show festival_swim:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
    
    $ hour += 1
    
    $ floatingstat = "+1 Stress"
    $ stat_stress += 1
    
    show screen floating_stats
    
    if quickact == False:
        $ renpy.pause(2.0)
        
    show festival_swim:
        ease 0.5 xpos -0.2

    pause 0.5

    hide festival_swim
    hide activity_background
    hide screen floating_stats

    window show

    return

label purevn_act_culturefest_kendo:
    
    hide screen school_map
    
    $ lunch = False
    
    scene bg courtyard_day with dissolve
                
    call culturefestival_events from _call_culturefestival_events_2_purevn
              
    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_background
        
    show festival_kendo:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
    
    $ hour += 1
    
    $ floatingstat = "+1 Stress"
    $ stat_stress += 1
    
    show screen floating_stats
    
    if quickact == False:
        $ renpy.pause(2.0)
        
    show festival_kendo:
        ease 0.5 xpos -0.2

    pause 0.5

    hide festival_kendo
    hide activity_background
    hide screen floating_stats

    window show

    return

label purevn_eat_classroom:

    hide screen school_map
    
    $ lunch = False
    
    scene bg classroom with dissolve
            
    call classlunch_events from _call_classlunch_events_purevn
              
    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_lunch_background
    
    call assist_enter from _call_assist_enter_1_purevn
    
    show activity_lunch_class:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
        
    if lovebento == True:
        $ floatingstat = "-1 Stress"
        $ stat_stress -= 1
        
        show screen floating_stats
    
    $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    call assist_exit from _call_assist_exit_1_purevn
    
    show activity_lunch_class:
        ease 0.5 xpos -0.2

    pause 0.5

    hide activity_lunch_background
    hide activity_lunch_cafeteria
    hide screen floating_stats
    
    if haveitem_bento == True:
        $ bento_count -= 1
        
    if bento_count == 0:
        $ haveitem_bento = False
        $ showitem_bento = True

    window show

    return

label purevn_eat_cafeteria:

    hide screen school_map

    $ lunch = False

    scene bg cafeteria with dissolve

    if week >= 1 and day > 2 and month >= 1: 

        call cafeteria_events from _call_cafeteria_events_purevn

    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_lunch_background

    call assist_enter from _call_assist_enter_2_purevn

    show activity_lunch_cafeteria:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    $ hour += 1

    if quickact == False:
        $ renpy.pause(2.0)

    call assist_exit from _call_assist_exit_2_purevn

    show activity_lunch_cafeteria:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_lunch_background
    hide activity_lunch_cafeteria

    window show

    return

label purevn_act_clubs:
    
    $ clubtime = True
        
    call clubtime_events from _call_clubtime_events_purevn

    if hour == 7:
        return
    
    if is_purevn():
        jump purevn_choose_club
    
    window hide
    scene bg campusmap
    show screen school_map
    with dissolve
    
    if stat_luck >= 0:
        $ ran_morale = renpy.random.randint(1,100) - renpy.random.randint(0,stat_luck) + (difficulty-2)*10
    if stat_luck < 0:
        $ ran_morale = renpy.random.randint(1,100) + renpy.random.randint(stat_luck,0) + (difficulty-2)*10
    
    if stat_kendo_morale < (stat_kendo_member*(1+(ran_morale/200))) and stat_kendo_member > 1:    
        call diceroll from _call_diceroll_2_purevn
        
        if roll < 30 - stat_kendo_morale:
            
            $ stat_kendo_member -= 1
            
            $ quitclub = "kendo"
            
            show screen club_quit
        
    if stat_swim_morale < (stat_swim_member*(1+(ran_morale/200))) and stat_swim_member > 1:    
        call diceroll from _call_diceroll_3_purevn
        
        if roll < 30 - stat_swim_morale:
            
            $ stat_swim_member -= 1
            
            $ quitclub = "swim"
            
            show screen club_quit
            
    if stat_science_morale < (stat_science_member*(1+(ran_morale/200))) and stat_science_member > 1:    
        call diceroll from _call_diceroll_4_purevn
        
        if roll < 30 - stat_science_morale:
            
            $ stat_science_member -= 1
            
            $ quitclub = "science"
            
            show screen club_quit
            
    if month > 1 or week >= 2:
        
        if stat_kendo_member < 5:
            
            $ quitclub = "kendo"
            $ kendo_disbanded -= 1
            
            show screen clubwarning
            
        if stat_science_member < 5:
            
            $ quitclub = "science"
            $ science_disbanded -= 1
            
            show screen clubwarning
            
        if stat_swim_member < 5:
            
            $ quitclub = "swim"
            $ swim_disbanded -= 1
            
            show screen clubwarning
            
    if kendo_disbanded == 0:
        
        jump badend_disbanded
        
    if swim_disbanded == 0:
        
        jump badend_disbanded

    if science_disbanded == 0:
        
        jump badend_disbanded
        
    if stat_kendo_member >= 5:
        
        $ kendo_disbanded = 7
                
    if stat_science_member >= 5:
        
        $ science_disbanded = 7
                
    if stat_swim_member >= 5:
        
        $ swim_disbanded = 7
            
    pause
    
label purevn_act_clubs2:
    
    $ clubtime = True
    
    if is_purevn():
        jump purevn_choose_club
    
    window hide
    scene bg campusmap
    show screen school_map
    with dissolve
            
    pause
    
label purevn_kendo_practice:
    
    $ current_activity = "kendo_practice_retry"
    $ retry = False

label purevn_kendo_practice_retry:

    window hide

    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    
    if nogym == False:
    
        if hour <= 5:
            scene bg gym with dissolve
        if hour > 5:
            scene bg gym_night with dissolve
            
    if nogym == True:
        
        scene bg courtyard_day with dissolve
    
    if retry == False:
        call kendo_events from _call_kendo_events_purevn

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_5_purevn

    $ tobeat = 20 + stat_stress + stat_kendo_readiness - ((stat_fitness/1.5) + (stat_charisma/2))
    show activity_club_background

    show activity_kendopractice base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0

    if roll >= tobeat:

        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind activity_kendopractice,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_kendopractice success onlayer screens
        
        call diceroll2 from _call_diceroll2_purevn
        
        if roll2 >= (tobeat+25):
            
            if sick == False:

                $ floatingstat = "+2 Readiness\n+1 Stress"
                $ stat_kendo_readiness += 2
                $ stat_stress += 1
                
            if sick == True:
                
                show sickicon

                $ floatingstat = "+2 Readiness\n+2 Stress"
                $ stat_kendo_readiness += 2
                $ stat_stress += 2

        if roll2 < (tobeat+25):
            
            if sick == False:

                $ floatingstat = "+2 Readiness\n-1 Morale\n+1 Stress"
                $ stat_kendo_readiness += 2
                $ stat_kendo_morale -= 1
                $ stat_stress += 1
                
            if sick == True:
                
                show sickicon
                
                $ floatingstat = "+2 Readiness\n-1 Morale\n+2 Stress"
                $ stat_kendo_readiness += 2
                $ stat_kendo_morale -= 1
                $ stat_stress += 2
        
        show screen floating_stats
        $ progress_readiness = stat_science_readiness + stat_swim_readiness + stat_kendo_readiness
        
        if persistent.progress_readiness < progress_readiness:
            $ persistent.progress_readiness = progress_readiness
        $ achievement.grant_progress("readiness", progress_readiness,1000)
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show activity_kendopractice fail onlayer screens
        
        call diceroll2 from _call_diceroll2_1_purevn
        
        if roll2 >= (tobeat+20):
            
            if sick == False:
        
                $ floatingstat = "+1 Readiness\n-1 Morale\n+2 Stress"
                $ stat_kendo_readiness += 1
                $ stat_kendo_morale -= 1
                $ stat_stress += 2
                
            if sick == True:
                
                show sickicon
                
                $ floatingstat = "+1 Readiness\n-1 Morale\n+4 Stress"
                $ stat_kendo_readiness += 1
                $ stat_kendo_morale -= 1
                $ stat_stress += 4
            
        if roll2 < (tobeat+20):
            
            if sick == False:
            
                $ floatingstat = "+1 Readiness\n-2 Morale\n+2 Stress"
                $ stat_kendo_readiness += 1
                $ stat_kendo_morale -= 2
                $ stat_stress += 2
                
            if sick == True:
                
                show sickicon
                
                $ floatingstat = "+1 Readiness\n-2 Morale\n+4 Stress"
                $ stat_kendo_readiness += 1
                $ stat_kendo_morale -= 2
                $ stat_stress += 4
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_kendopractice onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_club_background
    hide activity_success
    hide screen activity_failure
    hide activity_kendopractice onlayer screens
    hide screen floating_stats
    
    window show
        
    return

label purevn_kendo_recruit:
    
    $ current_activity = "kendo_recruit_retry"
    $ retry = False
    

label purevn_kendo_recruit_retry:
    
    hide screen activity_failure
    hide screen floating_stats
    
    hide screen school_map
    
    if nogym == False:
    
        if hour <= 5:
            scene bg gym with dissolve
        if hour > 5:
            scene bg gym_night with dissolve
            
    if nogym == True:
        
        scene bg courtyard_day with dissolve
        
    if is_purevn():
        if recruitmentday == False:
            $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_6_purevn

    $ tobeat = 20 + stat_stress + stat_kendo_member*10 - (stat_kendo_prestige/1.5) - stat_charisma
    show activity_club_background
    
    show activity_kendorecruit base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind activity_kendorecruit,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_kendorecruit success onlayer screens
        
        if sick == True:
            show sickicon
        
        if recruitmentday == False:
            
            $ floatingstat = "+1 Member\n+2 Stress"
            $ stat_kendo_member += 1
            $ stat_stress += 2
                            
        if recruitmentday == True:

            $ floatingstat = "+1 Member"
            $ stat_kendo_member += 1
                        
        show screen floating_stats
        
        $ progress_members = stat_kendo_member + stat_swim_member + stat_science_member
        if persistent.progress_members < progress_members:
            $ persistent.progress_members = progress_members
        $ achievement.grant_progress("member", progress_members,200)
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        if recruitmentday == True:
            $ retry = True
            
        show screen activity_failure
        show activity_kendorecruit fail onlayer screens
        
        if sick == True:
            show sickicon

        if recruitmentday == False:

            $ floatingstat = "+2 Stress"
            $ stat_stress += 2
            
        if recruitmentday == True:
            
            $ floatingstat = "+1 Stress"
            $ stat_stress += 1
            
        show screen floating_stats
        
    if recruitmentday == False and retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_kendorecruit onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_club_background
    hide activity_success
    hide screen activity_failure
    hide activity_kendorecruit onlayer screens
    hide screen floating_stats
    
    window show
        
    return

label purevn_kendo_morale:
    
    hide screen school_map
    
    if nogym == False:
    
        if hour <= 5:
            scene bg gym with dissolve
        if hour > 5:
            scene bg gym_night with dissolve
            
    if nogym == True:
        
        scene bg courtyard_day with dissolve
        
    call kendo_events from _call_kendo_events_1_purevn

    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_club_background

    show activity_kendopractice success:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    play sound "Sounds/bertrof_success.ogg"
        
    show activity_success behind activity_kendopractice,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
        xpos 0.5 ypos 0.5
        
    if sick == False:
        
        $ floatingstat = "+3 Morale"
        $ stat_kendo_morale += 3

    if sick == True:
        
        show sickicon
        
        $ floatingstat = "+3 Morale\n+1 Stress"
        $ stat_kendo_morale += 3
        $ stat_stress += 1
        
    show screen floating_stats
                
    $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_kendopractice success:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_success
    hide activity_club_background
    hide activity_kendopractice
    hide screen floating_stats
    
    window show
        
    return
    
label purevn_swim_practice:
    
    $ current_activity = "swim_practice_retry"
    $ retry = False
    
label purevn_swim_practice_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    
    window hide
    
    if hour <= 5:
        scene bg pool with dissolve
    if hour > 5:
        scene bg pool_evening with dissolve

    if retry == False:
        call pool_events from _call_pool_events_purevn

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_7_purevn

    $ tobeat = 20 + stat_stress + stat_swim_readiness - ((stat_fitness/1.5) + (stat_charisma/2))
    show activity_club_background
    
    show activity_swimpractice base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind activity_swimpractice,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_swimpractice success onlayer screens
        
        call diceroll2 from _call_diceroll2_2_purevn
        
        if roll2 >= (tobeat+20):
            
            if sick == False:

                $ floatingstat = "+2 Readiness\n+1 Stress"
                $ stat_swim_readiness += 2
                $ stat_stress += 1

            if sick == True:

                show sickicon

                $ floatingstat = "+2 Readiness\n+2 Stress"
                $ stat_swim_readiness += 2
                $ stat_stress += 2


        if roll2 < (tobeat+20):
            
            if sick == False:

                $ floatingstat = "+2 Readiness\n-1 Morale\n+1 Stress"
                $ stat_swim_readiness += 2
                $ stat_swim_morale -= 1
                $ stat_stress += 1
                
            if sick == True:
                
                show sickicon
                
                $ floatingstat = "+2 Readiness\n-1 Morale\n+2 Stress"
                $ stat_swim_readiness += 2
                $ stat_swim_morale -= 1
                $ stat_stress += 2
        
        show screen floating_stats
        $ progress_readiness = stat_science_readiness + stat_swim_readiness + stat_kendo_readiness
        if persistent.progress_readiness < progress_readiness:
            $ persistent.progress_readiness = progress_readiness
        $ achievement.grant_progress("readiness", progress_readiness,1000)
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show activity_swimpractice fail onlayer screens
        
        call diceroll2 from _call_diceroll2_3_purevn
        
        if roll2 >= (tobeat+20):
            
            if sick == False:
        
                $ floatingstat = "+1 Readiness\n-1 Morale\n+2 Stress"
                $ stat_swim_readiness += 1
                $ stat_swim_morale -= 1
                $ stat_stress += 2
                
            if sick == True:
                
                show sickicon
                
                $ floatingstat = "+1 Readiness\n-1 Morale\n+4 Stress"
                $ stat_swim_readiness += 1
                $ stat_swim_morale -= 1
                $ stat_stress += 4
            
        if roll2 < (tobeat+20):
            
            if sick == False:
            
                $ floatingstat = "+1 Readiness\n-2 Morale\n+2 Stress"
                $ stat_swim_readiness += 1
                $ stat_swim_morale -= 2
                $ stat_stress += 2
                
            if sick == True:
                
                show sickicon
                
                $ floatingstat = "+1 Readiness\n-2 Morale\n+4 Stress"
                $ stat_swim_readiness += 1
                $ stat_swim_morale -= 2
                $ stat_stress += 4
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1

    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_swimpractice onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_club_background
    hide activity_success
    hide screen activity_failure
    hide activity_swimpractice onlayer screens
    hide screen floating_stats
    
    window show
        
    return

label purevn_swim_recruit:
    
    $ current_activity = "swim_recruit_retry"
    $ retry = False
    

label purevn_swim_recruit_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    
    window hide
    
    hide screen school_map
    
    if hour <= 5:
        scene bg courtyard_day with dissolve
    if hour > 5:
        scene bg courtyard_evening with dissolve
    
    if is_purevn():
        if recruitmentday == False:
            $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_8_purevn

    $ tobeat = 20 + stat_stress + stat_swim_member*10 - (stat_swim_prestige/1.5) - stat_charisma
    show activity_club_background
    
    show activity_swimrecruit base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind activity_swimrecruit,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_swimrecruit success onlayer screens
        
        if recruitmentday == False:
                                        
            $ floatingstat = "+1 Member\n+2 Stress"
            $ stat_swim_member += 1
            $ stat_stress += 2
            
        if recruitmentday == True:
            
            $ floatingstat = "+1 Member"
            $ stat_swim_member += 1
        
        show screen floating_stats
        $ progress_members = stat_kendo_member + stat_swim_member + stat_science_member
        if persistent.progress_members < progress_members:
            $ persistent.progress_members = progress_members
        $ achievement.grant_progress("member", progress_members,200)
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        if recruitmentday == True:
            $ retry = True
        
        show screen activity_failure
        show activity_swimrecruit fail onlayer screens

        if sick == True:
            show sickicon
            
        if recruitmentday == False:
                                        
            $ floatingstat = "+2 Stress"
            $ stat_stress += 2
            
        if recruitmentday == True:
            
            $ floatingstat = "+1 Stress"
            $ stat_stress += 1

        show screen floating_stats
        
    if recruitmentday == False and retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_swimrecruit onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_club_background
    hide activity_success
    hide screen activity_failure
    hide activity_swimrecruit onlayer screens
    hide screen floating_stats
    
    window show
        
    return

label purevn_swim_morale:
    
    hide screen school_map
    
    if hour <= 5:
        scene bg pool with dissolve
    if hour > 5:
        scene bg pool_evening with dissolve

    call pool_events from _call_pool_events_1_purevn

    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_club_background

    show activity_swimpractice success:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    play sound "Sounds/bertrof_success.ogg"
        
    show activity_success behind activity_swimpractice,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
        xpos 0.5 ypos 0.5
        
    if sick == False:
        
        $ floatingstat = "+3 Morale"
        $ stat_swim_morale += 3
        
    if sick == True:
        
        show sickicon
        
        $ floatingstat = "+3 Morale\n+1 Stress"
        $ stat_swim_morale += 3
        $ stat_stress += 1
        
    show screen floating_stats
                
    $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_swimpractice success:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_success
    hide activity_club_background
    hide activity_swimpractice
    hide screen floating_stats
    
    window show
        
    return

label purevn_science_practice:
    
    $ current_activity = "science_practice_retry"
    $ retry = False
    

label purevn_science_practice_retry:

    hide screen floating_stats
    hide screen activity_failure
    
    hide screen school_map
    
    if hour <= 5:
        scene bg lab with dissolve
    if hour > 5:
        scene bg lab_evening with dissolve

    if retry == False:
        call lab_events from _call_lab_events_purevn

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_9_purevn

    $ tobeat = 20 + stat_stress + stat_science_readiness + month*5 + week  - ((stat_intelligence/3) + (stat_charisma/2))
    show activity_club_background

    show activity_sciencepractice base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:

        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind activity_sciencepractice,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_sciencepractice success onlayer screens
        
        call diceroll2 from _call_diceroll2_4_purevn

        if sick == True:
            show sickicon

        if roll2 >= (tobeat+20):

            $ floatingstat = "+2 Readiness\n+1 Stress"
            $ stat_science_readiness += 2
            $ stat_stress += 1

        if roll2 < (tobeat+20):

            $ floatingstat = "+2 Readiness\n-1 Morale\n+1 Stress"
            $ stat_science_readiness += 2
            $ stat_science_morale -= 1
            $ stat_stress += 1
        
        show screen floating_stats
        $ progress_readiness = stat_science_readiness + stat_swim_readiness + stat_kendo_readiness
        if persistent.progress_readiness < progress_readiness:
            $ persistent.progress_readiness = progress_readiness
        $ achievement.grant_progress("readiness", progress_readiness,1000)
    
    if roll < tobeat:

        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show activity_sciencepractice fail onlayer screens
        
        call diceroll2 from _call_diceroll2_5_purevn
        
        if sick == True:
            show sickicon
        
        if roll2 >= (tobeat+20):
            
            $ floatingstat = "+1 Readiness\n-1 Morale\n+2 Stress"
            $ stat_science_readiness += 1
            $ stat_science_morale -= 1
            $ stat_stress += 2
            
        if roll2 < (tobeat+20):
        
            $ floatingstat = "+1 Readiness\n-2 Morale\n+2 Stress"
            $ stat_science_readiness += 1
            $ stat_science_morale -= 2
            $ stat_stress += 2
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_sciencepractice onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_club_background
    hide activity_success
    hide screen activity_failure
    hide activity_sciencepractice onlayer screens
    hide screen floating_stats
    
    window show
        
    return
    

label purevn_science_recruit:

    $ current_activity = "science_recruit_retry"
    $ retry = False

label purevn_science_recruit_retry:

    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    
    if hour <= 5:
        scene bg courtyard_day with dissolve
    if hour > 5:
        scene bg courtyard_evening with dissolve

    window hide

    if is_purevn():
        if recruitmentday == False:
            $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_10_purevn

    $ tobeat = 20 + stat_stress + stat_science_member*10 - (stat_science_prestige/1.5) - stat_charisma
    show activity_club_background

    show activity_sciencerecruit base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0

    if roll >= tobeat:

        play sound "Sounds/bertrof_success.ogg"

        show activity_success behind activity_sciencerecruit,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_sciencerecruit success onlayer screens
        
        if recruitmentday == False:
                                
            $ floatingstat = "+1 Member\n+2 Stress"
            $ stat_science_member += 1
            $ stat_stress += 2

        if recruitmentday == True:
            
            $ floatingstat = "+1 Member"
            $ stat_science_member += 1
        
        show screen floating_stats
        $ progress_members = stat_kendo_member + stat_swim_member + stat_science_member
        if persistent.progress_members < progress_members:
            $ persistent.progress_members = progress_members
        $ achievement.grant_progress("member", progress_members,200)
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show activity_sciencerecruit fail onlayer screens
        
        if sick == True:
            show sickicon
        
        if recruitmentday == False:
                                
            $ floatingstat = "+2 Stress"
            $ stat_stress += 2

        if recruitmentday == True:
            
            $ floatingstat = "+1 Stress"
            $ stat_stress += 1
        
        show screen floating_stats
        
    if recruitmentday == False and retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_sciencerecruit onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_club_background
    hide activity_success
    hide screen activity_failure
    hide activity_sciencerecruit onlayer screens
    hide screen floating_stats

    window show

    return

label purevn_science_morale:
    
    hide screen school_map
    
    if hour <= 5:
        scene bg lab with dissolve
    if hour > 5:
        scene bg lab_evening with dissolve

    call lab_events from _call_lab_events_1_purevn

    if is_purevn():
        $ hour += 1
        window show
        return

    show activity_club_background

    show activity_sciencepractice success:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    play sound "Sounds/bertrof_success.ogg"
        
    if sick == True:
        show sickicon
        
    show activity_success behind activity_sciencepractice,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
        xpos 0.5 ypos 0.5
    $ floatingstat = "+3 Morale"
    $ stat_science_morale += 3

    show screen floating_stats
                
    $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_sciencepractice success:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_success
    hide activity_club_background
    hide activity_sciencepractice
    hide screen floating_stats
    
    window show
        
    return


label purevn_library_study:
    
    $ current_activity = "library_study_retry"
    $ retry = False
    
label purevn_library_study_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    window hide
    
    if hour <= 5:

        scene bg library with dissolve
        
    if hour > 5:
        
        scene bg library_night with dissolve
        
    if lunch == False and retry == False:
        
        call library_events from _call_library_events_purevn
    
    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_11_purevn
        
    $ tobeat = 15 + stat_stress + month*10 + week*2 - (stat_intelligence/3)
    
    if haveitem_minorstudycharm == True:
        $ tobeat -= 3
        
    if haveitem_studycharm == True:
        
        $ tobeat -= 5
        
    if haveitem_majorstudycharm == True:
        
        $ tobeat -= 10
        
    show activity_background
    
    call assist_enter from _call_assist_enter_3_purevn
    
    show activity_library base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        call assist_success from _call_assist_success_purevn
        
        show activity_success behind activity_library,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_library success onlayer screens
        
        if sick == True:
            show sickicon
        
        $ floatingstat = "+2 Intelligence\n+1 Stress"
        $ stat_intelligence += 2
        $ stat_stress += 1
        
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        call assist_fail from _call_assist_fail_purevn
        
        show screen activity_failure
        show activity_library fail onlayer screens
        
        if sick == True:
            show sickicon
        
        $ floatingstat = "+2 Stress"
        $ stat_stress += 2
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
        
    if quickact == False:
        $ renpy.pause(2.0)
    
    if lunch == True:
        if haveitem_bento == True:
            $ bento_count -= 1
            
        if bento_count == 0:
            $ haveitem_bento = False
            $ showitem_bento = True
    
    show activity_library onlayer screens:
        ease 0.5 xpos -0.2
        
    call assist_exit from _call_assist_exit_3_purevn
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide activity_library onlayer screens
    hide screen floating_stats
    
    window show
        
    return
    

label purevn_library_tutor:
    
    $ current_activity = "library_tutor_retry"
    $ retry = False

label purevn_library_tutor_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    window hide
    
    if hour <= 5:

        scene bg library with dissolve
        
    if hour > 5:
        
        scene bg library_night with dissolve

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_12_purevn
        
    $ tobeat = 20 + stat_stress + month*10 + week*2 - (stat_intelligence/3)
    
    if haveitem_minorstudycharm == True:
        $ tobeat -= 3
        
    if haveitem_studycharm == True:
        
        $ tobeat -= 5
        
    if haveitem_majorstudycharm == True:
        
        $ tobeat -= 10
        
    show activity_background
    
    $ assist_ava = True
    
    call assist_enter from _call_assist_enter_4_purevn
    
    show activity_library base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        call assist_success from _call_assist_success_1_purevn
        
        show activity_success behind activity_library,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_library success onlayer screens
        
        if sick == True:
            show sickicon
        
        $ floatingstat = "+3 Intelligence\n+1 Stress"
        $ stat_intelligence += 3
        $ stat_stress += 1
        
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        call assist_fail from _call_assist_fail_1_purevn
        
        show screen activity_failure
        show activity_library fail onlayer screens
        
        if sick == True:
            show sickicon
        
        $ floatingstat = "+1 Intelligence\n+2 Stress"
        $ stat_intelligence += 1
        $ stat_stress += 2
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
        
    if quickact == False:
        $ renpy.pause(2.0)

    show activity_library onlayer screens:
        ease 0.5 xpos -0.2

    call assist_exit from _call_assist_exit_4_purevn

    $ assist_ava = False

    pause 0.5

    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide activity_library onlayer screens
    hide screen floating_stats

    window show

    return


label purevn_library_homework:
    
    $ current_activity = "library_homework_retry"
    $ retry = False
    
label purevn_library_homework_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    window hide
    
    if hour <= 5:

        scene bg library with dissolve
        
    if hour > 5:
        
        scene bg library_night with dissolve
        
    if lunch == False and retry == False:
        
        call library_events from _call_library_events_1_purevn
            
    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_13_purevn
        
    $ tobeat = 20 + stat_stress + month*10 + week*2 - (stat_intelligence/3)
    
    if haveitem_minorstudycharm == True:
        $ tobeat -= 3
        
    if haveitem_studycharm == True:
        
        $ tobeat -= 5
        
    if haveitem_majorstudycharm == True:
        
        $ tobeat -= 10
        
    show activity_background
    
    call assist_enter from _call_assist_enter_5_purevn
    
    show activity_library base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        call assist_success from _call_assist_success_2_purevn
        
        show activity_success behind activity_library,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_library success onlayer screens
        
        if sick == True:
            show sickicon
        
        $ floatingstat = "-1 Homework\n+2 Stress"
        $ stat_homework -= 1
        $ stat_stress += 2
        
        show screen floating_stats
        
    if roll < tobeat:
        
        $ retry = True
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        call assist_fail from _call_assist_fail_2_purevn
        
        show screen activity_failure
        show activity_library fail onlayer screens
        
        if sick == True:
            show sickicon
        
        $ floatingstat = "-1 Homework\n+3 Stress"
        $ stat_homework -= 1
        $ stat_stress += 3
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
        
    if quickact == False:
        $ renpy.pause(2.0)

    if lunch == True:
        if haveitem_bento == True:
            $ bento_count -= 1
            
        if bento_count == 0:
            $ haveitem_bento = False
            $ showitem_bento = True
    
    show activity_library onlayer screens:
        ease 0.5 xpos -0.2
        
    call assist_exit from _call_assist_exit_5_purevn
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide activity_library onlayer screens
    hide screen floating_stats
    
    window show
        
    return


label purevn_studentcouncil_practice:
    
    $ current_activity = "studentcouncil_practice_retry"
    $ retry = False
    
label purevn_studentcouncil_practice_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    window hide
    
    scene bg councilroom with dissolve
    
    if retry == False:
        call studentcouncil_events from _call_studentcouncil_events_purevn
    
    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_14_purevn

    $ tobeat = 20 + stat_stress + month*10 + week*2 - (stat_intelligence/4) - (stat_charisma/2)
    show activity_background
    
    show activity_studentcouncil base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:

        play sound "Sounds/bertrof_success.ogg"

        show activity_success behind activity_studentcouncil,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_studentcouncil success onlayer screens

        if sick == False:

            $ floatingstat = "+2 Charisma\n+1 Stress"
            $ stat_charisma += 2
            $ stat_stress += 1
            
        if sick == True:
            
            show sickicon
            
            $ floatingstat = "+2 Charisma\n+1 Stress"
            $ stat_charisma += 2
            $ stat_stress += 2
        
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show activity_studentcouncil fail onlayer screens
        
        if sick == False:
        
            $ floatingstat = "+1 Charisma\n+2 Stress"
            $ stat_charisma += 1
            $ stat_stress += 2
            
        if sick == True:
            
            show sickicon
            
            $ floatingstat = "+1 Charisma\n+3 Stress"
            $ stat_charisma += 1
            $ stat_stress += 3
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_studentcouncil onlayer screens:
        ease 0.5 xpos -0.2
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide activity_studentcouncil onlayer screens
    hide screen floating_stats
    
    window show
        
    return
    
label purevn_act_afterschool:
    
    $ clubtime = False
    $ afterschool = True
    
    call afterschool_events from _call_afterschool_events_purevn

    if event_buyswords == True:
        return

    if m1w2_visitarcade == True:
        return

    if hour == 7:
        return
    
    if ava_tutoring == True:
        if day == 4 or day == 7:
            jump library_tutor
    
    if is_purevn():
        if (
            (month > 4) or (month == 4 and (week > 1 or (week == 1 and day > 4)))
        ) and (
            (affection_sola >= 50 and "m3w3_eldersday_shrine" in seen_labels and "m3w1_solaholo" in seen_labels) or
            (affection_chigara >= 50 and "m3w4_lynn_lab" in seen_labels) or
            (affection_asaga >= 50 and "m4_asagaafterbirthday" in seen_labels) or
            (affection_ava >= 60 and "m3w5_incident_councilroom2" in seen_labels)
        ) and (
            "m4_solastart" not in seen_labels and
            "m3w4_afterlab" not in seen_labels and
            "m4_asagamobchase" not in seen_labels and
            "m4_avastart" not in seen_labels
        ) and purevn.no_route == False:
            window hide
            
            scene bg campusmap
            show screen purevn_route_map
            with dissolve
            
            pause
        jump purevn_choose_afterschool
        
    window hide
    
    scene bg campusmap
    show screen school_map
    with dissolve
    
    pause
    
label purevn_switchtocitymap:
    
    if is_purevn():
        $ hour += 1
        return

    window hide
    hide screen school_map
    scene bg citymap
    show screen citymap
    with dissolve
    
    pause
    
label purevn_switchtoschoolmap:
    
    if is_purevn():
        $ hour += 1
        return
    
    window hide
    hide screen citymap
    scene bg campusmap
    show screen school_map
    with dissolve
    
    pause
        

label purevn_visit_museum:
    
    $ current_activity = "visit_museum_retry"
    $ retry = False
    
label purevn_visit_museum_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    
    if stat_money < 2:
        
        hide screen citymap
        hide screen activity_failure
        hide activity_museum onlayer screens
        
        "I don't have enough money to go here."

        if retry == False:

            show screen citymap

            pause

        return

    if stat_money >= 1:

        hide screen citymap

        $ stat_money -= 2
        $ times_museum += 1
        
        if persistent.times_museum < times_museum:
            $ persistent.times_museum = times_museum
        $ achievement.grant_progress("academic", times_museum,400)
        
        if hour <= 5:

            scene bg museum_day with dissolve
            
        if hour > 5:
            
            scene bg museum_night with dissolve
            
        if retry == False:
            call museum_events from _call_museum_events_purevn

        if is_purevn():
            $ hour += 1
            window show
            return
        
        call diceroll from _call_diceroll_15_purevn

        $ tobeat = 20 + stat_stress + month*5 + week - (stat_intelligence/2)
        show activity_background

        call assist_enter from _call_assist_enter_6_purevn

        show activity_museum base onlayer screens:
            xpos 1.2 ypos 0.5
            ease 0.5 xpos 0.5
            
        if quickact == False:
            pause 1.0
        
        if sick == True:
            show sickicon
        
        if roll >= tobeat:
            
            play sound "Sounds/bertrof_success.ogg"
            
            call assist_success from _call_assist_success_3_purevn
            show activity_success behind activity_museum,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
                xpos 0.5 ypos 0.5
            show activity_museum success onlayer screens
            
            $ floatingstat = "+3 Intelligence\n-1 Stress"
            $ stat_intelligence += 3
            $ stat_stress -= 1
            
            if stat_stress < 0:
                $ stat_stress = 0
            
            show screen floating_stats
            
        if roll < tobeat:
            
            play sound "Sounds/gabrielaraujo_fail.ogg"
            
            call assist_fail from _call_assist_fail_3_purevn
            show screen activity_failure
            show activity_museum fail onlayer screens
            
            $ floatingstat = "+2 Intelligence\n+1 Stress"
            $ stat_intelligence += 1
            
            show screen floating_stats
                
        if retry == False:
            $ hour += 1
        
        if quickact == False:
            $ renpy.pause(2.0)
        
        show activity_museum onlayer screens:
            ease 0.5 xpos -0.2
            
        call assist_exit from _call_assist_exit_6_purevn
        
        pause 0.5
        
        hide activity_background
        hide activity_success
        hide screen activity_failure
        hide activity_museum onlayer screens
        hide screen floating_stats
        
        window show
            
        return


label purevn_job_museum:
            
    $ current_activity = "job_museum_retry"
    $ retry = False

label purevn_job_museum_retry:
            
    hide screen floating_stats
    hide screen activity_failure
    hide screen citymap
    
    if hour <= 5:

        scene bg museum_day with dissolve
        
    if hour > 5:
        
        scene bg museum_night with dissolve

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_16_purevn
        
    $ tobeat = 40 + (stat_stress*2.5) + month*10 + week*2 - (stat_intelligence/3)
    show activity_background

    show job base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if sick == True:
        show sickicon
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind job,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show job success onlayer screens
        
        $ floatingstat = "+9 Money\n+2 Stress"
        $ stat_money += 9
        $ stat_stress += 2
        
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show job fail onlayer screens
        
        $ floatingstat = "+4 Money\n+3 Stress"
        $ stat_money += 4
        $ stat_stress += 3
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show job onlayer screens:
        ease 0.5 xpos -0.2
        
    if persistent.stat_money < stat_money:
        $ persistent.stat_money = stat_money
    $ achievement.grant_progress("money", stat_money,500)

    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide job onlayer screens
    hide screen floating_stats
    
    window show
        
    return


label purevn_visit_arcade:
    
    $ current_activity = "visit_arcade_retry"
    $ retry = False
    
label purevn_visit_arcade_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    
    if stat_money < 2:
        
        hide screen citymap
        hide screen activity_failure
        hide activity_arcade onlayer screens
        
        "I don't have enough money to go here."
        
        if retry == False:
        
            show screen citymap
            
            pause
                
        return
        
    if stat_money >= 2:
        
        hide screen citymap
        
        $ stat_money -= 2
        $ times_arcade += 1
        
        if persistent.times_arcade < times_arcade:
            $ persistent.times_arcade = times_arcade
        $ achievement.grant_progress("gamer", times_arcade,400)
            
        scene bg arcade with dissolve
        
        if retry == False:
            call arcade_events from _call_arcade_events_purevn

        if is_purevn():
            $ hour += 1
            window show
            return
        
        call diceroll from _call_diceroll_17_purevn

        $ tobeat = 20
        show activity_background

        call assist_enter from _call_assist_enter_7_purevn

        show activity_arcade base onlayer screens:
            xpos 1.2 ypos 0.5
            ease 0.5 xpos 0.5
            
        if quickact == False:
            pause 1.0
        
        if roll >= tobeat:
            
            play sound "Sounds/bertrof_success.ogg"
            
            call assist_success from _call_assist_success_4_purevn
            
            show activity_success behind activity_arcade,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
                xpos 0.5 ypos 0.5
            show activity_arcade success onlayer screens
            
            if sick == False:

                $ floatingstat = "-4 Stress\n-2 Intelligence"
                $ stat_stress -= 4
                $ stat_intelligence -= 2
                
            if sick == True:
                show sickicon
                $ floatingstat = "-2 Stress\n-2 Intelligence"
                $ stat_stress -= 2
                $ stat_intelligence -= 2

            if stat_stress < 0:
                $ stat_stress = 0
            if stat_intelligence < 0:
                $ stat_intelligence = 0

            show screen floating_stats

        if roll < tobeat:

            play sound "Sounds/gabrielaraujo_fail.ogg"
            
            call assist_fail from _call_assist_fail_4_purevn
            
            show screen activity_failure
            show activity_arcade fail onlayer screens
            
            if sick == False:
            
                $ floatingstat = "-1 Stress\n-2 Intelligence"
                $ stat_stress -= 1
                $ stat_intelligence -= 2
                
            if sick == True:
                show sickicon
                $ floatingstat = "+1 Stress\n-2 Intelligence"
                $ stat_stress += 1
                $ stat_intelligence -= 2

            if stat_stress < 0:
                $ stat_stress = 0
            if stat_intelligence < 0:
                $ stat_intelligence = 0

            show screen floating_stats

        if retry == False:
            $ hour += 1
            
        if quickact == False:
            $ renpy.pause(2.0)
        
        show activity_arcade onlayer screens:
            ease 0.5 xpos -0.2
        
        call assist_exit from _call_assist_exit_7_purevn
        
        pause 0.5
        
        hide activity_background
        hide activity_success
        hide screen activity_failure
        hide activity_arcade onlayer screens
        hide screen floating_stats
        
        window show
            
        return

       
label purevn_job_arcade:
            
    $ current_activity = "job_arcade_retry"
    $ retry = False

label purevn_job_arcade_retry:
            
    hide screen floating_stats
    hide screen activity_failure
    hide screen citymap
        
    scene bg arcade with dissolve

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_18_purevn

    $ tobeat = 30 + (stat_stress*1.5) - (times_arcade/2)
    show activity_background

    show job base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
        
    if quickact == False:
        pause 1.0
    
    if sick == True:
        show sickicon
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind job,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show job success onlayer screens
        
        $ floatingstat = "+5 Money\n+1 Stress"
        $ stat_money += 5
        $ stat_stress += 1
        
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show job fail onlayer screens
        
        $ floatingstat = "+2 Money\n+2 Stress"
        $ stat_money += 2
        $ stat_stress += 2
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show job onlayer screens:
        ease 0.5 xpos -0.2
    
    if persistent.stat_money < stat_money:
        $ persistent.stat_money = stat_money
    $ achievement.grant_progress("money", stat_money,500)
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide job onlayer screens
    hide screen floating_stats
    
    window show
        
    return
        

label purevn_visit_park:
    
    $ current_activity = "visit_park_retry"
    $ retry = False
    
label purevn_visit_park_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen citymap
    
    $ times_park += 1
    
    if persistent.times_park < times_park:
        $ persistent.times_park = times_park
    $ achievement.grant_progress("dog", times_park,400)

    if hour <= 5:

        scene bg park_day with dissolve
        
    if hour > 5:
        
        scene bg park_evening with dissolve
        
    if retry == False:
        call park_events from _call_park_events_purevn

    if is_purevn():
        $ hour += 1
        window show
        return
        

    call diceroll from _call_diceroll_19_purevn
        
    $ tobeat = 20 + (stat_stress/2)
    show activity_background

    call assist_enter from _call_assist_enter_8_purevn

    show activity_park base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0

    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        call assist_success from _call_assist_success_5_purevn
        
        show activity_success behind activity_park,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_park success onlayer screens
                    
        if sick == False:
        
            $ floatingstat = "-2 Stress\n+1 Fitness"
            $ stat_stress -= 2
            $ stat_fitness += 1
            
        if sick == True:
            
            show sickicon
            
            $ floatingstat = "+1 Stress\n+1 Fitness"
            $ stat_stress += 1
            $ stat_fitness += 1
        
        if stat_stress < 0:
            $ stat_stress = 0
                                                
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        call assist_fail from _call_assist_fail_5_purevn
        
        show screen activity_failure
        show activity_park fail onlayer screens
        
        $ floatingstat = "+1 Stress"
        $ stat_stress += 1
        
        show screen floating_stats
    
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_park onlayer screens:
        ease 0.5 xpos -0.2
    
    call assist_exit from _call_assist_exit_8_purevn
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide activity_park onlayer screens
    hide screen floating_stats

    window show

    return

      
label purevn_job_park:
            
    $ current_activity = "job_park_retry"
    $ retry = False
       
label purevn_job_park_retry:
            
    hide screen floating_stats
    hide screen activity_failure
    hide screen citymap
    
    if hour <= 5:

        scene bg park_day with dissolve
        
    if hour > 5:
        
        scene bg park_evening with dissolve

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_20_purevn

    $ tobeat = 30 + stat_stress - (stat_fitness/2)
    show activity_background

    show job base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if sick == True:
        show sickicon
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind job,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show job success onlayer screens
        
        $ floatingstat = "+4 Money\n+1 Stress"
        $ stat_money += 4
        $ stat_stress += 1
        
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show job fail onlayer screens
        
        $ floatingstat = "+2 Money\n+2 Stress"
        $ stat_money += 2
        $ stat_stress += 2
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show job onlayer screens:
        ease 0.5 xpos -0.2
    
    if persistent.stat_money < stat_money:
        $ persistent.stat_money = stat_money
    $ achievement.grant_progress("money", stat_money,500)
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide job onlayer screens
    hide screen floating_stats
    
    window show
        
    return
        

label purevn_visit_shrine:
    
    $ current_activity = "visit_shrine_retry"
    $ retry = False

label purevn_visit_shrine_retry:
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen citymap

    if hour <= 5:

        scene bg shrine_day with dissolve
        
    if hour > 5:
        
        scene bg shrine_evening with dissolve
        
    if retry == False:
        call shrine_events from _call_shrine_events_purevn
    
    if is_purevn():
        $ hour += 1
        window show
        return
        

    if persistent.times_shrine < times_shrine:
        $ persistent.times_shrine = times_shrine
    $ times_shrine += 1
    
    $ achievement.grant_progress("devout", times_shrine,400)
    
    window show
    
    show screen donation
    
    "\n\nPlease make a donation, if you are willing and able."
            

label purevn_job_shrine:

    $ current_activity = "job_shrine_retry"
    $ retry = False

label purevn_job_shrine_retry:

    hide screen floating_stats
    hide screen activity_failure
    hide screen citymap

    if hour <= 5:

        scene bg shrine_day with dissolve
        
    if hour > 5:
        
        scene bg shrine_evening with dissolve

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_22_purevn

    $ tobeat = 30 + stat_stress - times_shrine/2 - stat_fitness/2
    show activity_background

    show job base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind job,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show job success onlayer screens
        
        if sick == False:
        
            $ floatingstat = "+4 Money\n+1 Stress"
            $ stat_money += 4
            $ stat_stress += 1

        if sick == True:
        
            show sickicon
        
            $ floatingstat = "+4 Money\n+2 Stress"
            $ stat_money += 4
            $ stat_stress += 2         

        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show job fail onlayer screens

        if sick == False:

            $ floatingstat = "+2 Money\n+2 Stress\nSola's Disappointment"
            $ stat_money += 2
            $ stat_stress += 2
            $ affection_sola -= 1
            
        if sick == True:

            show sickicon

            $ floatingstat = "+2 Money\n+3 Stress\nSola's Disappointment"
            $ stat_money += 2
            $ stat_stress += 3
            $ affection_sola -= 1
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show job onlayer screens:
        ease 0.5 xpos -0.2
    
    $ achievement.grant_progress("money", stat_money,500)
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide job onlayer screens
    hide screen floating_stats
    
    window show
        
    return
    

label purevn_gym_exercise:
    
    $ current_activity = "gym_exercise_retry"
    $ retry = False
    
label purevn_gym_exercise_retry:
    
    window hide
    
    hide screen floating_stats
    hide screen activity_failure
    hide screen school_map
    
    $ times_gym += 1
    
    if persistent.times_gym < times_gym:
        $ persistent.times_gym = times_gym
    $ achievement.grant_progress("ripped", times_gym,200)

    if hour <= 5:

        scene bg gym with dissolve
        
    if hour > 5:
        
        scene bg gym_night with dissolve
        
    if retry == False:
        call gym_events from _call_gym_events_purevn

    if is_purevn():
        $ hour += 1
        window show
        return
        

    call diceroll from _call_diceroll_23_purevn
        
    $ tobeat = 20 + stat_stress
    
    show activity_background

    call assist_enter from _call_assist_enter_10_purevn

    show activity_exercise base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5

    if quickact == False:
        pause 1.0

    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        call assist_success from _call_assist_success_7_purevn
        
        show activity_success behind activity_exercise,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show activity_exercise success onlayer screens
        
        if sick == False:
        
            $ floatingstat = "+3 Fitness\n+2 Stress"
            $ stat_fitness += 3
            $ stat_stress += 2
            
        if sick == True:
            
            show sickicon
            
            $ floatingstat = "+3 Fitness\n+4 Stress"
            $ stat_fitness += 3
            $ stat_stress += 4
                
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        call assist_fail from _call_assist_fail_7_purevn
        
        show screen activity_failure
        show activity_exercise fail onlayer screens
        
        if sick == False:
        
            $ floatingstat = "+1 Fitness\n+3 Stress"
            $ stat_fitness += 1
            $ stat_stress += 3
        
        if sick == True:
            
            show sickicon
            
            $ floatingstat = "+1 Fitness\n+6 Stress"
            $ stat_fitness += 1
            $ stat_stress += 6
        
        show screen floating_stats
                            
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show activity_exercise onlayer screens:
        ease 0.5 xpos -0.2
    
    call assist_exit from _call_assist_exit_10_purevn
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide activity_exercise onlayer screens
    hide screen floating_stats
    
    window show
        
    return
    

label purevn_job_shop:
      
    $ current_activity = "job_shop_retry"
    $ retry = False
      
label purevn_job_shop_retry:
      
    hide screen floating_stats
    hide screen activity_failure
    hide screen citymap
    
    if hour <= 5:

        scene bg city_day with dissolve
        
    if hour > 5:
        
        scene bg city_night with dissolve

    if is_purevn():
        $ hour += 1
        window show
        return

    call diceroll from _call_diceroll_24_purevn

    $ tobeat = 34 + (stat_stress*2) + month*2 - stat_charisma
    show activity_background

    show job base onlayer screens:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
        
    if quickact == False:
        pause 1.0
    
    if sick == True:
        show sickicon
    
    if roll >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        
        show activity_success behind job,convo_asaga,convo_ava,convo_chigara,convo_sola,convo_maray:
            xpos 0.5 ypos 0.5
        show job success onlayer screens
        
        $ floatingstat = "+7 Money\n+2 Stress"
        $ stat_money += 7
        $ stat_stress += 2
        
        show screen floating_stats
        
    if roll < tobeat:
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        
        show screen activity_failure
        show job fail onlayer screens

        $ floatingstat = "+3 Money\n+3 Stress"
        $ stat_money += 3
        $ stat_stress += 3
        
        show screen floating_stats
        
    if retry == False:
        $ hour += 1
    
    if quickact == False:
        $ renpy.pause(2.0)
    
    show job onlayer screens:
        ease 0.5 xpos -0.2
    
    $ achievement.grant_progress("money", stat_money,500)
    
    pause 0.5
    
    hide activity_background
    hide activity_success
    hide screen activity_failure
    hide job onlayer screens
    hide screen floating_stats
    
    window show
        
    return
    
label purevn_visit_shop:
    
    hide screen citymap
    
    if hour <= 5:

        scene bg city_day with dissolve
        
    if hour > 5:
        
        scene bg city_night with dissolve
        
    call store_events from _call_store_events_purevn


    if is_purevn():
        window show
        return
        

    show screen shop_menu
    
    pause

    if showitem_spacewhalecolonge == False and showitem_alpacablanket == False and showitem_starraider == False and showitem_minorstudycharm == False and showitem_minorlovecharm == False and showitem_ryuvianshampoo == False and showitem_fancytie == False and showitem_balancedswords == False and showitem_uniongoggles == False and showitem_studycharm == False and showitem_majorstudycharm == False and showitem_encountercharm == False and showitem_lightbogu == False and showitem_mastersword == False and showitem_swimcap == False and showitem_protosuit == False and showitem_beakers == False and showitem_oresample == False and showitem_unionscanner == False and showitem_holo == False and showitem_retrycharm == False and showitem_admiralwatch == False and showitem_cementhair == False and showitem_fuzzysocks == False and showitem_stuffedwhale == False and showitem_incenceset == False and showitem_apron == False and showitem_historybook == False and showitem_sexypanties == False and showitem_recipebook == False and showitem_dragonbogu == False and showitem_ryuvianartifact == False and showitem_massagemachine == False and showitem_pillow == False:
        $ achievement.grant("soldout")
        $ persistent.soldout = True

label purevn_gohome:

    if hour < 6:
        
        if sick == False:
        
            hide screen citymap
            "It's too early to go back home."
            
            show screen citymap
            
            pause
            
        if competitionday == True:
        
            hide screen citymap
            "I can't go home on a competition day."
            
            show screen citymap
            
            pause
            
        if sick == True and competitionday == False:
            
            hide screen citymap
            
            if hour <= 5:
                scene bg room_day with dissolve
            if hour > 5:
                scene bg room_night with dissolve
            
            "Maybe I'll feel better after a nap..."
            
            jump act_sleep
        
    if hour >= 6:
    
        hide screen citymap
        scene bg room_night with dissolve
        
        call home_events from _call_home_events_purevn
            
        $ assist_maray = False
    
        if is_purevn():
            window show
            return
        
    return
    
label purevn_act_sleep:

    if nightskip == True:
        
        $ nightskip = False
        return

    $ sleep = True
    $ talk_maray = False
    $ assist_maray = False
    $ solashopping = False
    
    if is_purevn():
        scene bg room_night with dissolve
        $ hour = 7
        
        scene black with horizontalwipe

        $ hour = 1
        $ day += 1
        
        if day == 10:
            $ day = 0

        if week > 5:
            $ week = 1
            $ month += 1

        scene bg room_morning with horizontalwipe

        if purevn.developer == True:
            jump purevn_debug_jump_to_choice
    
        window show
        return

    if stat_stress >= 50 and challenge_day < 20:

        $ challenge_day += 1
        
        if persistent.challenge_day < 20:
            $ persistent.challenge_day = challenge_day
        $ achievement.progress("challenge", challenge_day, 20)

    if stat_stress < 50 and challenge_day < 20:
        
        $ challenge_day = 0
        $ persistent.challenge_day = challenge_day

    if hour > 5:
        scene bg room_night
    if hour <= 5:
        scene bg room_day
    
    show activity_background
    show kayto_sleep:
        xpos 1.2 ypos 0.5
        ease 0.5 xpos 0.5
        
    pause 1.0
    
    call diceroll from _call_diceroll_25_purevn

    if haveitem_alpacablanket == True and roll >= 50:
        $ floatingstat = 11-hour
        $ stat_stress -= 11-hour
    else:
        $ floatingstat = 10-hour
        $ stat_stress -= 10-hour

    show screen floating_stats
    
    if stat_stress < 0:
        $ stat_stress = 0
    
    $ renpy.pause(1.5)
    
    jump act_sleep_repeat
        
label purevn_act_sleep_repeat:
        
    if hour == 5:
        scene bg room_night
        show activity_background
        show kayto_sleep:
            xpos 0.5 ypos 0.5
        with dissolve
        
    if hour == 9:
        $ hour = 0
        if is_not_purevn():
            call sleep_loss from _call_sleep_loss_purevn
        $ renpy.pause(1.5)
    
    if hour < 9 and hour != 0:
        $ hour += 1
        if is_not_purevn():
            call sleep_loss from _call_sleep_loss_1_purevn
        $ renpy.pause(1.5)
        jump act_sleep_repeat
        
    hide screen floating_stats
    scene bg room_morning
    show activity_background
    show kayto_sleep:
        xpos 0.5 ypos 0.5
    with dissolve

    if day == 0:
        $ week += 1

    $ hour = 1
    $ day += 1
    
    if day == 10:
        $ day = 0

    if week > 5:
        $ week = 1
        $ month += 1
                        
    $ renpy.pause(0.5)
    
    $ sleep = False
    
    show kayto_sleep:
        ease 0.5 xpos -0.4

    pause 0.5

    hide activity_background
    hide kayto_sleep
    hide screen floating_stats
    
    window show

    return

label purevn_sleep_loss:
    
    if haveitem_pillow == False:
        $ roll = renpy.random.randint(1,10)
    if haveitem_pillow == True:
        $ roll = renpy.random.randint(1,14)

    if is_purevn():
        $ roll = 10
    
    if roll == 1:

        call diceroll from _call_diceroll_26_purevn
        $ tobeat = 20 + stat_stress + stat_fitness
        
        if roll < tobeat and stat_fitness > 1:
        
            hide screen floating_stats
            $ sleep = False
            $ floatingstat = "-1 Fitness"
            $ stat_fitness -= 1
            show screen floating_stats
    
    if roll == 2 or roll == 10:

        call diceroll from _call_diceroll_27_purevn
        $ tobeat = 20 + stat_stress + stat_intelligence
        
        if roll < tobeat and stat_intelligence > 1:
        
            hide screen floating_stats
            $ sleep = False
            $ floatingstat = "-1 Intelligence"
            $ stat_intelligence -= 1    
            show screen floating_stats
            
    if roll == 3:

        call diceroll from _call_diceroll_28_purevn
        $ tobeat = 20 + stat_stress + stat_charisma
        
        if roll < tobeat and stat_charisma > 1:
        
            hide screen floating_stats
            $ sleep = False
            $ floatingstat = "-1 Charisma"
            $ stat_charisma -= 1        
            show screen floating_stats
            
    if roll >= 4 and roll <= 6:
        
        call diceroll from _call_diceroll_29_purevn
            
        $ tobeat = 30 + (stat_luck*2)
        
        if roll < tobeat:
        
            hide screen floating_stats
            $ sleep = False
            
            if stat_luck < 10:            
                $ floatingstat = "-1 Luck"
                $ stat_luck -= 1

            if stat_luck >= 10 and stat_luck < 20:            
                $ floatingstat = "-2 Luck"
                $ stat_luck -= 2

            if stat_luck >= 20 and stat_luck < 25:            
                $ floatingstat = "-3 Luck"
                $ stat_luck -= 3

            if stat_luck >= 25 and stat_luck < 30:            
                $ floatingstat = "-4 Luck"
                $ stat_luck -= 4
                
            if stat_luck >= 30:            
                $ floatingstat = "-5 Luck"
                $ stat_luck -= 5
            
            show screen floating_stats
            
    if roll == 7:

        call diceroll from _call_diceroll_30_purevn
        $ tobeat = 20 + stat_kendo_readiness - stat_kendo_morale
        
        if roll < tobeat:
        
            hide screen floating_stats
            $ sleep = False
            $ floatingstat = "-1 Kendo Readiness"
            $ stat_kendo_readiness -= 1        
            show screen floating_stats

    if roll == 8:

        call diceroll from _call_diceroll_31_purevn
        $ tobeat = 20 + stat_science_readiness - stat_science_morale
        
        if roll < tobeat:
        
            hide screen floating_stats
            $ sleep = False
            $ floatingstat = "-1 Science Readiness"
            $ stat_science_readiness -= 1        
            show screen floating_stats

    if roll == 9:

        call diceroll from _call_diceroll_32_purevn
        $ tobeat = 20 + stat_swim_readiness - stat_swim_morale
        
        if roll < tobeat:
        
            hide screen floating_stats
            $ sleep = False
            $ floatingstat = "-1 Swim Readiness"
            $ stat_swim_readiness -= 1        
            show screen floating_stats

            
    return


label purevn_kendorounds:
    if is_purevn():
        scene black:
            pause 2.0
        with dissolvemedium
        scene bg gym with dissolve
        call purevn_choice_outcome_win from _call_kendorounds_purevn_choice_outcome_win
        jump purevn_kendorounds_end

    show competition_kendo:
        xpos 0.65 ypos 0.5
    show competition_asaga:
        xpos 0.35 ypos 0.5
    with dissolve
        
    pause 1.0
        
    show competition_kendo:
        ease 0.2 xpos 0.65
        ease 0.2 xpos 0.64
        ease 0.4 xpos 0.66
        repeat
    show competition_asaga:
        ease 0.25 xpos 0.35
        ease 0.25 xpos 0.34
        ease 0.45 xpos 0.36
        repeat
        
    $ renpy.pause(2.0)
    
    $ luck_mod = (stat_luck/2)-((difficulty-2)*month)

    if month == 1:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo1_ran+luck_mod-25)
    if month == 2:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo2_ran+luck_mod-25)
    if month == 3:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo3_ran+luck_mod-25)
    if month == 4:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo4_ran+luck_mod-25)
    if month == 5:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo5_ran+luck_mod-25)
    if month == 6:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo6_ran+luck_mod-25)
    if month == 7:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo7_ran+luck_mod-25)
    if month == 8:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo8_ran+luck_mod-25)
    if month == 9:
        $ mypower = (((stat_kendo_readiness*stat_kendo_member)+stat_kendo_morale)/month)+(kendo9_ran+luck_mod-25)
    
    if month < 7:
        $ tobeat = 55+(23*month)+(comp_round*15)+(win*(difficulty-2)*8)
    
    if month == 7:
        $ tobeat = 60+(23*month)+(comp_round*15)+(win*15)+(win*(difficulty-2)*8)
    if month == 8:
        $ tobeat = 70+(23*month)+(comp_round*20)+(win*20)+(win*(difficulty-2)*8)
    if month == 9:
        $ tobeat = 90+(23*month)+(comp_round*25)+(win*25)+(win*(difficulty-2)*12)
    
    if mypower >= tobeat:
        
        play sound "Sounds/kendodie.ogg"
        show activity_success behind competition_asaga,competition_kendo:
            xpos 0.5 ypos 0.5
    
        show competition_asaga:
            ease 0.3 xpos 0.7
        show competition_kendo:
            ease 0.2 ypos 0.45
            ease 0.8 ypos 1.5
            
        $ win += 1
                
    if mypower < tobeat:
        
        play sound "Sounds/kendodie.ogg"
        show activity_failure behind competition_asaga,competition_kendo:
            xpos 0.5 ypos 0.5
            
        show competition_kendo:
            ease 0.3 xpos 0.3
        show competition_asaga:
            ease 0.2 ypos 0.45
            ease 0.8 ypos 1.5
            
    $ comp_round += 1
    
    $ renpy.pause(2.0)
    
    hide activity_failure
    hide activity_success
    with dissolve
    
    if comp_round < 3:
        
        jump kendorounds

label purevn_kendorounds_end:

    stop music fadeout 1.5
    hide competition_kendo
    hide competition_asaga
    hide activity_background behind competition_kendo, competition_asaga
    with dissolve
        
    if win == 3:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show gold_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5
            
        $ stat_kendo_prestige += 50
        $ stat_prestige += 50
        $ affection_asaga += 6
        
    if win == 2:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show silver_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5

        $ stat_kendo_prestige += 30
        $ stat_prestige += 30
        $ affection_asaga += 4

    if win == 1:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show bronze_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5
            
        $ stat_kendo_prestige += 10
        $ stat_prestige += 10
        $ affection_asaga += 2
        
    if win == 0:
        
        call breakmusic from _call_breakmusic_purevn
        $ affection_asaga -= 3

    if month == 7 and win == 0:
        $ kendo_nationals = False
    if month == 7 and win > 0:
        $ kendo_nationals = True
        
    if month == 8 and win <= 1:
        $ kendo_galactic = False
    if month == 8 and win >= 2:
        $ kendo_galactic = True

    $ hour += 2
    call kendocompetitionend_events from _call_kendocompetitionend_events_purevn

    return


label purevn_swimrounds:
    if is_purevn():
        scene black:
            pause 2.0
        with dissolvemedium
        scene bg pool with dissolve
        call purevn_choice_outcome_win from _call_swimrounds_purevn_choice_outcome_win
        jump purevn_swimrounds_end
        
    show competition_swim:
        ypos 0.5 xpos 0.5
    show competition_sola:
        ypos 0.65 xpos 0.5
    with dissolve
        
    pause 1.0
        
    show competition_swim:
        ease 0.5 xpos 0.55
        ease 0.5 xpos 0.45
        ease 1.0 xpos 0.5
        repeat
    show competition_sola:
        ease 0.55 xpos 0.55
        ease 0.55 xpos 0.45
        ease 1.1 xpos 0.5
        repeat
        
    $ renpy.pause(2.0)
        
    $ luck_mod = (stat_luck/2)-((difficulty-2)*month)

    if month == 1:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim1_ran+luck_mod-25)
    if month == 2:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim2_ran+luck_mod-25)
    if month == 3:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim3_ran+luck_mod-25)
    if month == 4:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim4_ran+luck_mod-25)
    if month == 5:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim5_ran+luck_mod-25)
    if month == 6:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim6_ran+luck_mod-25)
    if month == 7:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim7_ran+luck_mod-25)
    if month == 8:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim8_ran+luck_mod-25)
    if month == 9:
        $ mypower = (((stat_swim_readiness*stat_swim_member)+stat_swim_morale)/month)+(swim9_ran+luck_mod-25)
    
    if month < 7:
        $ tobeat = 55+(23*month)+(comp_round*15)+(win*(difficulty-2)*8)
    if month == 7:
        $ tobeat = 60+(23*month)+(comp_round*15)+(win*15)+(win*(difficulty-2)*8)
    if month == 8:
        $ tobeat = 70+(23*month)+(comp_round*20)+(win*20)+(win*(difficulty-2)*8)
    if month == 9:
        $ tobeat = 90+(23*month)+(comp_round*25)+(win*25)+(win*(difficulty-2)*12)
    
    if mypower >= tobeat:
            
        show competition_sola:
            ease 1.0 xpos 0.7
        show competition_swim:
            ease 1.0 xpos 0.3
        
        pause 0.5
        
        play sound "Sounds/bertrof_success.ogg"
        show activity_success behind competition_swim,competition_sola:
            xpos 0.5 ypos 0.5
        
        $ win += 1
                
    if mypower < tobeat:
                    
        show competition_swim:
            ease 1.0 xpos 0.7
        show competition_sola:
            ease 1.0 xpos 0.3
            
        pause 0.5
        
        play sound "Sounds/gabrielaraujo_fail.ogg"
        show activity_failure behind competition_swim,competition_sola:
            xpos 0.5 ypos 0.5
            
    $ comp_round += 1
    
    $ renpy.pause(2.0)
    
    hide activity_failure
    hide activity_success
    with dissolve
    
    if comp_round < 3:
        
        jump swimrounds

label purevn_swimrounds_end:
    
    stop music fadeout 1.5
    hide competition_swim
    hide competition_sola
    hide activity_background behind competition_swim, competition_sola
    with dissolve
        
    if win == 3:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show gold_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5
            
        $ stat_swim_prestige += 50
        $ stat_prestige += 50
        $ affection_sola += 6
        
    if win == 2:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show silver_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5

        $ stat_swim_prestige += 30
        $ stat_prestige += 30
        $ affection_sola += 4

    if win == 1:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show bronze_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5
            
        $ stat_swim_prestige += 10
        $ stat_prestige += 10
        $ affection_sola += 2
        
    if win == 0:
        
        call breakmusic from _call_breakmusic_1_purevn
        $ affection_sola -= 3

    if month == 7 and win == 0:
        $ swim_nationals = False
    if month == 7 and win > 0:
        $ swim_nationals = True
        
    if month == 8 and win <= 1:
        $ swim_galactic = False
    if month == 8 and win >= 2:
        $ swim_galactic = True

    $ hour += 2
    call swimcompetitionend_events from _call_swimcompetitionend_events_purevn

    return
    

label purevn_sciencerounds:
    if is_purevn():
        scene black:
            pause 2.0
        with dissolvemedium
        scene bg museum_day with dissolve
        call purevn_choice_outcome_win from _call_sciencerounds_purevn_choice_outcome_win
        jump purevn_sciencerounds_end

    show sciencecompetition base:
        ypos 0.5 xpos 1.3
        ease 0.5 xpos 0.5

    $ renpy.pause(2.0)
        
    $ luck_mod = (stat_luck/2)-((difficulty-2)*month)

    if month == 2:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science1_ran+luck_mod-25)
    if month == 3:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science2_ran+luck_mod-25)
    if month == 4:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science3_ran+luck_mod-25)
    if month == 5:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science4_ran+luck_mod-25)
    if month == 6:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science5_ran+luck_mod-25)
    if month == 7:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science6_ran+luck_mod-25)
    if month == 8:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science7_ran+luck_mod-25)
    if month == 9 and week == 1:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science8_ran+luck_mod-25)
    if month == 9 and week == 4:
        $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+(science9_ran+luck_mod-25)

    $ mypower = (((stat_science_readiness*stat_science_member)+stat_science_morale)/month)+((roll/2)-25)
    
    if month < 8:
        $ tobeat = 55+(23*month)+(comp_round*15)+(win*(difficulty-2)*8)
    if month == 8:
        $ tobeat = 60+(23*month)+(comp_round*15)+(win*15)+(win*(difficulty-2)*8)
    if month == 9 and week == 1:
        $ tobeat = 70+(23*month)+(comp_round*20)+(win*20)+(win*(difficulty-2)*8)
    if month == 9 and week == 4:
        $ tobeat = 90+(23*month)+(comp_round*25)+(win*25)+(win*(difficulty-2)*12)
    
    if mypower >= tobeat:
        
        play sound "Sounds/bertrof_success.ogg"
        show activity_success behind sciencecompetition:
            xpos 0.5 ypos 0.5
        show sciencecompetition success:
            xpos 0.5 ypos 0.5
            pause 1.0
            ease 0.5 xpos -0.3

        $ win += 1

    if mypower < tobeat:
        
        play sound "Sounds/explosion.ogg"
        show activity_failure behind sciencecompetition:
            xpos 0.5 ypos 0.5
            
        show sciencecompetition fail:
            xpos 0.5 ypos 0.5
            pause 1.0
            ease 0.5 xpos -0.3

    $ comp_round += 1
    
    $ renpy.pause(2.0)
    
    hide activity_failure
    hide activity_success
    with dissolve
    
    if comp_round < 3:
        
        jump sciencerounds
        
label purevn_sciencerounds_end:

    stop music fadeout 1.5
    hide sciencecompetition
    hide activity_background
    with dissolve
        
    if win == 3:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show gold_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5
            
        $ stat_science_prestige += 50
        $ stat_prestige += 50
        $ affection_chigara += 6
        
    if win == 2:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show silver_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5

        $ stat_science_prestige += 30
        $ stat_prestige += 30
        $ affection_chigara += 4

    if win == 1:
        
        play music "Music/suisougakubunonatsu.ogg" fadeout 1.5
        play sound "Sounds/applause.ogg"
        
        show bronze_winner:
            xpos 1.5 ypos 0.5
            ease 0.5 xpos 0.5
            pause 4.0
            ease 0.5 xpos -0.5

        $ stat_science_prestige += 10
        $ stat_prestige += 10
        $ affection_chigara += 2

    if win == 0:

        call breakmusic from _call_breakmusic_2_purevn
        $ affection_chigara -= 3
        
    if month == 8 and win == 0:
        $ science_nationals = False
    if month == 8 and win > 0:
        $ science_nationals = True
        
    if month == 9 and week == 1 and win <= 1:
        $ science_galactic = False
    if month == 9 and week == 1 and win >= 2:
        $ science_galactic = True
        
    $ hour += 2
    call sciencecompetitionend_events from _call_sciencecompetitionend_events_purevn

    return
    
label purevn_examresults_calc:
    
    $ luck_mod = (stat_luck/2)-((difficulty-2)*8)
    
    if month == 1:
        $ exam_score = 25*(stat_intelligence*exam1_ran+luck_mod)/(20+(25*month))
    if month == 2:
        $ exam_score = 25*(stat_intelligence*exam2_ran+luck_mod)/(20+(25*month))
    if month == 3:
        $ exam_score = 25*(stat_intelligence*exam3_ran+luck_mod)/(20+(25*month))
    if month == 4:
        $ exam_score = 25*(stat_intelligence*exam4_ran+luck_mod)/(20+(25*month))
    if month == 5:
        $ exam_score = 25*(stat_intelligence*exam5_ran+luck_mod)/(20+(25*month))
    if month == 6:
        $ exam_score = 25*(stat_intelligence*exam6_ran+luck_mod)/(20+(25*month))
    if month == 7:
        $ exam_score = 25*(stat_intelligence*exam7_ran+luck_mod)/(20+(25*month))
    if month == 8:
        $ exam_score = 25*(stat_intelligence*exam8_ran+luck_mod)/(20+(25*month))
    if month == 9:
        $ exam_score = 25*(stat_intelligence*exam9_ran+luck_mod)/(20+(25*month))
        
    $ exam_score = int(round(exam_score))
    
    if sick == True:
        $ exam_score -= 5
    
    $ homework_score = 40-(homework_fail*2)
    
    if haveitem_minorstudycharm == True:
        $ exam_score += 1
    if haveitem_studycharm == True:
        $ exam_score += 2
    if haveitem_majorstudycharm == True:
        $ exam_score += 3

    if is_purevn():
        scene bg classroom with dissolve
        call purevn_choice_outcome_grade from _call_examresults_purevn_choice_outcome_grade

    if homework_score < 0:
        $ homework_score = 0

    $ stat_grade = int(homework_score+exam_score)
        
    if stat_grade < 1:
        $ stat_grade = 1
    if stat_grade > 99:
        $ stat_grade = 99
        
    if stat_grade >= 60:
        
        play music "Music/orchestrajingle.ogg" fadeout 1.5
        
        if stat_grade > 80:
            $ affection_ava += 9
        if stat_grade > 70 and stat_grade <= 80:
            $ affection_ava += 6
        if stat_grade > 60 and stat_grade <= 70:
            $ affection_ava += 3

    if stat_grade < 60:
        
        play music "Music/unmei.ogg" fadeout 1.5
        
        $ academicprobation += 1
        $ haveitem_academicprobation = True
        $ affection_ava -= 3
        
    if stat_grade >= 99:
        
        $ achievement.grant("genius")
        $ persistent.genius = True
        
    show screen examresults

    $ renpy.pause()

    hide screen examresults
    
    if academicprobation >= 3:
        jump badend_flunk

    return

label purevn_finalexamresults_calc:
    
    $ luck_mod = (stat_luck/2)-((difficulty-2)*8)
    
    if month == 5 and day == 7:
        $ exam_score = 100*(stat_intelligence*exam5b_ran+luck_mod)/(70*month)
    if month == 5 and day == 8:
        $ exam_score = 100*(stat_intelligence*exam5c_ran+luck_mod)/(70*month)
        
    if month == 9 and day == 7:
        $ exam_score = 100*(stat_intelligence*exam9b_ran+luck_mod)/(70*month)
    if month == 9 and day == 8:
        $ exam_score = 100*(stat_intelligence*exam9c_ran+luck_mod)/(70*month)

    $ exam_score = int(round(exam_score))
    $ homework_score = "N/A"
    
    if exam_score > 99:
        $ exam_score = 99
    
    if sick == True:
        $ exam_score -= 10

    if haveitem_minorstudycharm == True:
        $ exam_score += 3
    if haveitem_studycharm == True:
        $ exam_score += 6
    if haveitem_majorstudycharm == True:
        $ exam_score += 10

    if is_purevn():
        scene bg classroom with dissolve
        call purevn_choice_outcome_grade from _call_finalexamresults_purevn_choice_outcome_grade

    $ stat_grade = exam_score
        
    if stat_grade < 1:
        $ stat_grade = 1
    if stat_grade > 99:
        $ stat_grade = 99
        
    if stat_grade >= 60:
        
        play music "Music/orchestrajingle.ogg" fadeout 1.5
        
    if stat_grade < 60:
        
        play music "Music/unmei.ogg" fadeout 1.5
        
        $ academicprobation += 1
        $ haveitem_academicprobation = True
        
    show screen examresults

    if stat_grade >= 99:
        
        $ achievement.grant("genius")
        $ persistent.genius = True

    $ renpy.pause()

    hide screen examresults

    if academicprobation >= 3:
        jump badend_flunk

    return