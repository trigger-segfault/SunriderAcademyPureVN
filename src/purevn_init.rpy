init -1 python:
    purevn = True
    purevn_choose_outcome = False
    purevn_sola_holo = False
    purevn_seen_count_before = 0
    purevn_seen_count_after = 0


label purevn_full_stats:
    # Full stats
    $ stat_fitness = 100
    $ stat_intelligence = 500
    $ stat_charisma = 200
    $ stat_stress = 0
    $ stat_money = 200
    $ stat_luck = 100
    $ stat_grade = 100
    $ stat_prestige = 100
    $ stat_homework = 0
    
    $ stat_kendo_member = 100
    $ stat_kendo_readiness = 500
    $ stat_kendo_morale = 500
    
    $ stat_science_member = 100
    $ stat_science_readiness = 500
    $ stat_science_morale = 500
    
    $ stat_swim_member = 100
    $ stat_swim_readiness = 500
    $ stat_swim_morale = 500

    # Above 100 so rollback on affection doesn't trigger conversations
    $ affection_sola = 500
    $ affection_asaga = 500
    $ affection_ava = 500
    $ affection_chigara = 500
    $ affection_maray = 500

