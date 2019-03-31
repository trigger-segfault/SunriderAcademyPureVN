init -10 python:
    # Declare the PureVN class and variables
    class _PureVN(object):

        ### Important Variables

        # The version of the PureVN mod when you started the game
        def __init__(self):
            self.init_version = self.version

        # The version of this PureVN mod file
        @property
        def version(self):
            return 'v0.1.0.0' # Constant

        # The version of the PureVN mod when you started the game
        #save_version = version
        
        # PureVN Mode is activated for this playthrough
        enabled = False
        # User is given a decision to determine the outcome of competitions, exams, and the election
        choice_outcome = False

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

        # Used for screen purevn_decision4 to display fourth choice
        decision_extra_2 = False

        # Check if we encounter events during an activity, used to dissolve transition
        seen_count_before = 0
        seen_count_after = 0

        # Random number generation for PureVN
        rng = 0
        rng_start = 0
        rng_end = 0

    # Define the purevn variable
    purevn = _PureVN()