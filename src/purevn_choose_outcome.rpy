init python:
    # Choose student council election outcome
    config.label_overrides['voteadd'] = 'purevn_voteadd'

# Competition Outcome
label purevn_choice_outcome_win:
    if purevn_choice_outcome == False:
        $ win = 3
        return

    $ choice1_text = "Gold"
    $ choice1_jump = "purevn_choice_outcome_win_3"

    $ choice2_text = "Silver"
    $ choice2_jump = "purevn_choice_outcome_win_2"

    $ decision_extra = True
    $ choice3_text = "Bronze"
    $ choice3_jump = "purevn_choice_outcome_win_1"

    $ decision_extra_2 = True
    $ choice4_text = "Last Place"
    $ choice4_jump = "purevn_choice_outcome_win_0"

    show screen purevn_decision4
    pause

label purevn_choice_outcome_win_3:
    $ win = 3
    call purevn_decision_wipe from _call_purevn_decision_wipe_3
    return
label purevn_choice_outcome_win_2:
    $ win = 2
    call purevn_decision_wipe from _call_purevn_decision_wipe_2
    return
label purevn_choice_outcome_win_1:
    $ win = 1
    call purevn_decision_wipe from _call_purevn_decision_wipe_1
    return
label purevn_choice_outcome_win_0:
    $ win = 0
    call purevn_decision_wipe from _call_purevn_decision_wipe_0
    return

# Exam/Final Exam Outcome
label purevn_choice_outcome_grade:
    if purevn_choice_outcome == False:
        if month != 5 and month != 9:
            $ homework_score = 40
        $ exam_score = 900
        return

    $ choice1_text = "Highest Marks (Grade: 99)"
    $ choice1_jump = "purevn_choice_outcome_grade_99"

    $ choice2_text = "Good Marks (Grade: 80)"
    $ choice2_jump = "purevn_choice_outcome_grade_80"

    $ decision_extra = True
    $ choice3_text = "Barely Passed (Grade: 65)"
    $ choice3_jump = "purevn_choice_outcome_grade_65"

    $ decision_extra_2 = True
    $ choice4_text = "Academic Probation (Grade: 50)"
    $ choice4_jump = "purevn_choice_outcome_grade_50"

    show screen purevn_decision4
    pause

label purevn_choice_outcome_grade_99:
    if month != 5 and month != 9:
        $ homework_score = 40
    $ exam_score = 900
    call purevn_decision_wipe from _call_purevn_decision_wipe_99
    return
label purevn_choice_outcome_grade_80:
    if month != 5 and month != 9:
        $ homework_score = 40
        $ exam_score = 40
    else:
        $ exam_score = 80
    call purevn_decision_wipe from _call_purevn_decision_wipe_80
    return
label purevn_choice_outcome_grade_65:
    if month != 5 and month != 9:
        $ homework_score = 40
        $ exam_score = 25
    else:
        $ exam_score = 65
    call purevn_decision_wipe from _call_purevn_decision_wipe_65
    return
label purevn_choice_outcome_grade_50:
    if month != 5 and month != 9:
        $ homework_score = 40
        $ exam_score = 10
    else:
        $ exam_score = 50
    call purevn_decision_wipe from _call_purevn_decision_wipe_50
    return

# Student Council Election Outcome
label purevn_choice_outcome_election:
    if purevn_choice_outcome == False:
        $ kayto_vote_pre = 560
        $ fontana_vote_pre = 0
        return

    $ choice1_text = "Landslide Victory"
    $ choice1_jump = "purevn_choice_outcome_election_landslide"

    $ choice2_text = "Win Election"
    $ choice2_jump = "purevn_choice_outcome_election_win"

    $ decision_extra = True
    $ choice3_text = "Lose Election"
    $ choice3_jump = "purevn_choice_outcome_election_lose"

    $ decision_extra_2 = False

    show screen purevn_decision4
    pause

label purevn_choice_outcome_election_landslide:
    $ kayto_vote_pre = 560
    $ fontana_vote_pre = 0
    call purevn_decision_wipe from _call_purevn_decision_wipe_landslide
    return
label purevn_choice_outcome_election_win:
    $ kayto_vote_pre = renpy.random.randint(331,559)
    $ fontana_vote_pre = 560 - kayto_vote_pre
    call purevn_decision_wipe from _call_purevn_decision_wipe_win
    return
label purevn_choice_outcome_election_lose:
    # It's very well possible that not even your friends will vote for you </3
    $ kayto_vote_pre = renpy.random.randint(0,329)
    $ fontana_vote_pre = 560 - kayto_vote_pre
    call purevn_decision_wipe from _call_purevn_decision_wipe_lose
    return

label purevn_voteadd:
    if purevn == True:
        if purevn_election_outcome == False:
            $ purevn_election_outcome = True
            hide screen election
            call purevn_choice_outcome_election from _call_voteadd_purevn_choice_outcome_election
            show screen election
    
    $ renpy.not_infinite_loop(10)
    
    if config.skipping is not None:
        $ kayto_vote = kayto_vote_pre
        $ fontana_vote = fontana_vote_pre
        
    if kayto_vote < kayto_vote_pre:
        $ kayto_vote += 1
            
    if fontana_vote < fontana_vote_pre:
        $ fontana_vote += 1
            
    if kayto_vote < kayto_vote_pre:
        pause 0.0001
        jump voteadd
        
    if fontana_vote < fontana_vote_pre:
        pause 0.0001
        jump voteadd
        
    pause
    
    hide screen election
    
    if kayto_vote > fontana_vote:
        jump m9_vote_win
    
    if fontana_vote > kayto_vote:
        jump m9_vote_lose
    
    return