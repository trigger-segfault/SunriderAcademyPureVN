init +1:
    # Override decision screen and fix optional choice 3 jumping to choice 2 instead
    screen decision:
    
        modal True
        zorder 100
                
        imagebutton at tr_decision(0):
            xanchor 0.5
            ypos 0.35
            idle "UI/choice_hover.png"
            hover "UI/choice_base.png"
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"
            action (Hide("decision"),Jump(choice1_jump))
            
        imagebutton at tr_decision(0.2):
            xanchor 0.5
            ypos 0.5
            idle "UI/choice_hover.png"
            hover "UI/choice_base.png"
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"
            action (Hide("decision"),Jump(choice2_jump))
            
        if decision_extra == True:
            
            imagebutton at tr_decision(0.4):
                xanchor 0.5
                ypos 0.65
                idle "UI/choice_hover.png"
                hover "UI/choice_base.png"
                hover_sound "Sounds/hover1.ogg"
                activate_sound "Sounds/button1.ogg"
                action (Hide("decision"),Jump(choice3_jump)) # Fix choice2_jump being called here
                    
        text choice1_text at tr_decision(0):
            text_align 0.5 xanchor 0.5 ypos 0.39
            size 40
            outlines [ (4, "#282828", 0, 0) ]     
            
        text choice2_text at tr_decision(0.2):
            text_align 0.5 xanchor 0.5 ypos 0.54
            size 40
            outlines [ (4, "#282828", 0, 0) ]    
            
        if decision_extra == True:

            text choice3_text at tr_decision(0.4):
                text_align 0.5 xanchor 0.5 ypos 0.69
                size 40
                outlines [ (4, "#282828", 0, 0) ]    

screen purevn_decision4:
    
    modal True
    zorder 100
            
    imagebutton at tr_decision(0):
        xanchor 0.5
        ypos 0.25
        idle "UI/choice_hover.png"
        hover "UI/choice_base.png"
        hover_sound "Sounds/hover1.ogg"
        activate_sound "Sounds/button1.ogg"
        action (Hide("purevn_decision4"),Jump(choice1_jump))
        
    imagebutton at tr_decision(0.2):
        xanchor 0.5
        ypos 0.40
        idle "UI/choice_hover.png"
        hover "UI/choice_base.png"
        hover_sound "Sounds/hover1.ogg"
        activate_sound "Sounds/button1.ogg"
        action (Hide("purevn_decision4"),Jump(choice2_jump))
        
    if decision_extra == True:
        
        imagebutton at tr_decision(0.4):
            xanchor 0.5
            ypos 0.55
            idle "UI/choice_hover.png"
            hover "UI/choice_base.png"
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"
            action (Hide("purevn_decision4"),Jump(choice3_jump))
        
    if decision_extra_2 == True:
        
        imagebutton at tr_decision(0.6):
            xanchor 0.5
            ypos 0.70
            idle "UI/choice_hover.png"
            hover "UI/choice_base.png"
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"
            action (Hide("purevn_decision4"),Jump(choice4_jump))
                
    text choice1_text at tr_decision(0):
        text_align 0.5 xanchor 0.5 ypos 0.29
        size 40
        outlines [ (4, "#282828", 0, 0) ]     
        
    text choice2_text at tr_decision(0.2):
        text_align 0.5 xanchor 0.5 ypos 0.44
        size 40
        outlines [ (4, "#282828", 0, 0) ]    
        
    if decision_extra == True:

        text choice3_text at tr_decision(0.4):
            text_align 0.5 xanchor 0.5 ypos 0.59
            size 40
            outlines [ (4, "#282828", 0, 0) ]    
        
    if decision_extra_2 == True:

        text choice4_text at tr_decision(0.6):
            text_align 0.5 xanchor 0.5 ypos 0.74
            size 40
            outlines [ (4, "#282828", 0, 0) ] 
            
label purevn_decision_wipe:
    $ decision_extra = False
    $ decision_extra_2 = False
    return