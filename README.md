# digiwild

## Docker

```
 docker build -t ordes/digiwild:swallow . 
```

```
docker run -it -p 7860:7860 ordes/digiwild:swallow
```

## Needs

- Camera with multiples pictures?
- Uploading of pics
- GPS location
- Comments
- Symptomps selection (Dropdown)

## ornitho.ch schema

After selecting the species

```
- dead
- wounded

- Collision with a means of transport
    - road vehicle
        - road type (Options)
            - highway
            - main road
            - secondary road
            - local road/path/trail
            - parking lot
            - other
            - unknown
        - infrastructure number (Open)
    - train
        - infrastructure number (Open)
    - aircraft
    - boat
    - other
    - unknown
- Destruction / Deliberatly removed
    - hunting
        - shooting
        - bow
        - falconry
        -  hounds hunting
        - digging up
        - other
        - unknown
    - trap
        - killing trap
        - pole trap
        - trap cage
        - corvids nasse
        - net
        - cage trap
        - fall-trap
        - glue trap
        - insect trap
        - other
        - unknown
    - poisoning
    - removal or direct capture
        - gassing
        - raptor captured at nest
        - brood destruction
        - traffic/trade
        - capture accident
        - scientific sample
        - other
        - unknown
    - fishing
        - drowned/tangled
        - beached with capture indications
        - other
        - unknown
    - other
    - unkown 
- Indirect destruction 
    - pylone and electric grid
        - object (Options)
            - electric line
            - pole/pylon
            - other
            - unknown
        - cause (Options)
            - collision
            - electrocution
            - unknown
    - windfarm
    - other collision
        - Object (Options)
            - window
            - building
            - lighthouse
            - cable
            - wire fence/barbed wire
            - other crash
            - unknown
    - fall
        - Object (Options)
            - chimney
            - empty pole
            - hole/well
            - other
            - unknown
    - development work
        - Type (Options)
            - transport infrastructure
            - building
            - other
            - unknown
    - pollution / contamination
        - Type (Options)
            - oil pollution
            - chemical pollution
            - heavy metals
            - light
            - noise
            - plastic ingestion
            - other
            - unknown
    - agricultural net protection
    - vegetal / forest work
        - Type (Options)
            - clearing/mowing/plowing
            - tree felling/pruning
            - other
            - unknown
    - other
    - unknown
- Natural cause
    - predation
        - responsible (Options)
            - cat
            - dog
            - rooster/hen
            - other domestic animal
            - wild birds
            - wild mammal
            - other
            - unknown
    - weather
        - Type (Options)
            - cold wave
            - drought
            - hail
            - lightening
            - storm
            - other
            - unknown
    - natural disaster
        - Type (Options)
            - fire
            - avalanche
            - rock fall
            - mudslide
            - volcanic eruption/ashes
            - other
            - unknown
    - nest fall
    - strading due to exhaustion
    - disease/parasite
    - accidental drowing
        - Container (Options)
            - drinking trough
            - pool
            - storm pool
            - irrigation pool
            - natural pool
            - flood
            - other container
            - unknown
    - other
    - unknown
- Unknown 

- Event follow-up
    - Animal collected (Options)
        - Yes
        - No
    - Recipient (Options)
        - Veterinary
        - Care center
        - Local Museum
        - National Museum
        - Other
    - Radiography (Options)
        - Yes
        - No
        - Unknown
    - Given answer (Options)
        - Nothing
        - Complaint against X
        - Complaint
        - Police call
        - Discussion with the speaker
        - Press release
        - Unknown
    - Name of recipient / museum (Open)
    - Collection reference (Open)
```


