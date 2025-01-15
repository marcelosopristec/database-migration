from scripts.migration import migration


def main():
    """
    Entry point for the database migration script.

    This function establishes a connection to the MongoDB database and 
    performs schema type migration operations.
    """

    migration()


if __name__ == "__main__":
    main()