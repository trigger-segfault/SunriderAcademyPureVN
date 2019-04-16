init 2 python:
    # Set to false to disable all custom interaction in purevn_label_callback()
    purevn_label_callback_enabled = not hasattr(store,'ac_mod') and not hasattr(store,'ac_mod_button_list')

    def purevn_label_callback(label,abnormal):
        # Make sure to call the original label callback too,
        # but only if it's not handled by the Mod List.
        if not hasattr(store,'ac_mod'):
            purevn_original_label_callback(label,abnormal)

        if purevn_label_callback_enabled == False:
            return

        if not hasattr(store,'purevn') or purevn.enabled == False:
            # Manually ask the user to start PureVN if Sunrider Academy Mod List is not present.
            if label == "start" and not hasattr(store,'ac_mod') and not hasattr(store,'ac_mod_button_list'):
                renpy.jump("purevn_start")
        else:
            # Skip class selection, we're not playing games anymore.
            if label == "class_selection":
                # We can't use call in here, so we'll jump to a label to do it for us
                renpy.jump("purevn_class_selection")

            # Override here because this label is walked into from the end of the previous label.
            # This label is repeated multiple times, so we have election_outcome as a check to make
            # sure we don't call more than once.
            if label == "voteadd" and purevn.election_outcome == False:
                renpy.jump("purevn_choice_outcome_election")

# `init 20`, so Arc Cheat appears first in the most list
init 20 python:
    # Use Mod List's label callback override system if available
    if hasattr(store,'ac_mod'):
        ac_mod.register_label_callback(purevn_label_callback)
        ac_mod.register_main_button(text="PURE VN",action=Start("purevn_start"))
        ac_mod.register_main_button(text="PURE VN: SKIP COMMON",action=(SetVariable("skipcommon",True),Start("purevn_start")))
    else:
        if hasattr(store,'ac_mod_button_list'):
            ac_mod_button_list.append(["mods/purevn/UI/mod_purevn_base.png","mods/purevn/UI/mod_purevn_hover.png","purevn_start",False,False])
            ac_mod_button_list.append(["mods/purevn/UI/mod_purevn_skipcommon_base.png","mods/purevn/UI/mod_purevn_skipcommon_hover.png","purevn_start_skipcommon",False,False])
        # Keep track of the old callback so it can still be called
        purevn_original_label_callback = config.label_callback
        config.label_callback = purevn_label_callback

init python:
    # Check the status of PureVN Mode and Choice Outcome
    def purevn_status():
        #purevn_ensure()
        if not hasattr(store,'purevn'):
            return "{0}: PureVN Mode is DISABLED".format(PureVN().version)
        elif purevn.choice_outcome == False:
            return "{0}: PureVN Mode is ENABLED, Choice Outcome is DISABLED".format(purevn.version)
        else:
            return "{0}: PureVN Mode is ENABLED, Choice Outcome is ENABLED".format(purevn.version)
            
    # Ensure PureVN and check if enabled
    def is_purevn():
        # purevn.enabled is for legacy support
        return hasattr(store,'purevn') and purevn.enabled == True

    # Ensure PureVN and check if disabled
    def is_not_purevn():
        return not hasattr(store,'purevn') or purevn.enabled == False

# This label is only for supporting the legacy Mod List that doesn't give full action support
label purevn_start_skipcommon:
    $ skipcommon = True
    jump purevn_start

label purevn_start:
    #if chap_select == True:
    #    scene bg room_morning with dissolve

    scene black:
        pause 2.0
    with dissolvemedium
    #play music "Music/caramelkoubou.ogg" fadeout 1.5
    scene bg space with dissolve
    #scene bg skywalk_day with dissolve
    #scene bg room_morning with dissolve

    $ purevn_version = PureVN().version
    tut "The PureVN Mod (v[purevn_version]) is present. Enabling PureVN Mode will automate all non-scripted activity choices.\n\nWhile normally victory is set in stone, enabling Choice Outcome will allow you to decide the outcome competitions, exams, and the election."
    $ del purevn_version

    if hasattr(store,'ac_mod') or hasattr(store,'ac_mod_button_list'):
        $ choice1_text = "Automate Outcomes"
        $ choice1_jump = "purevn_start_on"

        $ choice2_text = "Choose Outcomes Myself"
        $ choice2_jump = "purevn_start_choice_outcome"

        $ decision_extra = False

        show screen decision

    else:
        $ choice1_text = "Normal Mode"
        $ choice1_jump = "start"

        $ choice2_text = "PureVN Mode"
        $ choice2_jump = "purevn_start_on"

        $ decision_extra = True
        $ choice3_text = "PureVN Mode & Choice Outcome"
        $ choice3_jump = "purevn_start_choice_outcome"

        show screen decision

    pause

