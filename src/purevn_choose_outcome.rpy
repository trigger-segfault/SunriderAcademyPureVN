# Competition Outcome
label purevn_choice_outcome_win:
    if purevn.choice_outcome == False:
        jump purevn_choice_outcome_win_3

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
        jump purevn_choice_outcome_grade_90

    # Don't allow unlocking of Genius achievement
    $ choice1_text = "High Marks"
    $ choice1_jump = "purevn_choice_outcome_grade_99"

    $ choice2_text = "Good Marks"
    $ choice2_jump = "purevn_choice_outcome_grade_80"

    $ purevn.decision_extra = True
    $ choice3_text = "Barely Passed"
    $ choice3_jump = "purevn_choice_outcome_grade_65"

    $ purevn.decision_extra_2 = True
    $ choice4_text = "Academic Warning"
    $ choice4_jump = "purevn_choice_outcome_grade_50"

    show screen purevn_decision4
    pause

label purevn_choice_outcome_grade_99:
    # This label's name is for legacy support, back when achievements weren't on the radar
    if month != 5 and month != 9:
        $ homework_score = 40
        $ exam_score = 50
    else:
        $ exam_score = 90
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
    if purevn.choice_outcome == False:
        jump purevn_choice_outcome_election_win
        return
    
    # Only hide the screen if we need to make a choice
    hide screen election

    $ choice1_text = "Rig the votes for Kayto"
    $ choice1_jump = "purevn_choice_outcome_election_landslide"

    $ choice2_text = "Vote for Kayto"
    $ choice2_jump = "purevn_choice_outcome_election_win"

    $ purevn.decision_extra = True
    $ choice3_text = "Vote for Fontana"
    $ choice3_jump = "purevn_choice_outcome_election_lose"

    show screen purevn_decision4
    pause

label purevn_choice_outcome_election_landslide:
    # Don't allow unlocking of Landslide Victory achievement
    # Yes, this label is named landslide, but it's staying that way for legacy support
    $ kayto_vote_pre = 559
    $ fontana_vote_pre = 1
    show screen election
    jump voteadd
label purevn_choice_outcome_election_win:
    $ kayto_vote_pre = renpy.random.randint(331,500)
    $ fontana_vote_pre = 560 - kayto_vote_pre
    show screen election
    jump voteadd
label purevn_choice_outcome_election_lose:
    # It's very well possible that not even your friends will vote for you </3
    # For the sake of immersion I guess I'll fix that :(
    $ kayto_vote_pre = renpy.random.randint(4,329)
    $ fontana_vote_pre = 560 - kayto_vote_pre
    show screen election
    jump voteadd