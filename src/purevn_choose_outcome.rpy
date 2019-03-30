label purevn_choose_outcome_win:
    if purevn_choose_outcome == False:
        $ win = 3
        return

    $ choice1_text = "Gold"
    $ choice1_jump = "purevn_choose_outcome_win_3"

    $ choice2_text = "Silver"
    $ choice2_jump = "purevn_choose_outcome_win_2"

    $ decision_extra = True
    $ choice3_text = "Bronze"
    $ choice3_jump = "purevn_choose_outcome_win_1"

    $ decision_extra_2 = True
    $ choice4_text = "Last Place"
    $ choice4_jump = "purevn_choose_outcome_win_0"

    show screen purevn_decision4
    pause

label purevn_choose_outcome_win_3:
    $ win = 3
    call purevn_decision_wipe
    return
label purevn_choose_outcome_win_2:
    $ win = 2
    call purevn_decision_wipe
    return
label purevn_choose_outcome_win_1:
    $ win = 1
    call purevn_decision_wipe
    return
label purevn_choose_outcome_win_0:
    $ win = 0
    call purevn_decision_wipe
    return
