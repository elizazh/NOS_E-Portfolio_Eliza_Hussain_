import subprocess


def tracert(domain):
    try:
        result = subprocess.run(["tracert", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("tracert command not found. Make sure it's available on your system.")
    except Exception as e:
        print(f"An error occurred: {e}")


domain = input("https://www.facebook.com/")
tracert(domain)
