#Distributable Version of the mask selector, all changes should be documented as notes in the code
#credit to RaVen and ATOMreal for all of the code below
#new submod maintainer is mayday-mayjay

init -99 python in mas_selspr:

    # prompt constants go here
    PROMPT_MAP["mask"] = {
        "_ev": "mj_mask_select",
        "_min-items": 1,
        "change": "Can you change your mask?",
        "wear": "Can you wear a mask?",
    }

#init -9 python in mas_selspr:
    #GRP_TOPIC_LIST.append("mask")

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_mask_select",
            category=["appearance"],
            prompt=store.mas_selspr.get_prompt("mask", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )


label mj_mask_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="mask")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("Which mask would you like me to wear?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #Add remover is for a 'None' option, basically

    #Dialogue if you canceled out
    if not _return:
        m 1eka "Oh, alright."