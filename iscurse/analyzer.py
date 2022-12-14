import json
import os
PATH = './data/AFINN-pt.json'

AFINN = json.load(open(PATH))


class Analyzer:
    def __init__(self):
        self.score = 0
        self.text = ''
        self.afinn = AFINN
    
    def get_score(self):
        return self.score

    def get_text(self):
        return self.text
    
    def get_emoji(self):
        if self.score > 0:
            return ':)'
        elif self.score < 0:
            return ':('
        else:
            return ':|'
        
    def get_binary(self):
        if self.score > 0:
            return 1
        else:
            return 0
    
    
    def get_sentiment(self):
        if self.score > 0:
            return 'positive'
        elif self.score < 0:
            return 'negative'
        else:
            return 'neutral'
    
    def analyse(self, text):
        self.text = text
        self.score = self._sentiment(self.text)
    
    def get_zero_to_five(self):
        if self.score < -3 and self.score >= -5:
            return 1
        elif self.score > -3 and self.score <= -1:
            return 2
        elif self.score > -1 and self.score <= 1:
            return 3
        elif self.score > 1 and self.score <= 3:
            return 4
        elif self.score > 3 and self.score <= 5:
            return 5
        else:
            print('Error: score out of range')
            print(self.score)

    def get_zero_to_ten(self):
        return self.get_zero_to_five() * 2
            
    def _load_data(self):
        here = os.path.abspath(os.path.dirname(__file__))
        afinn = json.load(open(os.path.join(here, 'data','AFINN-pt.json')))
        return afinn

    def _sentiment(self,text):
        score = []
        point  = 0
        final_score = 0
        res = [self.afinn[sent] for sent in self.afinn.keys() if sent in text]
        for sent in self.afinn.keys():
            if sent in text:
                point += 1
                score.append(self.afinn[sent])
        
    
        score = sum(score)
        final_score = score/point if point > 0 else 0

        return final_score
    