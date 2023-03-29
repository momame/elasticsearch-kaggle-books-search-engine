import csv
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
# es = Elasticsearch()
es = Elasticsearch(hosts=["http://localhost:9200/"])

# Define the index mapping
index_mapping = {
  "mappings": {
    "properties": {
      "id": { "type": "integer" },
      "title": { "type": "text" },
      "authors": { "type": "text" },
      "average_rating": { "type": "float" },
      "isbn": { "type": "keyword" },
      "isbn13": { "type": "keyword" },
      "num_pages": { "type": "integer" },
      "ratings_count": { "type": "integer" },
      "published_year":{"type":"integer"}
    }
  }
}

# delete the existing 'books' index if any
es.indices.delete(index='books', ignore=[400, 404], request_timeout=30)

# Create the index
es.indices.create(index="books", body=index_mapping)

# Index the data
with open("books.csv", newline="", encoding="utf-8") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    es.index(index="books", document=row)
