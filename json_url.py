import random
import urllib.request, json 


class VerbsHandler:
    def __init__(self):
        with urllib.request.urlopen("https://raw.githubusercontent.com/WithEnglishWeCan/generated-english-irregular-verbs/master/irregular.verbs.build.json") as url:
            self.data = json.load(url)
    
    def random_verbs(self):
        sample = random.choices(list(self.data.items()), k = 5)

        response = 'Here are the words to remember for today: \n \n'

        for verb, verb_list in sample:
            response += f"{verb} | {', '.join(verb_list[0]['2'])} | {', '.join(verb_list[0]['3'])}   meaning: {', '.join(verb_list[0]['description'])} \n"
    
        return response
