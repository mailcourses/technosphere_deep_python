#! /usr/bin/env python

from faker import Faker
from elasticsearch import Elasticsearch

def main():
    es_client = Elasticsearch()
    doc = {
        "author": "Антон Кухтичев"
    }
    index_name = 'test-index-msu'
    fake = Faker(locale="ru_RU")
    for num in range(10):
        doc['quote'] = fake.sentence(nb_words=5)
        doc['address'] = fake.address()
        res = es_client.index(index=index_name, id=num, body=doc)
    res = es_client.search(index=index_name, body={"query": {"match_all": {}}})
    print(res)

if __name__ == "__main__":
    main()
