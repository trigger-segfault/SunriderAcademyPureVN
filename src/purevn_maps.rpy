screen purevn_route_map:
    modal True

    imagebutton:
        xpos 1350 ypos 950
        idle "mods/purevn/UI/go_home_base.png"
        hover "mods/purevn/UI/go_home_hover.png"
        action (Hide("purevn_route_map"),SetField(purevn,"no_route",True),Jump("purevn_choose_afterschool"))
        hover_sound "Sounds/hover1.ogg"
        activate_sound "Sounds/button1.ogg"

    if month >= 4 and affection_sola >= 50 and "m3w3_eldersday_shrine" in seen_labels and "m3w1_solaholo" in seen_labels and "m4_solastart" not in seen_labels and "m3w4_afterlab" not in seen_labels and "m4_asagamobchase" not in seen_labels and "m4_avastart" not in seen_labels:
        imagebutton:
            xpos 835 ypos 475
            idle "UI/sola_arc_base.png"
            hover "UI/sola_arc_hover.png"
            action (Hide("purevn_route_map"),Jump("m4_solastart"))
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"
            
    if month >= 4 and affection_chigara >= 50 and "m3w4_lynn_lab" in seen_labels and "m3w4_afterlab" not in seen_labels and "m4_solastart" not in seen_labels and "m4_asagamobchase" not in seen_labels and "m4_avastart" not in seen_labels:
        imagebutton:
            xpos 1300 ypos 450
            idle "UI/chigara_arc_base.png"
            hover "UI/chigara_arc_hover.png"
            action (Hide("purevn_route_map"),Jump("m3w4_afterlab"))
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"
            
    if month >= 4 and affection_asaga >= 50 and "m4_asagaafterbirthday" in seen_labels and "m4_asagamobchase" not in seen_labels and "m4_solastart" not in seen_labels and "m3w4_afterlab" not in seen_labels and "m4_avastart" not in seen_labels:
        imagebutton:
            xpos 670 ypos 650
            idle "UI/asaga_arc_base.png"
            hover "UI/asaga_arc_hover.png"
            action (Hide("purevn_route_map"),Jump("m4_asagamobchase"))
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"
            
    if month >= 4 and affection_ava >= 60 and "m3w5_incident_councilroom2" in seen_labels and "m4_asagamobchase" not in seen_labels and "m4_solastart" not in seen_labels and "m3w4_afterlab" not in seen_labels and "m4_avastart" not in seen_labels:
        imagebutton:
            xpos 1550 ypos 750
            idle "UI/ava_arc_base.png"
            hover "UI/ava_arc_hover.png"
            action (Hide("purevn_route_map"),Jump("m4_avastart"))
            hover_sound "Sounds/hover1.ogg"
            activate_sound "Sounds/button1.ogg"