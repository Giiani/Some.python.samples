TEXT={'agree':"""Yes, I agree. That sounds fine to me.""",
      'busy':"""Sorry, can we do this later this week or next wekk?""",
      'upsell':"""Would you consider making this a monthle donation?"""}

import sys,pyperclip

if len(sys.argv)<2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()
    
keyphrase= sys.argv[1] #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy()
    print('Text for '+ [keyphrase]+ ' copy to clipboard.')
else: 
    print('There is no text for ' + keyphrase)
    