label purevn_start_off:
    # In case someone overrode the decision screen
    $ decision_extra = False
    # Disable label callback override
    $ purevn_label_callback_enabled = False

    jump start

label purevn_start_on:
    # In case someone overrode the decision screen
    $ decision_extra = False
    # Setup PureVN
    call purevn_initialize from _call_purevn_initialize_start_on

    # Disable Choice Outcome
    $ purevn.choice_outcome = False

    jump start
    
label purevn_start_choice_outcome:
    # In case someone overrode the decision screen
    $ decision_extra = False
    # Setup PureVN
    call purevn_initialize from _call_purevn_initialize_start_choice_outcome

    # Enable Choice Outcome
    $ purevn.choice_outcome = True

    jump start

label purevn_update:
    if purevn.cmp_version(purevn.current_version, '2.0.0.0') < 0:
        # Make sure label callbacks are enabled
        $ purevn_label_callback_enabled = purevn.enabled
        # Make sure our label overrides are redefined
        if purevn.enabled == True:
            call purevn_label_overrides from _call_purevn_label_overrides_update

    # Assign the the version we updated to
    $ purevn.current_version = purevn.version
    return

label purevn_older_version_warning:
    # No user, you're making a big mistake
    tut "The version of PureVN on this save is higher than the installed version of PureVN. You may encounter errors if you continue to use an older version!\n\nCurrent: v[purevn.current_version]\nInstalled: v[purevn.version]"

    # Don't warn the user again until the another version change
    $ purevn.current_version = purevn.version
    return

label purevn_class_selection:
    # No stat calculation, go full Buffsuki
    call purevn_full_stats from _call_purevn_full_stats_class_selection
    jump class_selected

label purevn_full_stats:
    python:
        # Full stats
        stat_fitness = 500
        stat_intelligence = 500
        stat_charisma = 500
        stat_stress = 0
        stat_money = 200
        stat_luck = 200
        # Handled by Choice Outcome
        #stat_grade = 100
        #stat_prestige = 500
        stat_homework = 0

        # Make sure we don't unlock Club Recruiter, Club Trainer, or Rich!!!

        stat_kendo_member = 60
        stat_kendo_readiness = 300
        stat_kendo_morale = 300

        stat_science_member = 60
        stat_science_readiness = 300
        stat_science_morale = 300

        stat_swim_member = 60
        stat_swim_readiness = 300
        stat_swim_morale = 300

        # Everyone's Kayto CANNOT be unlocked via PureVN unless the mode is disabled halfway through.
        # This is because the trigger for the achievement only comes after shopping
        # or getting intel from your sister. None of these are reachable with PureVN.

        # Above 100 so rollback on affection still won't trigger conversations
        affection_sola = 150
        affection_asaga = 150
        affection_ava = 150
        affection_chigara = 150
        affection_maray = 150

        # Force Waifu Mode
        difficulty = 0

    return

label purevn_initialize:

    # Define PureVN store variable
    $ purevn = PureVN()
    # Keep Legacy PureVN support
    $ purevn.enabled = True
    # Enable label callback override
    $ purevn_label_callback_enabled = True

    # Override all activities
    call purevn_label_overrides from _call_purevn_label_overrides_initialize

    return

