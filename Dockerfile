FROM docker.elastic.co/elasticsearch/elasticsearch:7.16.2

# Set some environment variables
ENV discovery.type=single-node
ENV cluster.name=demo-cluster
ENV bootstrap.memory_lock=true

# Expose the Elasticsearch REST API port
EXPOSE 9200
EXPOSE 9300