init +2 python:
    # Keep track of the old callback so it can still be called
    purevn_original_label_callback = config.label_callback

    # Hijack the beginning of the class_selection label (which is not called or jumped to)
    def purevn_label_callback(label, abnormal):
        # Make sure to call the original label callback too
        purevn_original_label_callback(label, abnormal)

        # Jump to PureVN setup choice and tutorial
        if label == 'class_selection':
            renpy.jump('purevn_start')
            
    config.label_callback = purevn_label_callback

label purevn_start:
    #hide stat onlayer screens
    #hide screen class_select
    #with dissolve

    #tut "The PureVN mod is present. Enabling PureVN will automate all non-scripted activity choices."
    #tut "Enabling PureVN & Choice Outcome, will allow you to decide competition and election outcomes."
    tut "The PureVN mod is present. Enabling PureVN will automate all non-scripted activity choices.\n\nWhile normally victory is set in stone, enabling Choice Outcome will allow you to decide competition and election outcomes."
    #TODO: Exam outcomes in the future?

    $ choice1_text = "Normal Mode"
    $ choice1_jump = "purevn_start_off"

    $ choice2_text = "PureVN Mode"
    $ choice2_jump = "purevn_start_on"

    $ decision_extra = True
    $ choice3_text = "PureVN Mode & Choice Outcome"
    $ choice3_jump = "purevn_start_choice_outcome"

    show screen purevn_decision4

    pause

label purevn_start_off:
    $ purevn = False
    $ purevn_choice_outcome = False
    jump purevn_class_selection

label purevn_start_on:
    $ purevn = True
    $ purevn_choice_outcome = False
    jump purevn_class_selection
    
label purevn_start_choice_outcome:
    $ purevn = True
    $ purevn_choice_outcome = True
    jump purevn_class_selection
    

label purevn_stat_calc:
    call purevn_decision_wipe from _call_class_selection_purevn_decision_wipe

    if purevn == True:
        "To enable or disable PureVN at anytime, open the console and enter 'purevn = True' or 'purevn = False'."
        "To enable or disable PureVN Choice Outcome at anytime, open the console and enter 'purevn_choice_outcome = True' or 'purevn_choice_outcome = False'."
        
        # No stat calculation, go full Buffsuki
        call purevn_full_stats from _call_class_selection_purevn_full_stats
        jump class_selected

    if stat_class == 0 or disp_class == 0:
        $ stat_fitness = " "
        $ stat_intelligence = " "
        $ stat_charisma = " "
        $ stat_stress = " "
        $ stat_money = " "
        $ stat_luck = " "
        $ stat_grade = " "
        $ stat_prestige = " "
        $ stat_homework = " "
    
    if stat_class == 1 or disp_class == 1:
        $ stat_fitness = 30
        $ stat_intelligence = 10
        $ stat_charisma = 10
        $ stat_stress = 0
        $ stat_money = 10
        $ stat_luck = 0
        $ stat_grade = 0
        $ stat_prestige = 0
        $ stat_homework = 0

    if stat_class == 2 or disp_class == 2:
        $ stat_fitness = 10
        $ stat_intelligence = 30
        $ stat_charisma = 10
        $ stat_stress = 0
        $ stat_money = 10
        $ stat_luck = 0
        $ stat_grade = 0
        $ stat_prestige = 0
        $ stat_homework = "{size=25}-1 per week{/size}"
        
    if stat_class == 3 or disp_class == 3:
        $ stat_fitness = 10
        $ stat_intelligence = 10
        $ stat_charisma = 30
        $ stat_stress = 0
        $ stat_money = 10
        $ stat_luck = 0
        $ stat_grade = 0
        $ stat_prestige = 0
        $ stat_homework = 0
        
    if stat_class == 4 or disp_class == 4:
        $ stat_fitness = 8
        $ stat_intelligence = 5
        $ stat_charisma = 5
        $ stat_stress = 0
        $ stat_money = 10
        $ stat_luck = 25
        $ stat_grade = 0
        $ stat_prestige = 0
        $ stat_homework = 0
        
    if stat_class == 5 or disp_class == 5:
        $ stat_fitness = 15
        $ stat_intelligence = 15
        $ stat_charisma = 15
        $ stat_stress = 0
        $ stat_money = 10
        $ stat_luck = 0
        $ stat_grade = 0
        $ stat_prestige = 0
        $ stat_homework = 0

    if stat_class == 6 or disp_class == 6:
        $ stat_fitness = 8
        $ stat_intelligence = 8
        $ stat_charisma = 8
        $ stat_stress = 0
        $ stat_money = 50
        $ stat_luck = 0
        $ stat_grade = 0
        $ stat_prestige = "{size=25}+10 per month{/size}"
        $ stat_homework = 0
        
    if disp_class == 1 or stat_class == 1:
        show stat athletic onlayer screens zorder 300:
            xpos 1250 ypos 510 zoom 0.5
    if disp_class == 2 or stat_class == 2:
        show stat intellectual onlayer screens zorder 300:
            xpos 1250 ypos 510 zoom 0.5
    if disp_class == 3 or stat_class == 3:
        show stat charismatic onlayer screens zorder 300:
            xpos 1250 ypos 510 zoom 0.5
    if disp_class == 4 or stat_class == 4:
        show stat karma onlayer screens zorder 300:
            xpos 1250 ypos 510 zoom 0.5
    if disp_class == 5 or stat_class == 5:
        show stat rounded onlayer screens zorder 300:
            xpos 1250 ypos 510 zoom 0.5
    if disp_class == 6 or stat_class == 6:
        show stat heir onlayer screens zorder 300:
            xpos 1250 ypos 510 zoom 0.5

    pause

label purevn_class_selection:
    call purevn_decision_wipe from _call_class_selection_purevn_decision_wipe

    $ purevn_setup = True

    if purevn == True:
        #tut "To enable or disable PureVN at anytime, open the console and enter 'purevn = True' or 'purevn = False'. To enable or disable PureVN Choice Outcome at anytime, open the console and enter 'purevn_choice_outcome = True' or 'purevn_choice_outcome = False'."
        
        #tut "To enable or disable PureVN at anytime, open the console and enter 'purevn = True' or 'purevn = False'."
        #tut "To enable or disable PureVN Choice Outcome at anytime, open the console and enter 'purevn_choice_outcome = True' or 'purevn_choice_outcome = False'."
        tut "To enable/disable PureVN or Choice Outcome, use the following commands:\n\npurevn = True/False\npurevn_choice_outcome = True/False"
        
        # No stat calculation, go full Buffsuki
        call purevn_full_stats from _call_class_selection_purevn_full_stats
        jump class_selected

    else:
        jump class_selection
        #show screen class_select
        #with dissolve
        #jump stat_calc
    #return