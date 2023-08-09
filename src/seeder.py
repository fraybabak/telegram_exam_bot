from di import contextService, binaryQuestionService

import json


# with open("src/seeds/contexts.json") as f:
    
#     contexts = json.load(f)

#     for context in contexts:
#         contextService.create(context['description'], context['title'])
    

with open("src/seeds/questions.json") as f:
        
        questions = json.load(f)
        for context in questions.keys():

            context_id = contextService.find_by_title(context).id
            for question in questions[context]:
                jesus = binaryQuestionService.create(question=question['question'],answer=True, rating=question['rating'],context_id=context_id)
                print(jesus)