import random

nouns = ['apple', 'ball', 'cat', 'dog', 'elephant',
         'fish', 'goat', 'house', 'iceberg', 'jackal',
         'king', 'llama', 'monkey', 'nurse', 'octopus',
         'pie', 'queen', 'robot', 'snake', 'tofu',
         'unicorn', 'vampire', 'wumpus', 'x-ray', 'yak',
         'zebra']

verbs = ['ate', 'bit', 'caught', 'dropped', 'explained',
         'fed', 'grabbed', 'hacked', 'inked', 'jumped',
         'knitted', 'loved', 'made', 'nosed', 'oiled',
         'puffed', 'quit', 'rushed', 'stung', 'trapped',
         'uplifted', 'valued', 'wanted']

templates = [
        'Waiter! I found a {{noun}} in my {{noun}}!',
        'The {{noun}} {{verb}} the {{noun}}.',
        'If you {{verb}} the {{noun}}, '
        'the {{noun}} will get you.',
        "Let's go: the {{noun}} is {{verb}}.",
        'Colorless green {{noun}}s {{verb}} furiously.'
]


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0
    # Add a while loop here.
    temp = 0
    while index < len(template):
        if template[index: (8+index)] == "{{noun}}":
            output.append(template[temp:index])
            output.append(random.choice(nouns))
            index += 8
            temp = index
        elif template[index: (8+index)] == "{{verb}}":
            output.append(template[temp:index])
            output.append(random.choice(verbs))
            index += 8
            temp = index
        else :
            index +=1
    output.append(template[temp:])
    
    # After the loop has finished, join the output and return it.
    return "".join(output)

if __name__ == '__main__':
    print(silly_string(nouns, verbs, templates))
