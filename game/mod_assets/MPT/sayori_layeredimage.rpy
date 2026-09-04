init python:

    # Base folders for the MPT. If you need to change the path for
    # whatever reason, just change the ones below!
    base_path = "mod_assets/MPT/sayori/"
    extra_path = base_path + "extra_assets/"

layeredimage sayori turned: # turned definitions.
    
    # This makes the sprite one single texture, instead of multiple textures on top of each other.
    # This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution=False)
    
    always base_path + "sayori_turned_facebase.png" # Always need this face.
    
    # Attributes for autofocus logic.
    group af_logic multiple:
        attribute afm null # This attribute controls whether automatic control of the mouths takes place or not.  Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null # This attribute controls whether automatic control of zorder takes place or not.  Add this tag to a character to enable automatic zorder control, remove it to disable it.
    
    group outfit: # These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: # Mood determines what the defaults images are for the following attributes:
        # "oe", "ce", "om", "cm", "brow".
        # By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
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
        attribute focu null # focus
        # attribute xxxx null # xxxx # Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: # Have to separate these out, they can't share moods.
        attribute nobl default null # No blush.
        attribute empty null
        attribute awkw null # awkward.  defaults for n
        attribute blus null # blushing.  defaults for n
        attribute blaw null # blushing and awkward.  defaults for n
    
    
    
    # Left arm variants
    group left if_any(["uniform"]):
        attribute ldown default:
            base_path + "sayori_turned_uniform_left_down.png"
        attribute lup:
            base_path + "sayori_turned_uniform_left_up.png"
    
    group left if_any(["casual"]):
        attribute ldown default:
            base_path + "sayori_turned_casual_left_down.png"
        attribute lup:
            base_path + "sayori_turned_casual_left_up.png"
    
    
    
    # Right arm variants
    group right if_any(["uniform"]):
        attribute rdown default:
            base_path + "sayori_turned_uniform_right_down.png"
        attribute rup:
            base_path + "sayori_turned_uniform_right_up.png"
    
    group right if_any(["casual"]):
        attribute rdown default:
            base_path + "sayori_turned_casual_right_down.png"
        attribute rup:
            base_path + "sayori_turned_casual_right_up.png"
    
    
    
    group nose:
        
        # Default nose/blush.
        attribute nose default if_any(["nobl"]):# default nose
            base_path + "sayori_turned_nose_n1.png"
        attribute nose if_any(["awkw"]):# default nose when "awkward"
            base_path + "sayori_turned_nose_n2.png"
        attribute nose if_any(["blus"]):# default nose when "blushing"
            base_path + "sayori_turned_nose_n3.png"
        attribute nose if_any(["blaw"]):# default nose when "blushing and awkward"
            base_path + "sayori_turned_nose_n4.png"
        attribute nose if_any(["empty"]):
            null
        
        
        # All noses - truncated tags:
        attribute n1:
            base_path + "sayori_turned_nose_n1.png"
        attribute n2:
            base_path + "sayori_turned_nose_n2.png"
        attribute n3:
            base_path + "sayori_turned_nose_n3.png"
        attribute n4:
            base_path + "sayori_turned_nose_n4.png"
        attribute nl:
            base_path + "sayori_turned_nose_nl.png"
    
    
    
    group mouth:
        
        # Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            base_path + "sayori_turned_mouth_ma.png"
        attribute cm default if_any(["neut","anno","worr","curi"]):
            base_path + "sayori_turned_mouth_md.png"
        attribute cm default if_any(["dist","flus"]):
            base_path + "sayori_turned_mouth_me.png"
        attribute cm default if_any(["lsur","shoc", "focu"]):
            base_path + "sayori_turned_mouth_mf.png"
        attribute cm default if_any(["sad","angr","pout","doub"]):
            base_path + "sayori_turned_mouth_mj.png"
        attribute cm default if_any(["cry","pani","vsur"]):
            base_path + "sayori_turned_mouth_mk.png"
        attribute cm default if_any(["vang"]):
            base_path + "sayori_turned_mouth_mm.png"
        attribute cm default if_any(["laug"]):
            base_path + "sayori_turned_mouth_mn.png"
        attribute cm default if_any(["yand"]):
            base_path + "sayori_turned_mouth_mo.png"
        
        # Open Mouths:
        attribute om if_any(["happ","laug"]):
            base_path + "sayori_turned_mouth_mb.png"
        attribute om if_any(["yand","nerv"]):
            base_path + "sayori_turned_mouth_mc.png"
        attribute om if_any(["pout","sedu"]):
            base_path + "sayori_turned_mouth_mf.png"
        attribute om if_any(["sad","lsur","dist","focu"]):
            base_path + "sayori_turned_mouth_mg.png"
        attribute om if_any(["neut","anno","shoc","worr"]):
            base_path + "sayori_turned_mouth_mh.png"
        attribute om if_any(["curi","doub"]):
            base_path + "sayori_turned_mouth_mi.png"
        attribute om if_any(["flus"]):
            base_path + "sayori_turned_mouth_mk.png"
        attribute om if_any(["cry","vsur"]):
            base_path + "sayori_turned_mouth_ml.png"
        attribute om if_any(["angr","pani","vang"]):
            base_path + "sayori_turned_mouth_mq.png"
        
        
        ### All mouths - truncated tags:
        attribute ma:
            base_path + "sayori_turned_mouth_ma.png"
        attribute mb:
            base_path + "sayori_turned_mouth_mb.png"
        attribute mc:
            base_path + "sayori_turned_mouth_mc.png"
        attribute md:
            base_path + "sayori_turned_mouth_md.png"
        attribute me:
            base_path + "sayori_turned_mouth_me.png"
        attribute mf:
            base_path + "sayori_turned_mouth_mf.png"
        attribute mg:
            base_path + "sayori_turned_mouth_mg.png"
        attribute mh:
            base_path + "sayori_turned_mouth_mh.png"
        attribute mi:
            base_path + "sayori_turned_mouth_mi.png"
        attribute mj:
            base_path + "sayori_turned_mouth_mj.png"
        attribute mk:
            base_path + "sayori_turned_mouth_mk.png"
        attribute ml:
            base_path + "sayori_turned_mouth_ml.png"
        attribute mm:
            base_path + "sayori_turned_mouth_mm.png"
        attribute mn:
            base_path + "sayori_turned_mouth_mn.png"
        attribute mo:
            base_path + "sayori_turned_mouth_mo.png"
        attribute mp:
            base_path + "sayori_turned_mouth_mp.png"
        attribute mq:
            base_path + "sayori_turned_mouth_mq.png"
        attribute mr:
            base_path + "sayori_turned_mouth_mr.png"

        ### LayeredRedux's Extra Mouths.
        #--------------------------------------------------------------------------------------
        attribute ms:
            extra_path + "sayori_turned_mouth_ms.png"
        attribute mt:
            extra_path + "sayori_turned_mouth_mt.png"
        attribute mu:
            extra_path + "sayori_turned_mouth_mu.png"
        attribute mv:
            extra_path + "sayori_turned_mouth_mv.png"
        attribute mw:
            extra_path + "sayori_turned_mouth_mw.png"
        #--------------------------------------------------------------------------------------
    
    
    
    group eyes if_not(["s_scream","s_scream_alt","s_dark"]):
        
        # Default Opened eyes:
        attribute oe default if_any(["neut","angr","happ","laug","sad"]):
            base_path + "sayori_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr","pout", "nerv"]):
            base_path + "sayori_turned_eyes_e1b.png"
        attribute oe default if_any(["anno","sedu","doub"]):
            base_path + "sayori_turned_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            base_path + "sayori_turned_eyes_e1g.png"
        attribute oe default if_any(["lsur","flus","vsur","curi","focu"]):
            base_path + "sayori_turned_eyes_e2a.png"
        attribute oe default if_any(["pani","vang","shoc"]):
            base_path + "sayori_turned_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            base_path + "sayori_turned_eyes_e3a.png"
        
        # Default Closed eyes:
        attribute ce if_any(["sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]):
            base_path + "sayori_turned_eyes_e4a.png"
        attribute ce if_any(["neut","happ","lsur","laug","yand","pout","sedu","focu"]):
            base_path + "sayori_turned_eyes_e4b.png"
        attribute ce if_any(["vang","flus","pani","vsur"]):
            base_path + "sayori_turned_eyes_e4c.png"
        attribute ce if_any(["cry"]):
            base_path + "sayori_turned_eyes_e4d.png"
        
        
        ### All eyes - truncated tags:
        attribute e1a:
            base_path + "sayori_turned_eyes_e1a.png"
        attribute e1b:
            base_path + "sayori_turned_eyes_e1b.png"
        attribute e1c:
            base_path + "sayori_turned_eyes_e1c.png"
        attribute e1d:
            base_path + "sayori_turned_eyes_e1d.png"
        attribute e1e:
            base_path + "sayori_turned_eyes_e1e.png"
        attribute e1f:
            base_path + "sayori_turned_eyes_e1f.png"
        attribute e1g:
            base_path + "sayori_turned_eyes_e1g.png"
        attribute e1h:
            base_path + "sayori_turned_eyes_e1h.png"
        attribute e2a:
            base_path + "sayori_turned_eyes_e2a.png"
        attribute e2b:
            base_path + "sayori_turned_eyes_e2b.png"
        attribute e2c:
            base_path + "sayori_turned_eyes_e2c.png"
        attribute e2d:
            base_path + "sayori_turned_eyes_e2d.png"
        attribute e3a:
            base_path + "sayori_turned_eyes_e3a.png"
        attribute e3b:
            base_path + "sayori_turned_eyes_e3b.png"
        attribute e4a:
            base_path + "sayori_turned_eyes_e4a.png"
        attribute e4b:
            base_path + "sayori_turned_eyes_e4b.png"
        attribute e4c:
            base_path + "sayori_turned_eyes_e4c.png"
        attribute e4d:
            base_path + "sayori_turned_eyes_e4d.png"
        attribute e4e:
            base_path + "sayori_turned_eyes_e4e.png"
        attribute e0a:
            base_path + "sayori_turned_eyes_e0a.png"
        attribute e0b:
            base_path + "sayori_turned_eyes_e0b.png"

        ### LayeredRedux's Extra Eyes.
        #--------------------------------------------------------------------------------------
        attribute e2e:
            extra_path + "sayori_turned_eyes_e2e.png"
        attribute e2f:
            extra_path + "sayori_turned_eyes_e2f.png"
        attribute e2g:
            extra_path + "sayori_turned_eyes_e2g.png"
        attribute e2h:
            extra_path + "sayori_turned_eyes_e2h.png"
        attribute e2i:
            extra_path + "sayori_turned_eyes_e2i.png"
        attribute e3c:
            extra_path + "sayori_turned_eyes_e3c.png"
        attribute e4f:
            extra_path + "sayori_turned_eyes_e4f.png"
        attribute e4g:
            extra_path + "sayori_turned_eyes_e4g.png"
        attribute e4h:
            extra_path + "sayori_turned_eyes_e4h.png"
        attribute e0c:
            extra_path + "sayori_turned_eyes_e0c.png"
        attribute e0d:
            extra_path + "sayori_turned_eyes_e0d.png"
        attribute e0e:
            extra_path + "sayori_turned_eyes_e0e.png"
        attribute e0f:
            extra_path + "sayori_turned_eyes_e0f.png"
        attribute e0g:
            extra_path + "sayori_turned_eyes_e0g.png"
        attribute e0h:
            extra_path + "sayori_turned_eyes_e0h.png"
        attribute esilly1:
            extra_path + "sayori_turned_eyes_silly1.png"
        attribute esilly2:
            extra_path + "sayori_turned_eyes_silly2.png"
        attribute estar1a:
            extra_path + "sayori_turned_eyes_star1a.png"
        attribute estar1b:
            extra_path + "sayori_turned_eyes_star1b.png"
        attribute estar2a:
            extra_path + "sayori_turned_eyes_star2a.png"
        attribute estar2b:
            extra_path + "sayori_turned_eyes_star2b.png"
        attribute estar3a:
            extra_path + "sayori_turned_eyes_star3a.png"
        attribute estar3b:
            extra_path + "sayori_turned_eyes_star3a.png"
        #--------------------------------------------------------------------------------------
    
    
    
    group eyebrows if_not(["s_scream","s_scream_alt","s_dark"]):
        
        # Default Eyebrows:
        attribute brow default if_any(["neut","happ","lsur","flus","shoc"]):
            base_path + "sayori_turned_eyebrows_b1a.png"
        attribute brow default if_any(["sad","cry","pani","yand","nerv"]):
            base_path + "sayori_turned_eyebrows_b1b.png"
        attribute brow default if_any(["laug","vsur","worr","sedu"]):
            base_path + "sayori_turned_eyebrows_b1c.png"
        attribute brow default if_any(["anno","pout","focu"]):
            base_path + "sayori_turned_eyebrows_b1d.png"
        attribute brow default if_any(["angr","vang"]):
            base_path + "sayori_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curi","doub"]):
            base_path + "sayori_turned_eyebrows_b1f.png"
        
        # The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            base_path + "sayori_turned_eyebrows_b2a.png"
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            base_path + "sayori_turned_eyebrows_b3c.png"
        
        
        ### All eyebrows - truncated tags:
        attribute b1a:
            base_path + "sayori_turned_eyebrows_b1a.png"
        attribute b1b:
            base_path + "sayori_turned_eyebrows_b1b.png"
        attribute b1c:
            base_path + "sayori_turned_eyebrows_b1c.png"
        attribute b1d:
            base_path + "sayori_turned_eyebrows_b1d.png"
        attribute b1e:
            base_path + "sayori_turned_eyebrows_b1e.png"
        attribute b1f:
            base_path + "sayori_turned_eyebrows_b1f.png"
        attribute b2a:
            base_path + "sayori_turned_eyebrows_b2a.png"
        attribute b2b:
            base_path + "sayori_turned_eyebrows_b2b.png"
        attribute b2c:
            base_path + "sayori_turned_eyebrows_b2c.png"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            base_path + "sayori_turned_eyebrows_b3a.png"
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            base_path + "sayori_turned_eyebrows_b3b.png"
        attribute b3c if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            base_path + "sayori_turned_eyebrows_b3c.png"
    
    
    # This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
        
        attribute s_scream:
            base_path + "sayori_turned_special_scream.png"
        #--------------------------------------------------------------------------------------
        attribute s_scream_alt:
            extra_path + "sayori_turned_special_scream_alt.png"
        attribute s_dark:
            extra_path + "sayori_turned_special_dark.png"
        #--------------------------------------------------------------------------------------

    ### These next few groups were added specifically for LayeredRedux.
    #--------------------------------------------------------------------------------------

    group sweat:
        attribute sweat1:
            extra_path + "sayori_turned_sweat.png"
        attribute sweat2:
            extra_path + "sayori_turned_sweat2.png"

    group eyemarks:
        attribute eyebags:
            extra_path + "sayori_turned_eyebags.png"

    group tears:
        attribute tears1:
            extra_path + "sayori_turned_tears.png"
        attribute tears2:
            extra_path + "sayori_turned_sobbing.png"

    #--------------------------------------------------------------------------------------



