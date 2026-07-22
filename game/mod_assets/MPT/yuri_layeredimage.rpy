init python:

    # Base folders for the MPT. If you need to change the path for
    # whatever reason, just change the ones below!
    base_path = "mod_assets/MPT/yuri/"
    extra_path = base_path + "extra_assets/"
    anim_path = extra_path + "anim/"

image y_stab1:
    anim_path + "yuri_turned_stab1.png"
image y_stab2_a:
    Composite((960, 960), (0, 0), anim_path + "yuri_turned_stab2.png", (450, 630), "blood")
image y_stab3:
    anim_path + "yuri_turned_stab3.png"
image y_stab4_a:
    Composite((960, 960), (0, 0), anim_path + "yuri_turned_stab4.png", (450, 630), "blood")
image y_stab5:
    anim_path + "yuri_turned_stab5.png"
image y_stab6_a:
    Composite((960, 960), (0, 0), anim_path + "yuri_turned_stab6.png", (480, 462), "blood")

image y_oneeye:
    Composite((960, 960), (0, 0), anim_path + "yuri_turned_eyes_oneeye1.png", (0, 0), "y_oneeye1")

image y_oneeye_long:
    Composite((960, 960), (0, 0), anim_path + "yuri_turned_eyes_oneeye1.png", (0, 0), "y_oneeye2")

image y_oneeye1:
    anim_path + "yuri_turned_eyes_oneeye2.png"
    subpixel True
    3.0
    linear 60 xoffset -50 yoffset 20

image y_oneeye2:
    anim_path + "yuri_turned_eyes_oneeye2.png"
    subpixel True
    3.0
    linear 300 xoffset -250 yoffset 100

image yuri_stab_anim:
    "y_stab1"
    0.6
    "y_stab2_a"
    1.0
    "y_stab3"
    0.8
    "y_stab4_a"
    1.2
    "y_stab5"
    0.8
    "y_stab6_a"

image yuri_stab_fast:
    "y_stab3"
    0.15
    "y_stab2_a"
    0.15
    repeat

image y_glitch_overlay:
    anim_path + "yuri_turned_glitch_za.png"
    0.15
    anim_path + "yuri_turned_glitch_zb.png"
    0.15
    anim_path + "yuri_turned_glitch_zc.png"
    0.15
    anim_path + "yuri_turned_glitch_zd.png"
    0.15
    repeat

image y_glitch2_overlay:
    anim_path + "yuri_turned_glitch_0a.png"
    0.1
    anim_path + "yuri_turned_glitch_0b.png"
    0.5
    anim_path + "yuri_turned_glitch_0a.png"
    0.3
    anim_path + "yuri_turned_glitch_0b.png"
    0.3
    alpha 0.0

image y_glitch2_overlay_loop:
    anim_path + "yuri_turned_glitch_0a.png"
    0.3
    anim_path + "yuri_turned_glitch_0b.png"
    0.5
    anim_path + "yuri_turned_glitch_0a.png"
    0.3
    anim_path + "yuri_turned_glitch_0b.png"
    0.5
    repeat

