# some dumdum called Q made this i think

""" 
credits :3 !!!

KaylaThePianist - coding rubber quackie
Pseurae - big code help and code review
Elckarow - code help

"""

# Plug-and-Play Auto²focus and Auto Zorder
#
# !!!!!!!!!!!!!!! USAGE INSTRUCTIONS !!!!!!!!!!!!!!! #
# 1. drop file in game folder                        #
# 2. done !                                          #
# ####################################################
#
#
#
# Notes
# -If you were using another autofocus implementation before, 
#  you might want to remove the stuff associated with it for this to work fully as intended,
#  otherwise you'll probably get double autofocus or something.
#
#
# -The way Auto²focus works is by detecting all the characters with *image tags*, 
#  and applying autofocus to all images with that tag.
#
#  So, for example... 
""" define stelle = Character("Nameless", image="stelle") """ # image tag is "stelle" 
#  ...is a valid character, becuase of the image tag associated with it,
#
#  and all images with that start with the tag "stelle":
"""
    image stelle funny = "stellefunny.png"
    image stelle raccoon = im.Composite((960, 960), (0, 0), "1l.png", (0, 0), "1r.png", (0, 0), "trash.png")
    layeredimage stelle:
        # ...
"""
#  will have autofocus automatically applied to them.
#
#   
#  On the contrary...
""" define aaron = Character("Bum") """ # no image tag
#  ...is not a valid character and Auto²focus will not work with them.
#
#  !! Tagless characters, however, can still be used on multi-character focusing,
#  an example of which is down below.
#
#
#
# Some examples of functionality
#
# Ingame toggles
"""
label mystory:
    show sayori 1a at t41                  # composite character
    show natsuki turned happ cm oe at t42  # layeredimage (MPT) character
    show monika forward happ cm oe at t43
    show yuri turned happ cm oe at t44

    s "wow im so focused" # sayori focused
    n "no way me too" # natsuki focused
    
    "damn they're pretty focused" # no one focused

    $ af.disable("monika") # disable autofocus for monika
    m "hey why am i not focused"

    $ af.disableZoom("yuri") # only disable zoom for Yuri (will still dim)
    y "hmm i feel quite dim"

    $ af.enable("monika")
    m "ah there we go"

    $ af.enableZoom("yuri") 
    y "oh, great. zoomies."

"""
#
#
# Support for multi-character focus and forced focusing
"""
# define special characters
define ny = Character('Nat & yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ev = Character('Everyone',   what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")


# due to characters usually being defined at init 0
# autofocus configs should be set later, at init 1, just to be absolutely sure.
# but it probably works at regular init time as well
init python:

    # for "Nat & Yuri" special character
    af.addCharacterToTag('natsuki', ny) # natsuki will now react and focus when 'ny' is talking 
    af.addCharacterToTag('yuri', ny) # same for yuri

    # for "Everyone" special character
    for tag in af.getAutofocusCharacterTags(): # get all the characters...
        af.addCharacterToTag(tag, ev) # ...and make them focus when 'ev' talks


label myotherstory:
    show monika forward happ cm oe at t41
    show natsuki turned happ cm oe at t43
    show yuri turned happ cm oe at t44

    m "...yall are so gay"

    ny "NO WE'RE NOT"  # natsuki and yuri focused

    show sayori happ cm oe at t42

    s "I HAVE A BOMB!!"

    # force monika, natsuki and yuri to be focused
    $ af.forceFocus("monika") 
    $ af.forceFocus("natsuki")
    $ af.forceFocus("yuri")

    "Club" "OH MY GOD RUN WE'RE GONNA DIE"

    $ af.unforceFocus("monika")
    $ af.unforceFocus("natsuki")
    $ af.unforceFocus("yuri")
"""
#
#
# auto zorder
"""

label myfinalstory:
    show sayori turned happ cm oe at t41
    show natsuki turned happ cm oe at t42

    n "damn im so focused and ordered in the z axis"
    s "wow me too no way"
    s "I'm so happy i want to hug you"
    
    $ af.disableAutoZorder("sayori")
    $ af.disableAutoZorder("natsuki")
    show sayori zorder 0 at t42
    show natsuki zorder 1
    
    s "yay!!"
    show sayori at h42
    s "hugs hugs hugs!!!"
    show natsuki at h42
    n "DWEJJSFJSDIAFJKSDSK GET AWAY FROM ME"
    
    show sayori at t32

    $ af.enableAutoZorder("sayori")
    $ af.enableAutoZorder("natsuki")
    n "eugh."
    s "hehe~"
"""
#
#
# Other configs
"""
init python:
    
    # you can modify how each character is zoomed and dimmed.
    # 
    # take a look at the defaultconfig variable down below
    # for the variables you can change
    af.setZoomConfig("natsuki", "focus", 1.5)                      # big focus zoom
    af.setZoomConfig("natsuki", "time", 0.75)                      # slow focus time
    af.setZoomConfig("natsuki", "warper", _warper.easein_elastic)  # special warper
    af.setDimConfig("natsuki", "idle", -0.5)                       # very dark idle dimming

"""


