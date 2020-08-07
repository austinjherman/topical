# topical

This is an exeriment that I made to start learning about natural language processing. The program uses Latent Dirichlet Allocation (LDA) to extract common themes from a text document that you provide.

## Installation
Download the code in this repo and install the dependencies `pip install -r requirements.txt`

## Run the program
You need a text file with content to run through the program. You can get a good chunk of text to run through. I ran the first book of Game of Thrones through (~22k lines) without a problem.

When you have your text ready, then just run `python topical.py path/to/your/file.txt`.

## Options
- `-cwc, --create-word-cloud` will open a word cloud in pyplot
- `-gcw, --graph-common-words` will open up a graph of common words

## Example
```
Heart of Darkness by Joseph Conrad

Topic #0:
man time think ivory air lost face water

Topic #1:
looked great earth white left things oh night

Topic #2:
came long eyes saw manager day come near

Topic #3:
did don mr say right black old asked

Topic #4:
like good got look work tell took yes

Topic #5:
little heard going silence began believe end half

Topic #6:
know heart thing voice thought kind light wanted

Topic #7:
said men just away house stood seen talk

Topic #8:
kurtz darkness river station went way life suddenly

Topic #9:
head pilgrims looking word people couldn big words
```
