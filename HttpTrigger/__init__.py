import logging

def main(req) -> dict:
    logging.info("Processing HTTP request...")
    return {
        "status": 200,
        "body": "Hello, World!"
    }