import renpy # type: ignore
"""renpy
init -100 python in af:
"""
from renpy import store # type: ignore
from store import _warper # type: ignore


# ive been forced (by myself) to add these in 
errmsg = "You're using a Ren'Py version ({}) that's incompatible with Auto²focus. The earliest compatible Ren'Py {} version is {}."
if renpy.version_tuple.major == 7 and renpy.version_tuple < (7, 7, 0, 24012702):
    raise Exception(errmsg.format(renpy.version_only, 7, "7.7.0"))
elif renpy.version_tuple.major == 8 and renpy.version_tuple < (8, 2, 0, 24012702):
    raise Exception(errmsg.format(renpy.version_only, 8, "8.2.0"))
elif renpy.version_tuple.major < 7:
    raise Exception("You're using a Ren'Py version ({}) that's incompatible with Auto²focus. The earliest compatible Ren'Py versions are 7.7.0/8.2.0.".format(renpy.version_only))



# if we're showing under this many characters, disable autofocus
# set to 2 as default, aka if only one character is showing, disable focus
# (set to None for no limits)
LowCharacterLimit = None 

# global controls
enabled = True
zoomActive = True
dimActive = True
autoZorderActive = True


# zorder values for autozorder
speaker_zorder = 2
idle_zorder = 1


# the default values for zoom and dim
defaultconfig = {
    "zoom": {
        "idle": 1.0, # initial zoom
        "focus": 1.01, # final zoom
        "time": 0.15, # zoom time
        "warper": _warper.easein, # zoom warper
    },

    # same values but for dimming
    # Antes: idle -0.1 / focus 0.0 -- el personaje que habla quedaba con el
    # brillo tal cual (0.0, sin oscurecer nada), lo que por contraste con el
    # otro personaje atenuado se veía muy pálido/blanco. Luego se subió a
    # idle -0.25 / focus -0.1 para corregir eso, pero terminó siendo
    # demasiado oscuro para el personaje que NO habla. Se bajó de nuevo,
    # manteniendo una diferencia similar entre los dos (~0.1) para que la
    # sombra del que no habla se siga notando sin verse casi negro.
    "dim": {
        "idle": -0.15,
        "focus": -0.03,
        "time": 0.15,
        "warper": _warper.easein,
    },
    "zorder":{
        "idle": idle_zorder,
        "speak": speaker_zorder
    }
}

# where the per-character configs are stored (this gets filled with {tag: defaultconfig} entries later)
customconfigs = dict()

# stores the characters that are being force-focused
forced = set()

# for enabling/disabling zooming and dimming for each character
# so if the character is not in the set, they will not zoom/dim
zoomed = set()
dimmed = set()

# stores {"tag": bool} entries for each character to control auto zorder
zordered = dict()

# this holds {tag: [list of Character objects]} entries
# i.e. {"natsuki": [<Character: 'n_name'>, <Character: 'Nat & Yuri'>, <Character: 'Everyone'>]}
characters = dict()


# the main brains behind animating the autofocus
"""renpy
init -101 python in af:
"""
class WarpedTimeProgressTracker:
    def __init__(self, maxTime, warp, minTime=0.0, _progress=0.0):
        assert minTime <= maxTime
        self.minTime = minTime
        self.maxTime = maxTime
        self.warp = warp

        self.done = True if minTime == maxTime or maxTime == 0.0 else False
        self.progress = _progress
        self.warpedProgress = self.progress
    
    @property
    def warpedProgress(self):
        return self._warpedProgress
    
    @warpedProgress.setter
    def warpedProgress(self, value):
        self._warpedProgress = self.warp(value)

    def update(self, dt):
        self.progress += dt
        self.progress = min(self.maxTime, max(self.minTime, self.progress))

        complete = (self.progress / self.maxTime) if self.maxTime else 1.0
        if complete <= 0.0: complete = 0.0
        if complete >= 1.0:
            complete = 1.0
            self.done = True
        else: self.done = False
        
        self.warpedProgress = complete

        return self.warpedProgress
        
    def reset(self):
        self.progress = 0.0
        self.done = False


class SingleLerp:
    def __init__(self, start, end, time, warper):
        self.start = start
        self.end = end
        self.tracker = WarpedTimeProgressTracker(time, warper)

    @staticmethod
    def lerp(a, b, t):
        return a + (b-a)*t