layeredimage yuri turned:
    
    # This makes the sprite one single texture, instead of multiple textures on top of each other.
    # This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution=False)
    
    always base_path + "yuri_turned_facebase.png"
    
    # Attributes for autofocus logic.
    group af_logic multiple:
        attribute afm null 
        # This attribute controls whether automatic control of the mouths takes place or not. 
        # Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null 
        # This attribute controls whether automatic control of zorder takes place or not.
        # Add this tag to a character to enable automatic zorder control, remove it to disable it.
    
    group outfit: 
    # These attributes are here only to determine which set of "body" sprites to use later. 
    # "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: # Mood determines what the defaults images are for the following attributes:
        # "oe", "ce", "om", "cm", "brow".
        # By changing what the "mood" attribute is, you can easily switch between premade sets 
        # of expressions that work well together, speeding up your workflow.
        # Additionally, you can add in any new ones as you like.
        attribute neut default null # neutral
        attribute angr null # angry
        attribute anno null # annoyed
        attribute cry null  # crying
        attribute curi null # curious
        attribute dist null # distant
        attribute doub null # doubtful
        attribute flus null # flustered
        attribute happ null # happy
        attribute laug null # laughing
        attribute lsur null # surprised (lightly)
        attribute nerv null # nervous
        attribute pani null # panicked
        attribute pout null # pouting
        attribute sad null  # sad
        attribute sedu null # seductive
        attribute shoc null # shocked
        attribute vang null # VERY angry
        attribute vsur null # surprised (very)
        attribute worr null # worried
        attribute yand null # yandere
        # attribute xxxx null # xxxx # Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: # Have to separate these out, they can't share moods.
        attribute nobl default null # Normal Blush.
        attribute awkw null # Awkward.
        attribute blus null # Blushing.
        attribute blaw null # Blushing AND Awkward.
        attribute empty null # No blush at all, just Empty.
    
    
    
    group left:
        # Uniform
        attribute ldown default if_any(["uniform"]):
            base_path + "yuri_turned_uniform_left_down.png"
        attribute lup if_any(["rup","rcut","rscar","rclean","rmix","rup_st"]) if_all(["uniform"]):
            base_path + "yuri_turned_uniform_left_up.png"

        ### LayeredRedux's Stab Animation Stuff
        #--------------------------------------------------------------------------------------
        attribute stab1 if_any(["uniform"]):
            "y_stab1"
        attribute stab2_a if_any(["uniform"]): # Blood Particles
            "y_stab2_a"
        attribute stab2 if_any(["uniform"]):
            anim_path + "yuri_turned_stab2.png"
        attribute stab3 if_any(["uniform"]):
            "y_stab3"
        attribute stab4_a if_any(["uniform"]): # Blood Particles
            "y_stab4_a"
        attribute stab4 if_any(["uniform"]):
            anim_path + "yuri_turned_stab4.png"
        attribute stab5 if_any(["uniform"]):
            "y_stab5"
        attribute stab6_a if_any(["uniform"]): # Blood Particles
            "y_stab6_a"
        attribute stab6 if_any(["uniform"]):
            anim_path + "yuri_turned_stab6.png"
        attribute stab if_any(["uniform"]):
            "yuri_stab_anim"
        attribute stab_f if_any(["uniform"]):
            "yuri_stab_fast"
        #--------------------------------------------------------------------------------------
        
        # Casual
        attribute ldown default if_any(["casual"]):
            base_path + "yuri_turned_casual_left_down.png"
        attribute lup if_any(["rup","rcut","rscar","rclean","rmix"]) if_all(["casual"]):
            base_path + "yuri_turned_casual_left_up.png"
    
    
    
    group right:
        attribute rdown default if_any(["uniform"]):
            base_path + "yuri_turned_uniform_right_down.png"
        attribute rup if_any(["uniform"]):
            base_path + "yuri_turned_uniform_right_up.png"
        attribute rcut if_any(["uniform"]):
            base_path + "yuri_turned_uniform_right_cut.png"

        ### LayeredRedux's Stab Animation Stuff
        #--------------------------------------------------------------------------------------
        attribute stab1 if_any(["uniform"]):
            null
        attribute stab2_a if_any(["uniform"]):
            null
        attribute stab2 if_any(["uniform"]):
            null
        attribute stab3 if_any(["uniform"]):
            null
        attribute stab4_a if_any(["uniform"]):
            null
        attribute stab4 if_any(["uniform"]):
            null
        attribute stab5 if_any(["uniform"]):
            null
        attribute stab6_a if_any(["uniform"]):
            null
        attribute stab6 if_any(["uniform"]):
            null
        attribute stab if_any(["uniform"]):
            null
        attribute stab_f if_any(["uniform"]):
            null
        #--------------------------------------------------------------------------------------

        attribute rdown default if_any(["casual"]):
            base_path + "yuri_turned_casual_right_down.png"
        attribute rup if_any(["casual"]):
            base_path + "yuri_turned_casual_right_up.png"

        ### LayeredRedux's Extra Bodies
        #--------------------------------------------------------------------------------------

        attribute rscar if_any(["uniform"]):
            extra_path + "yuri_turned_uniform_right_scars.png"
        
        attribute rclean if_any(["uniform"]):
            extra_path + "yuri_turned_uniform_right_uncut.png"

        attribute rmix if_any(["uniform"]):
            extra_path + "yuri_turned_uniform_right_midcut.png"

        attribute rdown_st if_any(["uniform"]):
            extra_path + "yuri_turned_uniform_right_down_stab.png"

        attribute rup_st if_any(["uniform"]):
            extra_path + "yuri_turned_uniform_right_up_stab.png"

        attribute rcut if_any(["casual"]):
            extra_path + "yuri_turned_casual_right_cut.png"

        attribute rscar if_any(["casual"]):
            extra_path + "yuri_turned_casual_right_scars.png"
        
        attribute rclean if_any(["casual"]):
            extra_path + "yuri_turned_casual_right_uncut.png"

        attribute rmix if_any(["casual"]):
            extra_path + "yuri_turned_casual_right_midcut.png"

        #--------------------------------------------------------------------------------------
    
    
    
    group left:
    # This is here a second time to deal with if the right half of Yuri is shown only down; 
    # the left half of her with her arm up has to render over the right half.

        # Uniform
        attribute lup if_not(["rup","rcut","rscar","rclean","rmix","rup_st"]) if_all(["uniform"]):
            base_path + "yuri_turned_uniform_left_up.png"
        
        # Casual
        attribute lup if_not(["rup","rcut","rscar","rclean","rmix"]) if_all(["casual"]):
            base_path + "yuri_turned_casual_left_up.png"
    
    
    
    group nose:
        
        # Default nose/blush.
        attribute nose default if_any(["nobl"]): # Default nose
            base_path + "yuri_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]): # Default nose when "awkward"
            base_path + "yuri_turned_nose_n2.png"
        attribute nose default if_any(["blus"]): # Default nose when "blushing"
            base_path + "yuri_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]): # Default nose when "blushing" and "awkward"
            base_path + "yuri_turned_nose_n4.png"
        attribute nose default if_any(["empty"]): # Default nose when "empty", so basically just nothing.
            null
        
        
        ### All noses - truncated tags:
        attribute n1:
            base_path + "yuri_turned_nose_n1.png"
        attribute n2:
            base_path + "yuri_turned_nose_n2.png"
        attribute n3:
            base_path + "yuri_turned_nose_n3.png"
        attribute n4:
            base_path + "yuri_turned_nose_n4.png"
    
    
    
    group mouth:
        
        # Default Closed Mouths:
        attribute cm default if_any(["happ","laug"]):
            base_path + "yuri_turned_mouth_ma.png"
        attribute cm default if_any(["neut","lsur","worr"]):
            base_path + "yuri_turned_mouth_md.png"# 
        attribute cm default if_any(["sedu"]):
            base_path + "yuri_turned_mouth_me.png"
        attribute cm default if_any(["dist","pout","curi"]):
            base_path + "yuri_turned_mouth_mf.png"
        attribute cm default if_any(["shoc"]):
            base_path + "yuri_turned_mouth_mg.png"
        attribute cm default if_any(["anno","vsur","sad","angr","cry","doub"]):
            base_path + "yuri_turned_mouth_mj.png"
        attribute cm default if_any(["nerv","flus"]):
            base_path + "yuri_turned_mouth_mk.png"
        attribute cm default if_any(["vang","pani"]):
            base_path + "yuri_turned_mouth_mm.png"
        attribute cm default if_any(["yand"]):
            base_path + "yuri_turned_mouth_mo.png"
        
        # Open Mouths:
        attribute om if_any(["happ", "laug"]):
            base_path + "yuri_turned_mouth_mb.png"
        attribute om if_any(["nerv","yand"]):
            base_path + "yuri_turned_mouth_mc.png"
        attribute om if_any(["worr","pout"]):
            base_path + "yuri_turned_mouth_me.png"
        attribute om if_any(["sedu"]):
            base_path + "yuri_turned_mouth_mf.png"
        attribute om if_any(["dist","lsur","angr","cry"]):
            base_path + "yuri_turned_mouth_mg.png"
        attribute om if_any(["neut","anno","vsur","curi"]):
            base_path + "yuri_turned_mouth_mh.png"
        attribute om if_any(["flus","doub"]):
            base_path + "yuri_turned_mouth_mi.png"
        attribute om if_any(["sad"]):
            base_path + "yuri_turned_mouth_mk.png"
        attribute om if_any(["vang","shoc","pani"]):
            base_path + "yuri_turned_mouth_ml.png"
        
        
        ### All mouths - truncated tags:
        attribute ma:
            base_path + "yuri_turned_mouth_ma.png"
        attribute mb:
            base_path + "yuri_turned_mouth_mb.png"
        attribute mc:
            base_path + "yuri_turned_mouth_mc.png"
        attribute md:
            base_path + "yuri_turned_mouth_md.png"
        attribute me:
            base_path + "yuri_turned_mouth_me.png"
        attribute mf:
            base_path + "yuri_turned_mouth_mf.png"
        attribute mg:
            base_path + "yuri_turned_mouth_mg.png"
        attribute mh:
            base_path + "yuri_turned_mouth_mh.png"
        attribute mi:
            base_path + "yuri_turned_mouth_mi.png"
        attribute mj:
            base_path + "yuri_turned_mouth_mj.png"
        attribute mk:
            base_path + "yuri_turned_mouth_mk.png"
        attribute ml:
            base_path + "yuri_turned_mouth_ml.png"
        attribute mm:
            base_path + "yuri_turned_mouth_mm.png"
        attribute mn:
            base_path + "yuri_turned_mouth_mn.png"
        attribute mo: # Originally 'mlc' in the original MPT.
            base_path + "yuri_turned_mouth_mo.png"
        attribute mp:
            base_path + "yuri_turned_mouth_mp.png"
        attribute mq:
            base_path + "yuri_turned_mouth_mq.png"
        attribute mr:
            base_path + "yuri_turned_mouth_mr.png"

        ### There are some Legacy mouths that were forgotten in MPT for some reason.
        #--------------------------------------------------------------------------------------
        attribute mla:
            extra_path + "yuri_turned_mouth_mla.png"
        attribute mlb:
            extra_path + "yuri_turned_mouth_mlb.png"
        attribute mlc: # This one was named 'mld' in the original MPT, keep that in mind.
            extra_path + "yuri_turned_mouth_mlc.png"
        #--------------------------------------------------------------------------------------

        ### LayeredRedux's Extra Mouths.
        #--------------------------------------------------------------------------------------
        attribute ms:
            extra_path + "yuri_turned_mouth_ms.png"
        attribute mt:
            extra_path + "yuri_turned_mouth_mt.png"
        attribute mu:
            extra_path + "yuri_turned_mouth_mu.png"
        attribute mv:
            extra_path + "yuri_turned_mouth_mv.png"
        attribute mw:
            extra_path + "yuri_turned_mouth_mw.png"
        #--------------------------------------------------------------------------------------
    
    
    group eyes if_not(["s_scream", "s_dark", "s_yandere"]):
        
        # Default Opened eyes:
        attribute oe default if_any(["neut","sedu"]):
            base_path + "yuri_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr"]):
            base_path + "yuri_turned_eyes_e1b.png"
        attribute oe default if_any(["happ","angr","pout","curi"]):
            base_path + "yuri_turned_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            base_path + "yuri_turned_eyes_e1h.png"
        attribute oe default if_any(["lsur","vang"]):
            base_path + "yuri_turned_eyes_e2a.png"
        attribute oe default if_any(["anno","flus","laug","sad"]):
            base_path + "yuri_turned_eyes_e2b.png"
        attribute oe default if_any(["nerv","doub"]):
            base_path + "yuri_turned_eyes_e2c.png"
        attribute oe default if_any(["shoc","pani","vsur"]):
            base_path + "yuri_turned_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            base_path + "yuri_turned_eyes_e3a.png"
        
        # Default Closed eyes:
        attribute ce if_any(["dist","anno","vang","flus","lsur","shoc","vsur","worr","sad","angr","nerv","curi","doub"]):
            base_path + "yuri_turned_eyes_e4a.png"
        attribute ce if_any(["neut","happ","yand","pani","laug","sedu","pout"]):
            base_path + "yuri_turned_eyes_e4b.png"
        attribute ce if_any(["cry"]):
            base_path + "yuri_turned_eyes_e4e.png"
        
        
        ### All eyes - truncated tags:
        attribute e1a:
            base_path + "yuri_turned_eyes_e1a.png"
        attribute e1b:
            base_path + "yuri_turned_eyes_e1b.png"
        attribute e1c:
            base_path + "yuri_turned_eyes_e1c.png"
        attribute e1d:
            base_path + "yuri_turned_eyes_e1d.png"
        attribute e1e:
            base_path + "yuri_turned_eyes_e1e.png"
        attribute e1f:
            base_path + "yuri_turned_eyes_e1f.png"
        attribute e1g:
            base_path + "yuri_turned_eyes_e1g.png"
        attribute e1h:
            base_path + "yuri_turned_eyes_e1h.png"
        attribute e2a:
            base_path + "yuri_turned_eyes_e2a.png"
        attribute e2b:
            base_path + "yuri_turned_eyes_e2b.png"
        attribute e2c:
            base_path + "yuri_turned_eyes_e2c.png"
        attribute e2d:
            base_path + "yuri_turned_eyes_e2d.png"
        attribute e3a:
            base_path + "yuri_turned_eyes_e3a.png"
        attribute e3b:
            base_path + "yuri_turned_eyes_e3b.png"
        attribute e4a:
            base_path + "yuri_turned_eyes_e4a.png"
        attribute e4b:
            base_path + "yuri_turned_eyes_e4b.png"
        attribute e4c:
            base_path + "yuri_turned_eyes_e4c.png"
        attribute e4d:
            base_path + "yuri_turned_eyes_e4d.png"
        attribute e4e:
            base_path + "yuri_turned_eyes_e4e.png"
        attribute e0a:
            base_path + "yuri_turned_eyes_e0a.png"
        attribute e0b:
            base_path + "yuri_turned_eyes_e0b.png"
        attribute ela:
            base_path + "yuri_turned_eyes_ela.png"
        attribute elb:
            base_path + "yuri_turned_eyes_elb.png"

        ### LayeredRedux's Extra Eyes
        #--------------------------------------------------------------------------------------
        attribute e2e:
            extra_path + "yuri_turned_eyes_e2e.png"
        attribute e3c:
            extra_path + "yuri_turned_eyes_e3c.png"
        attribute e4f:
            extra_path + "yuri_turned_eyes_e4f.png"
        attribute e4g:
            extra_path + "yuri_turned_eyes_e4g.png"
        attribute e4h:
            extra_path + "yuri_turned_eyes_e4h.png"
        attribute e0c:
            extra_path + "yuri_turned_eyes_e0c.png"
        attribute e0d:
            extra_path + "yuri_turned_eyes_e0d.png"
        attribute e0e:
            extra_path + "yuri_turned_eyes_e0e.png"
        attribute e0f:
            extra_path + "yuri_turned_eyes_e0f.png"
        attribute e0g:
            extra_path + "yuri_turned_eyes_e0g.png"
        attribute e0h:
            extra_path + "yuri_turned_eyes_e0h.png"
        attribute esilly1:
            extra_path + "yuri_turned_eyes_silly1.png"
        attribute esilly2:
            extra_path + "yuri_turned_eyes_silly2.png"
        attribute estar1a:
            extra_path + "yuri_turned_eyes_star1a.png"
        attribute estar1b:
            extra_path + "yuri_turned_eyes_star1b.png"
        attribute estar2a:
            extra_path + "yuri_turned_eyes_star2a.png"
        attribute estar2b:
            extra_path + "yuri_turned_eyes_star2b.png"
        attribute estar3a:
            extra_path + "yuri_turned_eyes_star3a.png"
        attribute estar3b:
            extra_path + "yuri_turned_eyes_star3a.png"

        attribute efly:
            "y_oneeye"

        attribute efly_long:
            "y_oneeye_long"
        #--------------------------------------------------------------------------------------
    
    
    group eyebrows if_not(["s_scream", "s_dark", "s_yandere"]):
        
        # Default Eyebrows:
        attribute brow default if_any(["happ","neut"]):
            base_path + "yuri_turned_eyebrows_b2a.png"
        attribute brow default if_any(["flus","lsur","laug"]):
            base_path + "yuri_turned_eyebrows_b1b.png"
        attribute brow default if_any(["dist","sedu"]):
            base_path + "yuri_turned_eyebrows_b3c.png"
        attribute brow default if_any(["anno", "pout"]):
            base_path + "yuri_turned_eyebrows_b1d.png"
        attribute brow default if_any(["vang","angr"]):
            base_path + "yuri_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curi","doub"]):
            base_path + "yuri_turned_eyebrows_b1f.png"
        attribute brow default if_any(["worr","sad","nerv","cry"]):
            base_path + "yuri_turned_eyebrows_b2b.png"
        attribute brow default if_any(["yand","shoc","vsur","pani"]):
            base_path + "yuri_turned_eyebrows_b2c.png"
        
        
        ### All eyebrows - truncated tags:
        # This first set of definitions has only the logic to exclude certain eyebrows 
        # for particular large eye Yuri expressions.
        attribute b1a:
            base_path + "yuri_turned_eyebrows_b1a.png"
        attribute b1b:
            base_path + "yuri_turned_eyebrows_b1b.png"
        attribute b1c if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            base_path + "yuri_turned_eyebrows_b1c.png"
        attribute b1d if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            base_path + "yuri_turned_eyebrows_b1d.png"
        attribute b1e if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            base_path + "yuri_turned_eyebrows_b1e.png"
        attribute b1f:
            base_path + "yuri_turned_eyebrows_b1f.png"
        attribute b2a:
            base_path + "yuri_turned_eyebrows_b2a.png"
        attribute b2b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            base_path + "yuri_turned_eyebrows_b2b.png"
        attribute b2c:
            base_path + "yuri_turned_eyebrows_b2c.png"
        attribute b3a if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            base_path + "yuri_turned_eyebrows_b3a.png"
        attribute b3b if_not(["e0b","e2d","e3a","e3b","shoc","pani","vsur","yand"]):
            base_path + "yuri_turned_eyebrows_b3b.png"
        attribute b3c:
            base_path + "yuri_turned_eyebrows_b3c.png"
        
        
        # This second set allows those above eyebrows to render on 
        # problematic moods... so long as their eyes are closed.
        attribute b1c if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            base_path + "yuri_turned_eyebrows_b1c.png"
        attribute b1d if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            base_path + "yuri_turned_eyebrows_b1d.png"
        attribute b1e if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            base_path + "yuri_turned_eyebrows_b1e.png"
        attribute b2b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            base_path + "yuri_turned_eyebrows_b2b.png"
        attribute b3a if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            base_path + "yuri_turned_eyebrows_b3a.png"
        attribute b3b if_any(["shoc","pani","vsur","yand"]) if_all(["ce"]):
            base_path + "yuri_turned_eyebrows_b3b.png"
    
    
    
    # This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
        
        attribute s_scream:
            base_path + "yuri_turned_special_scream.png"

        #--------------------------------------------------------------------------------------
        attribute s_dark:
            extra_path + "yuri_turned_special_dark.png"
        attribute s_yandere:
            extra_path + "yuri_turned_special_yandere.png"
        #--------------------------------------------------------------------------------------


    ### These next few groups were added specifically for LayeredRedux.
    #--------------------------------------------------------------------------------------
    group decor:
        attribute blood_mark:
            extra_path + "yuri_turned_bloodmark.png"

    group sweat:

        attribute sweat1:
            extra_path + "yuri_turned_sweat.png"
        attribute sweat2:
            extra_path + "yuri_turned_sweat2.png"

    group eyebags:

        attribute eyebags:
            extra_path + "yuri_turned_eyebags.png"

    group tears:

        attribute tears1:
            extra_path + "yuri_turned_tears.png"
        attribute tears2:
            extra_path + "yuri_turned_sobbing.png"

    group other:
        attribute o_glitch:
            "y_glitch_overlay"

        attribute o_glitch2:
            "y_glitch2_overlay"
        
        attribute o_glitch2_loop:
            "y_glitch2_overlay_loop"
    #--------------------------------------------------------------------------------------


