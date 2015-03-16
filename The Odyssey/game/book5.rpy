# Odysseus - the Nymph and Shipwreck

label book5:
    
    # Assembly of the gods
    
    scene bg assembly gods
    with fade
    
    "The gods had assembled once more.{w=0.5} Athena had beseeched her father to show mercy to Odysseus.{w=0.5}"
    
    athe "Father,{w=0.25} please allow Odysseus to return home.{w=0.5} He has no boat,{w=0.25} no crew.{w=0.5}"
    
    athe "He is being held back against his will.{w=0.5}"
    
    athe "Suitors who have ruined his home are now plotting to murder his son,{w=0.25} Telemachus.{w=0.5}"
    
    zeus "Odysseus shall return home with your blessing.{w=0.5} He will pay the traitors back.{w=0.5}"
    
    zeus "Bless his son so he will return home safely.{w=0.5}"
    
    zeus "Hermes,{w=0.25} go to Calypso and tell her to release Odysseus.{w=0.5} It is time he returned to his family.{w=0.5}"
    
    # Calypso's home
    
    scene bg calypso home
    with fade
    
    "Upon entering Calypso's luxurious home,{w=0.25} Hermes seats himself and dines with her.{w=0.5}"
    
    "After some time,{w=0.25} he tells her of Zeus' decree.{w=0.5}"
    
    herm "Zeus claims you are holding Odysseus,{w=0.25} warrior who fought at Troy for nine years.{w=0.5}"
    
    herm "He now commands you to release him and allow him to return to his home.{w=0.5}"
    
    caly "What? You gods are cruel.{w=0.5}"
    
    caly "You take mortals as you choose,{w=0.25} but now you chatise me for doing the same?"
    
    caly "I was the one who saved his life while his crew perished at the hands of Zeus' fury.{w=0.5}"
    
    caly "But,{w=0.25} no one can deny Zeus,{w=0.25} now can they? Unfortunately,{w=0.25} though,{w=0.25} I have neither ship nor crew for him.{w=0.5}"
    
    "Hermes,{w=0.25} now having relayed Zeus' message,{w=0.25} leaves.{w=0.5}"
    
    # Outside,{w=0.25} on island
    
    scene bg calypso island headland
    with fade
    
    play sound "waves.wav" loop
    
    "After her divine visitor has left,{w=0.25} Calypso seeks out Odysseus and finds him weeping,{w=0.25} as usual,{w=0.25} on the headland.{w=0.5}"
    
    caly "Grieve no longer,{w=0.25} Odysseus.{w=0.5} I am willing to send you home at long last.{w=0.5}"
    
    caly "Make for yourself a raft.{w=0.5} I shall provide you with supplies for your journey.{w=0.5}"
    
    odys "I don't believe you! This must be a trap.{w=0.5}"
    
    caly "I would never harm you.{w=0.5} Trust me.{w=0.5} I swear by the gods.{w=0.5}"
    
    stop sound fadeout 1.0
    
    # Calypso's home
    
    scene bg calypso home
    with fade
    
    "Calypso and Odysseus return to her home for the night and dine together.{w=0.5}"
    
    "Calypso,{w=0.25} saddened by Odysseus' imminent departure,{w=0.25} attempts to convince him to stay one last time.{w=0.5}"
    
    caly "Why on Earth would you choose to leave me for a mortal woman?"
    
    odys "It is indeed true,{w=0.25} that you are by far more beautiful than my wife.{w=0.5}"
    
    odys "However,{w=0.25} my heart still resides in my home in Ithaca.{w=0.5} I cannot abandon my home.{w=0.5}"
    
    # Change day,{w=0.25} outside,{w=0.25} on island
    
    scene bg black
    with fade
    
    "...{w=1.0}{nw}"
    
    scene bg calypso island beach
    with fade
    
    "In the morning,{w=0.25} Calypso had aided Odysseus in building his raft by supplying him with tools and timber.{w=0.5}"
    
    # Cycle days,{w=0.25} outside,{w=0.25} on island
    
    scene bg black
    with fade
    
    "...{w=1.0}{nw}"
    
    scene bg calypso island beach
    with fade
    
    "On the fifth day,{w=0.25} Calypso had filled his boat with supplies.{w=0.5}"
    
    "Well furnished for his voyage,{w=0.25} Odysseus eagerly sets sail.{w=0.5}"
    
    # Cycle days,{w=0.25} at sea
    
    scene bg black
    with fade
    
    "...{w=1.0}{nw}"
    
    play sound "waves.wav" loop
    
    scene bg sea calm
    with fade
    
    "On the eighteenth day of his journey,{w=0.25} Odysseus is spied by Poseidon,{w=0.25} Lord of the Seas.{w=0.5}"
    
    "Infuriated by the sight before him,{w=0.25} Poseidon churns the seas,{w=0.25} wind,{w=0.25} and thunderheads,{w=0.25} creating a terrible storm.{w=0.5}"
    
    stop sound fadeout 1.0
    
    # Storms
    
    scene bg sea storm
    with pixellate
    
    play sound "storm.wav" loop
    
    "Odysseus' small boat breaks apart and capsizes.{w=0.5}"
    
    "In the midst of the storm,{w=0.25} as Odysseus grapples helplessly to remains of his raft,{w=0.25} a sea nymph,{w=0.25} Leucothea,{w=0.25} finds him.{w=0.5}"
    
    stop sound fadeout 1.0
    
    # island
    
    scene bg phaeacia bushes
    with fade
    
    play sound "waves.wav" loop
    
    "With her help,{w=0.25} and the blessings of Athena,{w=0.25} Odysseus swims for days until he reaches land.{w=0.5}"
    
    "After staggering ashore,{w=0.25} he takes shelter beneath a pair of olive bushes,{w=0.25} where Athena blesses him with sleep.{w=0.5}"
    
    stop sound fadeout 1.0
    
    # Fade to black
    
    scene bg black
    with fade
    
    pause
    
    return