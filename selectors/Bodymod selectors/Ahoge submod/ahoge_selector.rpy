# Credit to RaVen for a template, submod by MayJay

init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["ahoge_acs"] = {
        "_ev": "monika_ahoge_acs_select",
        "_min-items": 1,
        "change": "Can you change your ahoge?",
        "wear": "Can you make an ahoge in your hair?",
    }

#init -9 python in mas_selspr:
    #GRP_TOPIC_LIST.append("ahoge_acs")


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_ahoge_acs_select",
            category=["appearance"],
            prompt=store.mas_selspr.get_prompt("ahoge_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label monika_ahoge_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="ahoge_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What kind of ahoge do you want me to wear?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."