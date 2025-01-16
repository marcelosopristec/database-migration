import asyncio

from db import DatabaseConnection
from scripts.frameworks_types_assets import MigrationAssetManagerSchemas


def connect_asset_manager(old_version: bool = False):
    database_name = "old_asset_manager" if old_version is True else "asset_manager"

    datagerry_connection = DatabaseConnection(
        db_name=database_name,
        host="localhost",
        port=27017,
    )

    datagerry_connection.connect()

    return datagerry_connection

def migration():
    """
    Entry point for the database migration script.

    This function establishes a connection to the MongoDB database and 
    performs schema type migration operations.

    Steps:
    1. Creates a `DatabaseConnection` object with the specified database
       name, host, and port for MongoDB.
    2. Connects to the database using the `connect()` method of the 
       `DatabaseConnection` object.
    3. Initializes the `MigrationAssetManagerSchemas` class to handle 
       schema type migration logic.
    4. Executes the `find_schema_type_and_save()` method to retrieve 
       schema types from the source database and save them as needed.

    Usage:
        Run this script directly to start the migration process:
        ```
        python main.py
        ```

    Dependencies:
        - `db.DatabaseConnection`: Handles the database connection logic.
        - `scripts.migration.MigrationAssetManagerSchemas`: Contains the 
          logic for schema type migration.

    Note:
        - Ensure that the database server is running and accessible at 
          the specified `host` and `port`.
        - Replace `old_asset_manager` with the actual database name if different.

    """

    migration_types = []

    datagerry_connection = connect_asset_manager(True)

    migration_asset_manager = MigrationAssetManagerSchemas()
    migration_asset_manager.save_framework_type()
    migration_asset_manager.generate_documents()

    datagerry_connection.disconnect()

    # asset_manager_connection = connect_asset_manager()
    # migration_asset_manager.save_documents()
    # asset_manager_connection.disconnect()

