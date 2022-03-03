import os

from cassandra.cluster import Cluster

keyspace = os.environ.get('CASSANDRA_KEYSPACE', 'yandex')

cluster = Cluster([os.environ.get('CASSANDRA_HOSTNAME', 'cassandra')])
session = cluster.connect(keyspace)

