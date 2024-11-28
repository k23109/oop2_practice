import modules.SayHello as App  # Ensure the path is correct and `modules` is in your PYTHONPATH.

def run():
    app = App.SayHello("GitHub")
    app.say()

if __name__ == '__main__':  # Fixed spacing and syntax
    run()
