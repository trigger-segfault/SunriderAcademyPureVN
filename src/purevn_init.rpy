init python:
    # Declare the PureVN class and variables
    class PureVN(object):

        ### Important Variables

        # The version of this PureVN mod file
        @property
        def version(self):
            return 'v0.3.0.0' # Constant

        # The current version of the PureVN class that you loaded the save from
        def __init__(self):
            self.current_version = self.version
        
        # PureVN Mode is activated for this playthrough
        enabled = False
        # User is given a decision to determine the outcome of competitions, exams, and the election
        choice_outcome = False

        # Enable special commands that skip story after sleep to test certain scenes, will be disabled after each choice
        developer = False

        ### Internal Variables

        # PureVN has asked for user setup input
        setup = False

        # The user has declined to choose a heroine route
        no_route = False

        # Keep track of if we asked the user to buy a present so we don't keep nagging them
        asaga_get_present = False
        maray_get_present = False
        ava_get_present = False
        chigara_get_present = False
        sola_get_present = False
        sola_get_holo = False

        # We have rigged the election during label purevn_voteadd and should not rig it again
        election_outcome = False

        # Check if we encounter events during an activity, used to horizontalwipe transition
        seen_count_before = 0
        seen_count_after = 0

        # Used for screen purevn_decision4 to display third choice
        decision_extra = False

        # Used for screen purevn_decision4 to display fourth choice
        decision_extra_2 = False

        # Random number generation for PureVN
        rng = 0
        rng_start = 0
        rng_end = 0

init python:
    # Regex for version comparison
    import re

    # Default initialization
    purevn = None

    ### PureVN Update Functions
        
    def purevn_update():
        # No new versions to update from yet

        # Assign the the version we updated to
        purevn.current_version = purevn.version
    
    ### PureVN Helper Functions

    # Guarantee that PureVN exists and is up-to-date
    def purevn_ensure():
        global purevn
        try:
            #if purevn is bool:
            #    purevn_update_old()
            if type(purevn) is PureVN:
                versiondif = purevn_cmp_version(purevn.current_version, purevn.version)
                if versiondif < 0:
                    purevn_update()
                elif versiondif > 0:
                    renpy.call('purevn_older_version_warning')
            purevn.version
            return purevn
        except NameError:
            purevn = PureVN()
            return purevn
        except AttributeError:
            purevn = PureVN()
            return purevn

    # Ensure PureVN and check if enabled
    def is_purevn():
        return purevn_ensure().enabled

    # Ensure PureVN and check if disabled
    def is_not_purevn():
        return not purevn_ensure().enabled

    # Compare PureVN version numbers
    def purevn_cmp_version(version1, version2):
        version1 = version1[1:]
        version2 = version2[1:]
        def normalize(v):
            return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
        return cmp(normalize(version1), normalize(version2))

    ### PureVN Console Commands

    # Disable PureVN Mode and Choice Outcome
    def purevn_disable():
        purevn_ensure()
        purevn.enabled = False
        purevn.choice_outcome = False
        return "PureVN and Choice Outcome has been DISABLED"

    # Enable PureVN Mode and disable Choice Outcome
    def purevn_enable():
        purevn_ensure()
        purevn.enabled = True
        purevn.choice_outcome = False
        return "PureVN has been ENABLED and Choice Outcome has been DISABLED"

    # Enable PureVN Mode and enable Choice Outcome
    def purevn_choice_outcome_enable():
        purevn_ensure()
        purevn.enabled = True
        purevn.choice_outcome = True
        return "PureVN and Choice Outcome has been ENABLED"

    # Check the status of PureVN Mode and Choice Outcome
    def purevn_status():
        purevn_ensure()
        if purevn.enabled == False:
            return "{0}: PureVN Mode is DISABLED".format(purevn.version)
        elif purevn.choice_outcome == False:
            return "{0}: PureVN Mode is ENABLED, Choice Outcome is DISABLED".format(purevn.version)
        else:
            return "{0}: PureVN Mode is ENABLED, Choice Outcome is ENABLED".format(purevn.version)

    #def purevn_help():
    #    purevn_ensure()
    #    return  ("Sunrider Academy PureVN Mod {0}:\n\n".format(purevn.version) +
    #            "COMMANDS:\n" +
    #            " > purevn_help() # Display this help message\n" +
    #            " > purevn_disable() # Disable PureVN Mode and disable Choice Outcome\n" +
    #            " > purevn_enable() # Enable PureVN Mode and disable Choice Outcome\n" +
    #            " > purevn_choice_outcome_enable() # Enable PureVN Mode and enable Choice Outcome\n" +
    #            " > purevn_status() # Display the version and enabled status of PureVN Mode and Choice Outcome\n")

label purevn_older_version_warning:
    # No user, you're making a big mistake
    tut "The version of PureVN on this save is higher than the installed version of PureVN. You may encounter errors if you continue to use an older version!\n\nCurrent: [purevn.current_version]\nInstalled: [purevn.version]"

    # Don't warn the user again until the another version change
    $ purevn.current_version = purevn.version
    return

label purevn_full_stats:
    # Full stats
    $ stat_fitness = 500
    $ stat_intelligence = 500
    $ stat_charisma = 500
    $ stat_stress = 0
    $ stat_money = 500
    $ stat_luck = 500
    # Handled by Choice Outcome
    #$ stat_grade = 100
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

    # Above 100 so rollback on affection still won't trigger conversations
    $ affection_sola = 500
    $ affection_asaga = 500
    $ affection_ava = 500
    $ affection_chigara = 500
    $ affection_maray = 500

    # Force Waifu Mode
    $ difficulty = 0

    return