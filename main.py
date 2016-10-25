#!/usr/bin/python

import queue
import threading
import click

@click.command()
@click.option('--count', '-c', default=1, help='number of greetings')
@click.argument('firstname')
@click.argument('lastname')
def hello(count, firstname, lastname):
    for x in range(count):
        print('hello %s %s!' % (firstname, lastname))

@click.group()
def cli():
    pass

@click.command()
def initdb():
    print('initialized the db')

@click.command()
def dropdb():
    print('destroyed the db')

cli.add_command(initdb)
cli.add_command(dropdb)





if __name__ == '__main__':
    hello()
    cli()