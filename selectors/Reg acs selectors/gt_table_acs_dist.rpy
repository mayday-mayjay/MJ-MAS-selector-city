#creds to u/geneTechnician for these ones, thank you for allowing me to host them on github!

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["ltable_acs"] = {
        "_ev": "gt_ltable_acs_select",
        "_min-items": 1,
        "change": "Can you put something else on the left side of your desk?",
        "wear": "Can you put something on the left side of your desk?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_ltable_acs_select",
            category=["desk"],
            prompt=store.mas_selspr.get_prompt("ltable_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_ltable_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="ltable_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What would you like me to put out on my desk?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."
return


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["rtable_acs"] = {
        "_ev": "gt_rtable_acs_select",
        "_min-items": 1,
        "change": "Can you put something else on the right side of your desk?",
        "wear": "Can you put something on the right side of your desk?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_rtable_acs_select",
            category=["desk"],
            prompt=store.mas_selspr.get_prompt("rtable_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_rtable_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="rtable_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What would you like me to put on my desk?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."
return


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["flowers_acs"] = {
        "_ev": "gt_flowers_acs_select",
        "_min-items": 1,
        "change": "Can you put out a different set of flowers?",
        "wear": "Can you put some flowers on your desk?",
    }


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gt_flowers_acs_select",
            category=["desk"],
            prompt=store.mas_selspr.get_prompt("flowers_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label gt_flowers_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="flowers_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What flowers would you like me to put out on the desk?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."
return