def getdata():
    usejson = True #Set to False to use enviorment variables instead of config.json
    if usejson:
        import json
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print('config.json not found! Attempting to use .env instead...')
            usejson = False
    if not usejson:
        from dotenv import load_dotenv
        import os
        load_dotenv()
        #If you don't fill out the environment variables, it will return empty and probably crash, so make sure you fill them out!
        return {
            "Token": os.getenv('TOKEN'),
            "Prefix": os.getenv('PREFIX'),
            "Owners": os.getenv('OWNERS').split(','),
            "Database": {
                "Host": os.getenv('DB_HOST'),
                "User": os.getenv('DB_USER'),
                "Password": os.getenv('DB_PASSWORD'),
                "Database": os.getenv('DB_DATABASE')
        }
    }