label purevn_label_overrides:
    python:
        config.label_overrides['act_class'] = 'purevn_act_class'
        config.label_overrides['act_class_retry'] = 'purevn_act_class_retry'
        config.label_overrides['act_exam'] = 'purevn_act_exam'
        config.label_overrides['act_lunch'] = 'purevn_act_lunch'
        config.label_overrides['eat_courtyard'] = 'purevn_eat_courtyard'
        config.label_overrides['act_culturefest_science'] = 'purevn_act_culturefest_science'
        config.label_overrides['act_culturefest_swim'] = 'purevn_act_culturefest_swim'
        config.label_overrides['act_culturefest_kendo'] = 'purevn_act_culturefest_kendo'
        config.label_overrides['eat_classroom'] = 'purevn_eat_classroom'
        config.label_overrides['eat_cafeteria'] = 'purevn_eat_cafeteria'
        config.label_overrides['act_clubs'] = 'purevn_act_clubs'
        config.label_overrides['act_clubs2'] = 'purevn_act_clubs2'
        config.label_overrides['kendo_practice'] = 'purevn_kendo_practice'
        config.label_overrides['kendo_practice_retry'] = 'purevn_kendo_practice_retry'
        config.label_overrides['kendo_recruit'] = 'purevn_kendo_recruit'
        config.label_overrides['kendo_recruit_retry'] = 'purevn_kendo_recruit_retry'
        config.label_overrides['kendo_morale'] = 'purevn_kendo_morale'
        config.label_overrides['swim_practice'] = 'purevn_swim_practice'
        config.label_overrides['swim_practice_retry'] = 'purevn_swim_practice_retry'
        config.label_overrides['swim_recruit'] = 'purevn_swim_recruit'
        config.label_overrides['swim_recruit_retry'] = 'purevn_swim_recruit_retry'
        config.label_overrides['swim_morale'] = 'purevn_swim_morale'
        config.label_overrides['science_practice'] = 'purevn_science_practice'
        config.label_overrides['science_practice_retry'] = 'purevn_science_practice_retry'
        config.label_overrides['science_recruit'] = 'purevn_science_recruit'
        config.label_overrides['science_recruit_retry'] = 'purevn_science_recruit_retry'
        config.label_overrides['science_morale'] = 'purevn_science_morale'
        config.label_overrides['library_study'] = 'purevn_library_study'
        config.label_overrides['library_study_retry'] = 'purevn_library_study_retry'
        config.label_overrides['library_tutor'] = 'purevn_library_tutor'
        config.label_overrides['library_tutor_retry'] = 'purevn_library_tutor_retry'
        config.label_overrides['library_homework'] = 'purevn_library_homework'
        config.label_overrides['library_homework_retry'] = 'purevn_library_homework_retry'
        config.label_overrides['studentcouncil_practice'] = 'purevn_studentcouncil_practice'
        config.label_overrides['studentcouncil_practice_retry'] = 'purevn_studentcouncil_practice_retry'
        config.label_overrides['act_afterschool'] = 'purevn_act_afterschool'
        config.label_overrides['switchtocitymap'] = 'purevn_switchtocitymap'
        config.label_overrides['switchtoschoolmap'] = 'purevn_switchtoschoolmap'
        config.label_overrides['visit_museum'] = 'purevn_visit_museum'
        config.label_overrides['visit_museum_retry'] = 'purevn_visit_museum_retry'
        config.label_overrides['job_museum'] = 'purevn_job_museum'
        config.label_overrides['job_museum_retry'] = 'purevn_job_museum_retry'
        config.label_overrides['visit_arcade'] = 'purevn_visit_arcade'
        config.label_overrides['visit_arcade_retry'] = 'purevn_visit_arcade_retry'
        config.label_overrides['job_arcade'] = 'purevn_job_arcade'
        config.label_overrides['job_arcade_retry'] = 'purevn_job_arcade_retry'
        config.label_overrides['visit_park'] = 'purevn_visit_park'
        config.label_overrides['visit_park_retry'] = 'purevn_visit_park_retry'
        config.label_overrides['job_park'] = 'purevn_job_park'
        config.label_overrides['job_park_retry'] = 'purevn_job_park_retry'
        config.label_overrides['visit_shrine'] = 'purevn_visit_shrine'
        config.label_overrides['visit_shrine_retry'] = 'purevn_visit_shrine_retry'
        config.label_overrides['job_shrine'] = 'purevn_job_shrine'
        config.label_overrides['job_shrine_retry'] = 'purevn_job_shrine_retry'
        config.label_overrides['gym_exercise'] = 'purevn_gym_exercise'
        config.label_overrides['gym_exercise_retry'] = 'purevn_gym_exercise_retry'
        config.label_overrides['job_shop'] = 'purevn_job_shop'
        config.label_overrides['job_shop_retry'] = 'purevn_job_shop_retry'
        config.label_overrides['visit_shop'] = 'purevn_visit_shop'
        config.label_overrides['gohome'] = 'purevn_gohome'
        config.label_overrides['act_sleep'] = 'purevn_act_sleep'
        config.label_overrides['act_sleep_repeat'] = 'purevn_act_sleep_repeat'
        config.label_overrides['sleep_loss'] = 'purevn_sleep_loss'
        config.label_overrides['kendorounds'] = 'purevn_kendorounds'
        config.label_overrides['kendorounds_end'] = 'purevn_kendorounds_end'
        config.label_overrides['swimrounds'] = 'purevn_swimrounds'
        config.label_overrides['swimrounds_end'] = 'purevn_swimrounds_end'
        config.label_overrides['sciencerounds'] = 'purevn_sciencerounds'
        config.label_overrides['sciencerounds_end'] = 'purevn_sciencerounds_end'
        config.label_overrides['examresults_calc'] = 'purevn_examresults_calc'
        config.label_overrides['finalexamresults_calc'] = 'purevn_finalexamresults_calc'

    return