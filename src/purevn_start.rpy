init +2 python:
    # Keep track of the old callback so it can still be called
    purevn_original_label_callback = config.label_callback

    # Hijack the beginning of the class_selection label (which is not called or jumped to)
    def purevn_label_callback(label, abnormal):
        # Make sure to call the original label callback too
        purevn_original_label_callback(label, abnormal)

        # Jump to PureVN setup choice and tutorial
        if label == 'class_selection' and purevn_setup == False:
            renpy.jump('purevn_start')
            
    config.label_callback = purevn_label_callback

label purevn_start:
    tut "The PureVN Mod ([purevn_version]) is present. Enabling PureVN Mode will automate all non-scripted activity choices.\n\nWhile normally victory is set in stone, enabling Choice Outcome will allow you to decide the outcome competitions, exams, and the election."
    
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

label purevn_class_selection:
    call purevn_decision_wipe from _call_class_selection_purevn_decision_wipe

    $ purevn_setup = True

    if purevn == True:
        tut "To enable/disable PureVN or Choice Outcome, use the following commands:\n\npurevn = True/False\npurevn_choice_outcome = True/False"
        
        # No stat calculation, go full Buffsuki
        call purevn_full_stats from _call_class_selection_purevn_full_stats
        jump class_selected

    else:
        jump class_selection