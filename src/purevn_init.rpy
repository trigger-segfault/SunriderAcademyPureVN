init python:
    purevn_version = 'v0.1.0.0';
    purevn = False
    purevn_setup = False
    purevn_choice_outcome = False
    purevn_asaga_get_present = False
    purevn_maray_get_present = False
    purevn_ava_get_present = False
    purevn_chigara_get_present = False
    purevn_sola_get_present = False
    purevn_sola_get_holo = False
    purevn_seen_count_before = 0
    purevn_seen_count_after = 0

    # decision4
    decision_extra_2 = False

label purevn_full_stats:
    # Full stats
    $ stat_fitness = 500
    $ stat_intelligence = 500
    $ stat_charisma = 500
    $ stat_stress = 0
    $ stat_money = 500
    $ stat_luck = 500
    $ stat_grade = 100
    #$ stat_prestige = 500
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

    # Force Waifu Mode
    $ difficulty = 0

    return