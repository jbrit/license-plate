import click
import db

def validate_license(license):
    if len(license) != 8:
        raise click.BadParameter('License must be 8 characters long')
    if not license[0:2].isalpha():
        raise click.BadParameter('License must start with two letter')
    if not license[-2:].isalpha(): 
        raise click.BadParameter('License must end with two letter')
    if not license[3:-3].isdigit():
        raise click.BadParameter('License must have numbers in between')
   


@click.group()
def cli():
    pass

@cli.command()
@click.argument('license')
def addlicense(license):
    validate_license(license)
    click.echo(f"Adding license {license}")
    db.insert_license(license)


@cli.command()
@click.argument('license')
def removelicense(license):
    validate_license(license)
    click.echo(f"Removing license {license}")
    db.delete_license(license)

@cli.command()
def getlicenses():
    click.echo(db.read_license())


if __name__ == '__main__':
    cli()