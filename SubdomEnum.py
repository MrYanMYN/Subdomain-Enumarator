import requests
import click
import time

@click.command()
@click.option('--domain', prompt="Enter the domain: " ,help='Enter a valid domain (without a subdomain)')
@click.option('--wordlist' ,prompt='Wordlist locaion: ' , help='enter the location of your preferred worlist')
@click.version_option(version="0.1.0")

def program(domain, wordlist):
    click.echo("Starting domain enumaration...")
    time.sleep(1)
    with open(wordlist , "r") as wl:
        for line in wl.readlines():
            word = line.strip("\n")
            try:
                req = requests.get(f'http://{word}.{domain}')
                if req.status_code == 200:
                    click.echo(f"Valid domain {word}.{domain}")
                else:
                    pass
            except:
                pass
        click.echo("""=========================
    Done
=========================""")

if __name__ == '__main__':
    program()