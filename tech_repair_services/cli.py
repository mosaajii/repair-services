"""Console script for tech_repair_services."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for tech_repair_services."""
    click.echo("Replace this message by putting your code into "
               "tech_repair_services.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
