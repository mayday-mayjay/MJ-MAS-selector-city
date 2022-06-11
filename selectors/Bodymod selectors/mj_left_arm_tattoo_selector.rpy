# Credit to RaVen / ATOMreal for a template, submod by mayday-mayjay (dont reupload my stuff, nerd)


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["larmtattoo_acs"] = {
        "_ev": "mj_larmtattoo_acs_select",
        "_min-items": 1,
        "change": "Can you change your tattoo on your left arm?",
        "wear": "Can you put a tattoo on your left arm?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_larmtattoo_acs_select",
            category=["appearance"],
            prompt=store.mas_selspr.get_prompt("larmtattoo_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_larmtattoo_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="larmtattoo_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What tattoo would you like me to have?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, [mas_quipExp('6eua')], mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."
