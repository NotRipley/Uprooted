# Uprooted
## Uprooted: Mathematically Correct Root
This is a repo exploring the game of root (and someday) creating models to play. 

### Load the Package
```
pip install -e .
```


```
```
### Structure
```
|-- utils/
    Files that will be utility functions and classes (e.g. cards class)
|-- input-data/
    Files where we can input and change the value of initialisation
|-- tests/
    Tests to check behaviour
    
Uprooted/
   ├── input_data/
   ├── tests/
   ├── src/
        |-- game-engine/
              |-- board.py
              |-- deck.py
              |-- errors.py 
   ├── LICENSE
   └── README

E.g. input all the cards as a json into ./inputs. Then use Deck.initialise_cards(filepath) to create the deck of cards.
```


### Conventions
* Singular terms preferentially i.e. "mouse"/"rabbit"/"fox"/"bird" in variable names
* Card descriptions in full lowercase with no special characters
* 

### Contributing
* Do not use AI to write code or fix methods. 