layeredimage yuri shy:
    
    # This makes the sprite one single texture, instead of multiple textures on top of each other.
    # This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution=False)
    
    always base_path + "yuri_shy_facebase.png"
    
    # Attributes for autofocus logic.
    group af_logic multiple:
        attribute afm null # This attribute controls whether automatic control of the mouths takes place or not.  Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null # This attribute controls whether automatic control of zorder takes place or not.  Add this tag to a character to enable automatic zorder control, remove it to disable it.
    
    group outfit:
    
        attribute uniform default:
            base_path + "yuri_shy_uniform_bodybase.png"
        attribute casual:
            base_path + "yuri_shy_casual_bodybase.png"
    
    
    
    group mood: # Mood determines what the defaults images are for the following attributes:
        # "oe", "ce", "om", "cm", "brow".
        # By changing what the "mood" attribute is, you can easily switch between premade sets 
        # of expressions that work well together, speeding up your workflow.
        # Additionally, you can add in any new ones as you like.
        attribute neut default null # neutral
        attribute angr null # angry
        attribute happ null # happy
        attribute sad null  # sad
    
    
    
    group blush:
        attribute nobl default null # No blush.
        attribute awkw null # Awkward.
        attribute blus null # Blushing.
        attribute blaw null # Blushing AND Awkward.
        attribute bful null # Full Face Blush.  Currently only works on the side face.
        attribute empty null
    
    
    group nose:
        
        # Default nose/blush.
        attribute nose default if_any(["nobl"]): # Default nose
            base_path + "yuri_shy_nose_n1.png"
        attribute nose default if_any(["awkw"]): # Default nose when "awkward"
            base_path + "yuri_shy_nose_n2.png"
        attribute nose default if_any(["blus"]): # Default nose when "blushing"
            base_path + "yuri_shy_nose_n3.png"
        attribute nose default if_any(["blaw"]): # Default nose when "blushing" and "awkward"
            base_path + "yuri_shy_nose_n4.png"
        attribute nose default if_any(["bful"]): # Full face blush
            base_path + "yuri_shy_nose_n5.png"
        attribute nose default if_any(["empty"]):
            null
        
        
        ### All noses - truncated tags:
        attribute n1:
            base_path + "yuri_shy_nose_n1.png"
        attribute n2:
            base_path + "yuri_shy_nose_n2.png"
        attribute n3:
            base_path + "yuri_shy_nose_n3.png"
        attribute n4:
            base_path + "yuri_shy_nose_n4.png"
        attribute n5:
            base_path + "yuri_shy_nose_n5.png"
    
    
    
    group mouth:
        
        # Default closed mouths
        attribute cm default if_any(["neut"]):
            base_path + "yuri_shy_mouth_m1.png"
        attribute cm default if_any(["angr","sad"]):
            base_path + "yuri_shy_mouth_m2.png"
        attribute cm default if_any(["happ"]):
            base_path + "yuri_shy_mouth_m3.png"
        
        # Default open mouth.
        attribute om:
            base_path + "yuri_shy_mouth_m4.png"
        
        
        # All mouths - truncated tags:
        attribute m1:
            base_path + "yuri_shy_mouth_m1.png"
        attribute m2:
            base_path + "yuri_shy_mouth_m2.png"
        attribute m3:
            base_path + "yuri_shy_mouth_m3.png"
        attribute m4:
            base_path + "yuri_shy_mouth_m4.png"
    
    
    
    group eyes if_not(["n5","bful"]): # Cannot show if full-face blush is present.
        
        # Open eyes
        attribute oe default if_any(["happ"]):
            base_path + "yuri_shy_eyes_e1.png"
        attribute oe default if_any(["neut"]):
            base_path + "yuri_shy_eyes_e2.png"
        attribute oe default if_any(["angr"]):
            base_path + "yuri_shy_eyes_e3.png"
        attribute oe default if_any(["sad"]):
            base_path + "yuri_shy_eyes_e4.png"
        
        # Closed eyes
        attribute ce if_any(["angr","neut","happ"]):
            base_path + "yuri_shy_eyes_e5.png"
        attribute ce if_any(["sad"]):
            base_path + "yuri_shy_eyes_e6.png"
        
        
        # All eyes - truncated tags:
        attribute e1:
            base_path + "yuri_shy_eyes_e1.png"
        attribute e2:
            base_path + "yuri_shy_eyes_e2.png"
        attribute e3:
            base_path + "yuri_shy_eyes_e3.png"
        attribute e4:
            base_path + "yuri_shy_eyes_e4.png"
        attribute e5:
            base_path + "yuri_shy_eyes_e5.png"
        attribute e6:
            base_path + "yuri_shy_eyes_e6.png"

        ### LayeredRedux's Extra Eyes
        #--------------------------------------------------------------------------------------
        attribute e7:
            extra_path + "yuri_shy_eyes_e7.png"
        #--------------------------------------------------------------------------------------

    
    
    
    group eyebrows if_not(["n5","bful"]): # Cannot show if full-face blush is present.
        
        attribute brow default if_any(["happ"]):
            base_path + "yuri_shy_eyebrows_b1.png"
        attribute brow default if_any(["neut","sad"]):
            base_path + "yuri_shy_eyebrows_b2.png"
        attribute brow default if_any(["angr"]):
            base_path + "yuri_shy_eyebrows_b3.png"
        
        
        # All brows - Truncated:
        attribute b1:
            base_path + "yuri_shy_eyebrows_b1.png"
        attribute b2:
            base_path + "yuri_shy_eyebrows_b2.png"
        attribute b3:
            base_path + "yuri_shy_eyebrows_b3.png"

    ### Group added for LayeredRedux
    #--------------------------------------------------------------------------------------
    group sweat:
        attribute sweat1:
            extra_path + "yuri_shy_sweat.png"
    #--------------------------------------------------------------------------------------