def getargs(k, d):
    if k in d:
        return d.get(k)
    else:
        return defaultconfig.get(k)
cgetargs = renpy.curry(getargs)



"""renpy
init -100 python in af:
"""
from renpy import store # type: ignore
from store import ( # type: ignore
    _warper, At, BrightnessMatrix, Transform, 
    LayeredImage, LayeredImageProxy)

class Speaking:
    def __init__(self, chars):
        self.chars = chars

    def isSpeaking(self):
        if LowCharacterLimit is not None:
            if len(renpy.get_showing_tags() & set(characters.keys())) < LowCharacterLimit:
                return None

        # Obtener quién está hablando
        char = renpy.last_say().who

        if isinstance(char, renpy.character.ADVCharacter):
            # Comprobamos si el objeto 'char' (ej: 'ny' o 's') está en la lista de personajes permitidos para esta etiqueta
            self.speaking = any(c == char for c in self.chars)
            return self.speaking
            
        return False


# zoom controller
class CharacterZoom(Speaking):
    def __init__(self, tag, chars):
        super(CharacterZoom,self).__init__(chars)
        self.tag = tag
    
        g = cgetargs(d=customconfigs[tag]["zoom"])
        idle  = g("idle")
        focus = g("focus")
        time  = g("time")
        warp  = g("warper")
        
        self.sl = SingleLerp(idle, focus, time, warp)

    def __call__(self, trans, st, at, dt):
        zoom = self.tag in zoomed
        force = self.tag in forced
        speaking = self.isSpeaking() not in (False, None)

        if enabled and ((speaking and zoom and zoomActive) or force): 
            t = self.sl.tracker.update(dt)
        else: 
            t = self.sl.tracker.update(-dt)

        trans.zoom = SingleLerp.lerp(self.sl.start, self.sl.end, t)

# dim controller
class CharacterDim(Speaking):
    def __init__(self, tag, chars):
        super(CharacterDim,self).__init__(chars)
        self.tag = tag
        
        g = cgetargs(d=customconfigs[tag]["dim"])
        idle  = g("idle")
        focus = g("focus")
        time  = g("time")
        warp  = g("warper")
        
        self.sl = SingleLerp(idle, focus, time, warp)

    def __call__(self, trans, st, at, dt):
        dim = self.tag in dimmed
        force = self.tag in forced
        speaking = self.isSpeaking() in (True, None)

        if not enabled or enabled and (speaking or force or not (dim and dimActive)):
            t = self.sl.tracker.update(dt)
        else: 
            t = self.sl.tracker.update(-dt)
        trans.matrixcolor = BrightnessMatrix(SingleLerp.lerp(self.sl.start, self.sl.end, t))


# this merges the zoom and dim controllers and passes some other stuff to them
class DTFM:
    def __init__(self, initialAttrs, use_at=True):
        self.attrs = list(initialAttrs)

        self.use_at = use_at
        self.last_t = 0.0

    def addAttr(self, attr):
        self.attrs.append(attr)
    
    def __call__(self, trans, st, at):
        t = (at if self.use_at else st)
        dt = max(t-self.last_t, 1/144)
        
        self.last_t = t
        for attr in self.attrs:
            attr(trans, st, at, dt)
        return 0


# the autofocus
def SimpleAutofocus(tag, chars):
    return Transform(function=DTFM([
        CharacterZoom(tag, chars),
        CharacterDim(tag, chars)
        ])
    )

# helper thingy for non-layeredimage disps
def AutofocusWrap(d, af):
    return At(d, af)


# little function to check all defined images and wrap them in autofocus according to their tag
def wrapTaggedImages(charsDict):
    all_images = tuple(tuple(i.split()) for i in renpy.list_images())
    tags = charsDict.keys()
    for img in all_images:
        tag = img[0]
        if tag not in tags: continue

        d = renpy.get_registered_image(img)
        tag_af = getattr(store.af, tag)
        if not isinstance(d, (LayeredImage, LayeredImageProxy)):
            renpy.image(img, AutofocusWrap(d, tag_af))
        elif isinstance(d, LayeredImage):
            d.at = tuple(d.at) + (tag_af,)


# per-character toggles
def forceFocus(tag):   forced.add(tag)
def unforceFocus(tag): forced.remove(tag)

# zoom toggles
def enableZoom(tag):  zoomed.add(tag)
def disableZoom(tag): zoomed.remove(tag)
def toggleZoom(tag): 
    if tag in zoomed: disableZoom(tag)
    else: enableZoom(tag)

