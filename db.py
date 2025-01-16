import mongoengine
from mongoengine.connection import get_db
from mongoengine import disconnect


class DatabaseConnection:
    """
    A class to manage the MongoDB connection using MongoEngine.
    """
    def __init__(self, db_name: str, host: str = "localhost", port: int = 27017, username: str = None, password: str = None, authentication_source: str = "admin"):
        """
        Initialize the database connection.
        
        :param db_name: Name of the database.
        :param host: MongoDB server address (default: localhost).
        :param port: MongoDB server port (default: 27017).
        :param username: Username for authentication (optional).
        :param password: Password for authentication (optional).
        :param authentication_source: The database to authenticate against (default: admin).
        """
        self.db_name = db_name
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.authentication_source = authentication_source
        self.connection = None

    def connect(self):
        """
        Establish a connection to the MongoDB database.
        """
        self.connection = mongoengine.connect(
            db=self.db_name,
            host=self.host,
            port=self.port,
        )
        
        print(f"Connected to MongoDB database: {self.db_name}")

    def disconnect(self):
        """
        Close the MongoDB connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

            disconnect()
            
            print(f"Disconnected from MongoDB database: {self.db_name}")

    def get_database(self):
        """
        Get the MongoDB database instance.
        :return: The database instance.
        """
        if self.connection:
            return get_db()
        raise ConnectionError("Database is not connected. Call connect() first.")
