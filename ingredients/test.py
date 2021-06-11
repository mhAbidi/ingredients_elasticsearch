from nltk.corpus import stopwords
import elasticsearch
import nltk
import os
import pprint
os.system('cls')
print("HERE IS YOUR RESULT\n\n")
client = elasticsearch.Elasticsearch()
word_list = "ppricot".split()
remove_words = [
    "tablespoon",
    "tbsp",
    "gram",
    "gms",
    "gm",
    "grams",
    "teaspoon",
    "half",
    "full",
    "dozen",
    "dz",
    "tsp",
    "cup",
    "big",
    ]
for word in remove_words:
    try:
        word_list.remove(word)
    except: pass
filtered_words = [word for word in word_list if word not in stopwords.words('english')]
filtered_phrase = ""
for word in filtered_words:
    filtered_phrase+=word+" "
print("Filtered Words::", filtered_phrase)


#for f in filtered_words:


query = {
        "query": {
            "match": {
                "title": {
                    "query": filtered_phrase,
                    "fuzziness": 1
                    }
            }
        }
    }
ret = client.search(body=query, index="nin_v3")
#print(ret["hits"]["hits"])
#ret = set(ret)
#print(ret)
hits = ret["hits"]["hits"]
print("\n Results::::\n")
result = []
for i in hits:
        result.append((i["_source"]["title"], i["_score"]))
        #print((i["_source"]["title"], i["_score"]))
#print(len(result))
result = set(result)
result = list(result)
result.sort(key=lambda x:x[1],reverse=True)
print(result[0])
result.pop(0)
print("\n\nSuggested Results:\n")
pprint.pprint(result)





