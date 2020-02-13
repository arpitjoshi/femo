from neo4j import GraphDatabase


class Neo4j:
    def __init__(self):
        self.app = None
        self.driver = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.driver = GraphDatabase.driver('bolt:///graph_db')
        return self.driver

    def get_db(self):
        if not self.driver:
            return self.connect()
        else:
            return self.driver

