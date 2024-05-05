from testcontainers.mysql import MySqlContainer
from testcontainers.elasticsearch import ElasticSearchContainer

def test_search():
    with ElasticSearchContainer() as es:
        connection_url = es.get_url()   
        print(connection_url)