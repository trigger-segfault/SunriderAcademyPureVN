init +2 python:
    # Keep track of the old callback so it can still be called
    purevn_original_label_callback = config.label_callback

    # Hijack the beginning of the class_selection label (which is not called or jumped to)
    def purevn_label_callback(label, abnormal):
        # Make sure PureVN is defined or upgrade PureVN structure
        #if purevn == None:
        #    purevn = PureVN()
        #elif purevn == False or purevn == True:
        #    raise Exception("PureVN ({0}) is not compatible with pre-release v0.1.0.0!".format(PureVN().version))

        # Make sure to call the original label callback too
        purevn_original_label_callback(label, abnormal)

        # Jump to PureVN setup choice and tutorial
        if label == 'start' and chap_select == True and purevn_ensure().setup == False:
            renpy.jump('purevn_start')
        if label == 'class_selection' and purevn_ensure().setup == False:
            renpy.jump('purevn_start')

        # Override here because this label is walked into from the end of the previous label
        if label == 'voteadd' and is_purevn() and purevn.election_outcome == False:
            renpy.jump('purevn_choice_outcome_election')
            
    config.label_callback = purevn_label_callback

label purevn_start:
    #if chap_select == True:
    #    scene bg room_morning with dissolve

    $ purevn = PureVN()
    tut "The PureVN Mod ([purevn.version]) is present. Enabling PureVN Mode will automate all non-scripted activity choices.\n\nWhile normally victory is set in stone, enabling Choice Outcome will allow you to decide the outcome competitions, exams, and the election."
    
    $ choice1_text = "Normal Mode"
    $ choice1_jump = "purevn_start_off"

    $ choice2_text = "PureVN Mode"
    $ choice2_jump = "purevn_start_on"

    $ purevn.decision_extra = True
    $ choice3_text = "PureVN Mode & Choice Outcome"
    $ choice3_jump = "purevn_start_choice_outcome"

    show screen purevn_decision4

    pause

label purevn_start_off:
    $ purevn.enabled = False
    $ purevn.choice_outcome = False
    jump purevn_class_selection

label purevn_start_on:
    $ purevn.enabled = True
    $ purevn.choice_outcome = False
    jump purevn_class_selection
    
label purevn_start_choice_outcome:
    $ purevn.enabled = True
    $ purevn.choice_outcome = True
    jump purevn_class_selection

label purevn_class_selection:
    $ purevn.setup = True

    if chap_select == True:
        scene black with dissolve
        return

    if is_purevn():
        # No stat calculation, go full Buffsuki
        call purevn_full_stats from _call_class_selection_purevn_full_stats
        jump class_selected

    else:
        jump class_selection