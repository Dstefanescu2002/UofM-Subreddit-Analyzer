from department_names import DEPARTMENT_NAMES
import re

class EntityExtractor:
        
    def extract(self, text: str) -> list:
        text = text.upper()
        dn_text = '|'.join(DEPARTMENT_NAMES)
        pattern = re.compile(f'\\b({dn_text}).?.?([1-9]\d{{2}})\\b')
        re_output = pattern.findall(text)
        return list(set([' '.join(x) for x in re_output]))

    def batch_extract(self, posts: list) -> list:
        entities = []
        for post in posts:
            entities.append(self.extract(post))
        return entities
    
    def calculate_accuracy(self, pred_entities: list, correct_entities: list) -> float:
        if len(pred_entities) != len(correct_entities):
            print ("Prediction and correct label lists are of different size.")
            return -1
        total_correct = 0
        for i in range(len(correct_entities)):
            f_correct_entity = correct_entities[i].replace('(', '').replace(')', '').split(', ')
            f_correct_entity = [i for i in f_correct_entity if i]
            correct = True
            if len(f_correct_entity) == len(pred_entities[i]):
                for j in range(len(f_correct_entity)):
                    if f_correct_entity[j].upper() != pred_entities[i][j].upper():
                        correct = False
            else:
               print(f_correct_entity, pred_entities[i])
               correct = False
            total_correct += correct
        return total_correct/len(correct_entities)
