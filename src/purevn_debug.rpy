label purevn_debug_jump_to_choice:
    # Disable developer mode again, (one choice per enable)
    # This way we won't be bothered with a choice every night
    $ purevn.developer = False

    # Power up the Microwave bois, we goin' time-traveling!
    $ choice1_text = "Competition"
    $ choice1_jump = "purevn_debug_jump_to_choice_competition"

    $ choice2_text = "Exam"
    $ choice2_jump = "purevn_debug_jump_to_choice_exam"

    $ purevn.decision_extra = True
    $ choice3_text = "Final Exam"
    $ choice3_jump = "purevn_debug_jump_to_choice_finalexam"

    $ purevn.decision_extra_2 = True
    $ choice4_text = "Election"
    $ choice4_jump = "purevn_debug_jump_to_choice_election"

    # Needs to be skipped so jumps are faster to test
    $ seen_labels.add("asagacooklunch")
    $ seen_labels.add("chigara_cooklunch")
    $ seen_labels.add("m1w2_avaapartmentfront")
    $ seen_labels.add("m1w2_asagahallway")
    $ seen_labels.add("m1w2_solashrine")
    $ seen_labels.add("m1w1_sola_courtyard")
    $ seen_labels.add("m1w4_courtyard")
    $ seen_labels.add("m2w4_hallway")
    $ seen_labels.add("m2w4_councilroom")
    $ seen_labels.add("m3w4_councilroom_incident")
    $ seen_labels.add("m3w5_incident_councilroom2")
    $ seen_labels.add("m4_asagatalklynnhallway")
    $ seen_labels.add("m9_class")
    $ seen_labels.add("m9_electionstart")
    $ seen_labels.add("m9_asaga_fontanasabotage")

    show screen purevn_decision4
    pause

init python:
    def purevn_jump_to_date(m,w,d):
        global month, week, day
        month = m
        week = w
        day = d
        renpy.set_return_stack([])
        renpy.jump("m{0}w{1}".format(m,w))

label purevn_debug_jump_to_choice_competition:
    # First Kendo Competition
    $ purevn_jump_to_date(1,3,9)
    return

label purevn_debug_jump_to_choice_exam:
    # First Exam
    $ purevn_jump_to_date(1,5,8)
    return

label purevn_debug_jump_to_choice_finalexam:
    # First Final Exams
    $ purevn_jump_to_date(5,2,6)
    return

label purevn_debug_jump_to_choice_election:
    # Student Council Election
    $ purevn_jump_to_date(9,5,2)
    return