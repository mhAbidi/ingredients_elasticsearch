# ingredients_elasticsearch


## Ingredients ElasticSearch Engine

Requirements:
1. ElasticSearch Server 7.12.1<br>
    Follow the instructions to download and setup from here: https://www.elastic.co/downloads/elasticsearch
2. Python 3.9.2<br>
3. Python packages: nltk, elasticsearch, pprint<br>


DataSet: ingredients_v1.csv<br>

The dataset was first cleaned, and refined features were extracted.
Follow data_cleaning_ingredient_features.ipynb file for the cleaning procecss.


Dataset Extracted: unique_ingredients.csv<br>

#### First run the ingredients_indexer.py to index the dataset into elasticsearch server.<br>
#### After indexing is done. Run the test.py to run search queries.
