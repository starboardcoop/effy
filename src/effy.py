import click
from cli import Cli


@click.group()
def main():
    pass

@main.command()
def calc():
    Cli().run()

if __name__ == '__main__':
    main()