from dragonfly import (Grammar, AppContext, Dictation, Key)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class JetbrainsRule(MergeRule):
    pronunciation = "jet brains"

    mapping = {
        "quickfix":                 R(Key("a-enter"), rdescript="JetBrains: Quick Fix"),
        "duplicate":                R(Key("c-d"), rdescript="JetBrains: Duplicate"),
        "auto complete":            R(Key("cs-a"), rdescript="JetBrains: Auto Complete"),
        "format code":              R(Key("ca-l"), rdescript="JetBrains: Format Code"),
        "show doc":                 R(Key("c-q"), rdescript="JetBrains: Show Documentation"),
        "show param":               R(Key("c-p"), rdescript="JetBrains: Show Parameters"),
        "Jen method":               R(Key("a-insert"), rdescript="JetBrains: Generated Method"),
        "jump to source":           R(Key("f4"), rdescript="JetBrains: Jump To Source"),
        "delete line":              R(Key("c-y"), rdescript="JetBrains: Delete Line"),
        "search symbol":            R(Key("cas-n"), rdescript="JetBrains: Search Symbol"),
        "build":                    R(Key("c-f9"), rdescript="JetBrains: Build"),
        "build and run":            R(Key("s-f10"), rdescript="JetBrains: Build And Run"),
        "next tab":                 R(Key("a-right"), rdescript="JetBrains: Next Tab"),
        "prior tab":                R(Key("a-left"), rdescript="JetBrains: Previous Tab"),
        
        "comment line":             R(Key("c-slash"), rdescript="JetBrains: Comment Line"), 
        "uncomment line":           R(Key("cs-slash"), rdescript="JetBrains: Uncomment Line"), 
        "select ex":                R(Key("c-w"), rdescript="JetBrains: untitled command"), 
        "select ex down":           R(Key("cs-w"), rdescript="JetBrains: entitled command"),
        "search everywhere":        R(Key("shift, shift"), rdescript="JetBrains: Search Everywhere"),
        "find in current":          R(Key("cs-f"), rdescript="JetBrains: Find In Current"),
        "go to line":               R(Key("c-g"), rdescript="JetBrains: Go To Line"), 
        }
    extras = [
              Dictation("text"),
              Dictation("mim"),
              IntegerRefST("n", 1, 1000),
              
             ]
    defaults = {"n": 1, "mim":""}

#---------------------------------------------------------------------------

context = AppContext(executable="idea", title="IntelliJ") \
          | AppContext(executable="idea64", title="IntelliJ") \
          | AppContext(executable="studio64") \
          | AppContext(executable="pycharm")
grammar = Grammar("IntelliJ + Android Studio + PyCharm", context=context)

if settings.SETTINGS["apps"]["jetbrains"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(JetbrainsRule())
    else:
        rule = JetbrainsRule(name="jet brains")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()