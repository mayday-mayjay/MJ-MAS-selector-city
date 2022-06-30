# Credit to RaVen for a template, submod by MayJay

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["headpiece_acs"] = {
        "_ev": "mj_headpiece_acs_select",
        "_min-items": 1,
        "change": "Can you change your headpiece?",
        "wear": "Can you wear a headpiece?",
    }



#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_headpiece_acs_select",
            category=["appearance"],
            prompt=store.mas_selspr.get_prompt("headpiece_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_headpiece_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="headpiece_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What kind of headpiece do you want me to wear?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."