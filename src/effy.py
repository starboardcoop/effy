import click
from cli import Cli


@click.group()
def main():
    """A simple app for calculating someone's contribution to a project."""
    pass

@main.command()
def calc():
    """Starts the app."""
    Cli().run()

if __name__ == '__main__':
    main()