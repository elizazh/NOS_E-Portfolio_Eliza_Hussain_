import subprocess


def run_traceroute(domain):
    print(f"\nTraceroute for: {domain}")
    result = subprocess.run(["tracert", domain], capture_output=True, text=True)
    print(result.stdout)


domains = ["google.com", "openai.com", "bbc.co.uk"]
for domain in domains:
    run_traceroute(domain)