# dim toggles
def enableDim(tag):  dimmed.add(tag)
def disableDim(tag): dimmed.remove(tag)
def toggleDim(tag): 
    if tag in dimmed: disableDim(tag)
    else: enableDim(tag)

# autozorder toggles
def enableAutoZorder(tag):  zordered[tag] = True
def disableAutoZorder(tag): zordered[tag] = False
def toggleAutoZorder(tag): 
    zordered[tag] = not zordered[tag]

# general autofocus toggles
def enable(tag):
    enableZoom(tag)
    enableDim(tag)
    
def disable(tag):
    disableZoom(tag)
    disableDim(tag)
    
def toggle(tag): 
    toggleZoom(tag)
    toggleDim(tag)



## other miscellaneous functions
def getCharacterTags():
    return characters.keys()

def setZoomConfig(tag, config, value):
    customconfigs[tag]["zoom"][config] = value
def getZoomConfig(tag, config):
    if tag not in customconfigs.keys(): return None
    return customconfigs[tag]["zoom"][config]

def setDimConfig(tag, config, value):
    customconfigs[tag]["dim"][config] = value
def getDimConfig(tag, config):
    if tag not in customconfigs.keys(): return None
    return customconfigs[tag]["dim"][config]

def setZorderConfig(tag, config, value):
    customconfigs[tag]["zorder"][config] = value
def getZorderConfig(tag, config):
    if tag not in customconfigs.keys(): return None
    return customconfigs[tag]["zorder"][config]


# adds a character object to a tag
# so that this tag is checked against more than one character.
#
# This is helpful for when you have 
# a special character meant to act as multiple
# i.e. the "Nat & Yuri" character
def addCharacterToTag(tag, char):
    characters[tag].append(char)


"""renpy
init -1 python in af:
"""
from renpy import store # type: ignore
from copy import deepcopy

# override the default character definition functions
# to add some autofocus logic in between
def Character(*args, **kwargs):
    rv = renpy.character.Character(*args, **kwargs)
    if rv.image_tag:
        tag = rv.image_tag
        customconfigs.update({tag: deepcopy(defaultconfig)})

        oldchars = characters.get(tag, [])
        characters[tag] = oldchars + [rv]

        zoomed.add(tag)
        dimmed.add(tag)
        zordered.update({tag: bool(autoZorderActive)})

    return rv
DynamicCharacter = renpy.partial(Character, dynamic=True)

store.Character = Character
store.DynamicCharacter = DynamicCharacter


# do this after init 500 (where images are defined)
"""renpy
init 501 python in af:
"""
# set autofocus variables for each character (autofocus.charactername)
# such as autofocus.monika, autofocus.natsuki, autofocus.sayori, autofocus.notyuricauseihateher
for tag, char in characters.items():
    setattr(store.af, tag, SimpleAutofocus(tag, char))
wrapTaggedImages(characters)


## Auto zorder
"""renpy
init python in af:
"""

speakers_queue = []
def push_to_speakers_queue(who):
    speakers_queue.append(who)
    if len(speakers_queue) > 2:
        speakers_queue.pop(0)

# assume characters are on the master layer
# will probably change this later somehow
# (tbf if you're putting them somewhere else
# you probably know what you're doing)
def autozorder_callback(ev, interact=True, **kwargs):
    if not interact: return
    if ev != "begin": return
    if not autoZorderActive: return

    stag = renpy.get_say_image_tag()
    if stag is not None:
        if not renpy.showing(stag): return
        push_to_speakers_queue(stag)
        if stag in zordered and zordered[stag]:
            renpy.change_zorder('master', stag, getZorderConfig(stag, "speak"))
    else:
        lastsay_who = renpy.last_say().who
        push_to_speakers_queue(lastsay_who)
        if isinstance(lastsay_who, renpy.character.ADVCharacter):
            for tag, charlist in characters.items():
                if lastsay_who in charlist and zordered[tag]:
                    renpy.change_zorder('master', tag, getZorderConfig(tag, "speak"))

    lastchar = speakers_queue[0]
    if isinstance(lastchar, renpy.character.ADVCharacter):
        if isinstance(renpy.last_say().who, renpy.character.ADVCharacter) and lastchar == renpy.last_say().who: return
        for tag, charlist in characters.items():
            if lastchar in charlist and zordered[tag]:
                renpy.change_zorder('master', tag, getZorderConfig(tag, "idle"))
    elif lastchar is not None and lastchar in zordered and zordered[lastchar]:
        if getZorderConfig(lastchar, "idle") is not None:
            renpy.change_zorder('master', lastchar, getZorderConfig(lastchar, "idle"))


"""renpy
init python:
"""
config.all_character_callbacks.append(af.autozorder_callback) # type: ignore