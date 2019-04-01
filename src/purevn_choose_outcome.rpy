#init python:
    # Choose student council election outcome
    #config.label_overrides['voteadd'] = 'purevn_voteadd'

# Competition Outcome
label purevn_choice_outcome_win:
    if purevn.choice_outcome == False:
        $ win = 3
        return

    $ choice1_text = "Gold"
    $ choice1_jump = "purevn_choice_outcome_win_3"

    $ choice2_text = "Silver"
    $ choice2_jump = "purevn_choice_outcome_win_2"

    $ purevn.decision_extra = True
    $ choice3_text = "Bronze"
    $ choice3_jump = "purevn_choice_outcome_win_1"

    $ purevn.decision_extra_2 = True
    $ choice4_text = "Last Place"
    $ choice4_jump = "purevn_choice_outcome_win_0"

    show screen purevn_decision4
    pause

label purevn_choice_outcome_win_3:
    $ win = 3
    return
label purevn_choice_outcome_win_2:
    $ win = 2
    return
label purevn_choice_outcome_win_1:
    $ win = 1
    return
label purevn_choice_outcome_win_0:
    $ win = 0
    return

# Exam/Final Exam Outcome
label purevn_choice_outcome_grade:
    if purevn.choice_outcome == False:
        if month != 5 and month != 9:
            $ homework_score = 40
        $ exam_score = 900
        return

    $ choice1_text = "Highest Marks (Grade: 99)"
    $ choice1_jump = "purevn_choice_outcome_grade_99"

    $ choice2_text = "Good Marks (Grade: 80)"
    $ choice2_jump = "purevn_choice_outcome_grade_80"

    $ purevn.decision_extra = True
    $ choice3_text = "Barely Passed (Grade: 65)"
    $ choice3_jump = "purevn_choice_outcome_grade_65"

    $ purevn.decision_extra_2 = True
    $ choice4_text = "Academic Probation (Grade: 50)"
    $ choice4_jump = "purevn_choice_outcome_grade_50"

    show screen purevn_decision4
    pause

label purevn_choice_outcome_grade_99:
    if month != 5 and month != 9:
        $ homework_score = 40
    $ exam_score = 900
    return
label purevn_choice_outcome_grade_80:
    if month != 5 and month != 9:
        $ homework_score = 40
        $ exam_score = 40
    else:
        $ exam_score = 80
    return
label purevn_choice_outcome_grade_65:
    if month != 5 and month != 9:
        $ homework_score = 40
        $ exam_score = 25
    else:
        $ exam_score = 65
    return
label purevn_choice_outcome_grade_50:
    if month != 5 and month != 9:
        $ homework_score = 40
        $ exam_score = 10
    else:
        $ exam_score = 50
    return

# Student Council Election Outcome
label purevn_choice_outcome_election:
    $ purevn.election_outcome = True
    hide screen election
    if purevn.choice_outcome == False:
        $ kayto_vote_pre = 560
        $ fontana_vote_pre = 1
        return

    $ choice1_text = "Rig the votes for Kayto"
    $ choice1_jump = "purevn_choice_outcome_election_landslide"

    $ choice2_text = "Vote for Kayto"
    $ choice2_jump = "purevn_choice_outcome_election_win"

    $ purevn.decision_extra = True
    $ choice3_text = "Vote for Fontana"
    $ choice3_jump = "purevn_choice_outcome_election_lose"

    #show screen decision
    show screen purevn_decision4
    pause

label purevn_choice_outcome_election_landslide:
    $ kayto_vote_pre = 560
    $ fontana_vote_pre = 1
    show screen election
    jump voteadd
label purevn_choice_outcome_election_win:
    $ kayto_vote_pre = renpy.random.randint(331,559)
    $ fontana_vote_pre = 560 - kayto_vote_pre
    show screen election
    jump voteadd
label purevn_choice_outcome_election_lose:
    # It's very well possible that not even your friends will vote for you </3
    $ kayto_vote_pre = renpy.random.randint(0,329)
    $ fontana_vote_pre = 560 - kayto_vote_pre
    show screen election
    jump voteadd