layeredimage sayori tap: # tapping definitions.
    
    # This makes the sprite one single texture, instead of multiple textures on top of each other.
    # This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at renpy.partial(Flatten, drawable_resolution=False)
    
    # Attributes for autofocus logic.
    group af_logic multiple:
        attribute afm null # This attribute controls whether automatic control of the mouths takes place or not.  Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null # This attribute controls whether automatic control of zorder takes place or not.  Add this tag to a character to enable automatic zorder control, remove it to disable it.
    
    group outfit:
        attribute uniform default:
            base_path + "sayori_tapping_uniform_bodybase.png"
        attribute casual:
            base_path + "sayori_tapping_casual_bodybase.png"
    
    always base_path + "sayori_tapping_facebase.png"
    
    
    
    group mood: # Mood determines what the defaults images are for the following attributes:
        # "oe", "ce", "om", "cm", "brow".
        # By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        # Additionally, you can add in any new ones as you like.
        attribute nerv default null # nervous
        attribute angr null # angry
        attribute dist null # distant
        attribute neut null # neutral
        attribute pout null # pouting
    
    
    
    group blush: # Have to separate these out, they can't share moods.
        attribute nobl default null # no blush applied.
        attribute awkw null # awkward.  defaults for n
        attribute blus null # blushing.  defaults for n
        attribute blaw null # blushing AND awkward.  defaults for n
        attribute bful null # full face blush.
    
    
    
    group nose:
        
        # Default nose/blush.
        attribute nose default if_any(["nobl"]):# Default nose
            base_path + "sayori_tapping_nose_n1.png"
        attribute nose default if_any(["awkw"]):# Default nose when "awkward"
            base_path + "sayori_tapping_nose_n2.png"
        attribute nose default if_any(["blus"]):# Default nose when "blushing"
            base_path + "sayori_tapping_nose_n3.png"
        attribute nose default if_any(["blaw"]):# Default nose when "blushing" and "awkward"
            base_path + "sayori_tapping_nose_n4.png"
        attribute nose default if_any(["bful"]):# Default nose when "blushing" and "awkward"
            base_path + "sayori_tapping_nose_n5.png"
        
        # All noses - truncated tags:
        attribute n1:
            base_path + "sayori_tapping_nose_n1.png"
        attribute n2:
            base_path + "sayori_tapping_nose_n2.png"
        attribute n3:
            base_path + "sayori_tapping_nose_n3.png"
        attribute n4:
            base_path + "sayori_tapping_nose_n4.png"
        attribute n5:
            base_path + "sayori_tapping_nose_n5.png"
    
    
    
    group mouth:
        
        # Default Closed Mouths:
        attribute cm default if_any(["pout"]):
            base_path + "sayori_tapping_mouth_m2.png"
        attribute cm default if_any(["neut","nerv","angr","dist"]):
            base_path + "sayori_tapping_mouth_m3.png"
        
        # Open Mouths:
        attribute om if_any(["nerv"]):
            base_path + "sayori_tapping_mouth_m1.png"
        attribute om if_any(["neut","pout","angr","dist"]):
            base_path + "sayori_tapping_mouth_m4.png"
        
        
        # All mouths - truncated tags:
        attribute m1:
            base_path + "sayori_tapping_mouth_m1.png"
        attribute m2:
            base_path + "sayori_tapping_mouth_m2.png"
        attribute m3:
            base_path + "sayori_tapping_mouth_m3.png"
        attribute m4:
            base_path + "sayori_tapping_mouth_m4.png"
        
        ### LayeredRedux's Extra Mouths
        #--------------------------------------------------------------------------------------
        attribute m5:
            extra_path + "sayori_tapping_mouth_m5.png"
        attribute m6:
            extra_path + "sayori_tapping_mouth_m6.png"
        attribute m7:
            extra_path + "sayori_tapping_mouth_m7.png"
        attribute m8:
            extra_path + "sayori_tapping_mouth_m8.png"
        attribute m9:
            extra_path + "sayori_tapping_mouth_m9.png"
        #--------------------------------------------------------------------------------------
    
    
    
    group eyes if_not(["n5","bful"]):
        
        # Default Opened eyes:
        attribute oe default if_any(["neut","nerv"]):
            base_path + "sayori_tapping_eyes_e1.png"
        attribute oe default if_any(["pout","dist"]):
            base_path + "sayori_tapping_eyes_e2.png"
        attribute oe default if_any(["angr"]):
            base_path + "sayori_tapping_eyes_e5.png"
        
        # Default Closed eyes:
        attribute ce if_any(["neut","nerv","pout","angr","dist"]):
            base_path + "sayori_tapping_eyes_e6.png"
        
        
        # All eyes - truncated tags:
        attribute e1:
            base_path + "sayori_tapping_eyes_e1.png"
        attribute e2:
            base_path + "sayori_tapping_eyes_e2.png"
        attribute e3:
            base_path + "sayori_tapping_eyes_e3.png"
        attribute e4:
            base_path + "sayori_tapping_eyes_e4.png"
        attribute e5:
            base_path + "sayori_tapping_eyes_e5.png"
        attribute e6:
            base_path + "sayori_tapping_eyes_e6.png"
        
        ### LayeredRedux's Extra Eyes
        #--------------------------------------------------------------------------------------
        attribute e7:
            extra_path + "sayori_tapping_eyes_e7.png"
        #--------------------------------------------------------------------------------------
    
    
    
    group eyebrows if_not(["n5","bful"]):
        
        # Default Eyebrows:
        attribute brow default if_any(["neut"]):
            base_path + "sayori_tapping_eyebrows_b3.png"
        attribute brow default if_any(["nerv","dist"]):
            base_path + "sayori_tapping_eyebrows_b1.png"
        attribute brow default if_any(["pout","angr"]):
            base_path + "sayori_tapping_eyebrows_b2.png"
        
        
        # All eyebrows - truncated tags:
        attribute b1:
            base_path + "sayori_tapping_eyebrows_b1.png"
        attribute b2:
            base_path + "sayori_tapping_eyebrows_b2.png"
        attribute b3:
            base_path + "sayori_tapping_eyebrows_b3.png"

        ### LayeredRedux's Extra Eyebrows
        #--------------------------------------------------------------------------------------
        attribute b4:
            extra_path + "sayori_tapping_eyebrows_b4.png"
        #--------------------------------------------------------------------------------------

    ### Group added for LayeredRedux
    #--------------------------------------------------------------------------------------
    group sweat:
        attribute sweat1:
            extra_path + "sayori_tapping_sweat.png"
    #--------------------------------------------------------------------------------------

