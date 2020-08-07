import sys
import argparse


class cli:

    class colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def __init__(self, cli_args):
        parser = argparse.ArgumentParser(description='Pull themes out of text.')

        parser.add_argument('infile', type=str, help='Specify a file to read from.')

        parser.add_argument('-od', '--outdir',
                            help='Specify a directory to store output files.')

        parser.add_argument('-cwc', '--create-wordcloud', action='store_true',
                            help='Do you want to make a wordcloud?')

        parser.add_argument('-gcw', '--graph-common-words', action="store_true",
                            help='Do you want to graph common words?')

        parser.add_argument('-ksw', '--keep-stop-words', action="store_true",
                            help='Do you want to graph common words?')

        self.args = parser.parse_args(cli_args)

    def validate_args(self):
        self.validate_infile()


cli = cli(sys.argv[1:])
cli.args.outdir if not cli.args.outdir else cli.args.outdir.strip('/')
