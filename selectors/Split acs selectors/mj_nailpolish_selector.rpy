# Credit to RaVen for a template, submod by MayJay

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["nailpolish_acs"] = {
        "_ev": "mj_nailpolish_acs_select",
        "_min-items": 1,
        "change": "Can you change your nailpolish?",
        "wear": "Can you wear some nailpolish?",
    }



#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_nailpolish_acs_select",
            category=["appearance"],
            prompt=store.mas_selspr.get_prompt("nailpolish_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_nailpolish_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="nailpolish_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What kind of nailpolish do you want me to have?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."