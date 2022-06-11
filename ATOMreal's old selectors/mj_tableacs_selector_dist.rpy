# Special thanks to RaVen for a template
#Edited by ATOM (u/The_Foothills). You will never be able to completely get rid of my trace i left in the community
#the comment above me is an overdramatic lil bitch. get bent, atom. -u/mayday-mayjay


init -99 python in mas_selspr:

    # acs type data
    PROMPT_MAP["table_acs"] = {
        "_ev": "mj_table_acs_select",
        "_min-items": 1,
        "change": "Can you put something else on your desk?",
        "wear": "Can you put something on your desk?",
    }

#keeping this here incase MAS devs ever try bring the need for this back
#init -9 python in mas_selspr:
    #GRP_TOPIC_LIST.append("table_acs")


#selector data
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mj_table_acs_select",
            category=["desk"],
            prompt=store.mas_selspr.get_prompt("table_acs", "change"),
            pool=True,
            unlocked=False,
            rules={"no_unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        ),
        restartBlacklist=True
    )

#more selector data
label mj_table_acs_select:
    python:
        use_acs = store.mas_selspr.filter_acs(True, group="table_acs")

        mailbox = store.mas_selspr.MASSelectableSpriteMailbox("What would you want me to put on the desk?")
        sel_map = {}

    m 1eua "Sure [player]!"

    call mas_selector_sidebar_select_acs(use_acs, mailbox=mailbox, select_map=sel_map, add_remover=True) #add_remover is for a 'None' option, basically

    if not _return:
        m 1eka "Oh, alright."