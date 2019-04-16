init python:
    # Declare the PureVN class and variables
    class PureVN(object):

        ### Important Variables

        # # The version of this PureVN mod file
        # @property
        # def version(self):
        #     return '2.0.0.0' # Constant

        # The current version of the PureVN class that you loaded the save from
        def __init__(self):
            """
            @attr version: The version of PureVN installed.
            @attr current_version: The version of PureVN for this save.
            """
            self.version = '2.0.0.0'
            self.current_version = self.version
            self.label_name = None
        
        # PureVN Mode is activated for this playthrough
        # enabled is for legacy support
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

        # Compare PureVN version numbers
        def cmp_version(self,version1,version2):
            import re

            def normalize(v):
                return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
            return cmp(normalize(version1), normalize(version2))

        def update(self):
            versiondif = self.cmp_version(self.current_version,self.version)
            if versiondif < 0:
                renpy.call('purevn_update')
                #purevn_update()
            elif versiondif > 0:
                renpy.call('purevn_older_version_warning')