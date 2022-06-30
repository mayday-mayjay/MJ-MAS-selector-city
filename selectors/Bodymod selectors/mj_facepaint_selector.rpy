# Credit to RaVen for a template, submod by MayJay

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["facepaint_acs"] = {
        "_ev": "mj_facepaint_acs_select",
        "_min-items": 1,
        "change": "Can you put on some different face-paint?",
        "wear": "Can you put on some face-paint?",
    }

#init -9 python in mas_selspr:
    #GRP_TOPIC_LIST.append("ahoge_acs")


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_facepaint_acs_select",
            category=["appearance"],
            prompt=store.mas_selspr.get_prompt("facepaint_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_facepaint_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="facepaint_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What kind of face-paint should I wear?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."