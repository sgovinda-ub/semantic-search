from rest import FlaskAppWrapper
from rest import action

def main():
    app = FlaskAppWrapper("test")
    app.add_endpoint('/action', 'action', action, methods=['GET'])
    app.run()
    print("Hello World!")



if __name__ == "__main__":
    main()