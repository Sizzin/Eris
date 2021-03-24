import argparse

from methods import *

__version__ = '0.1'

parser = argparse.ArgumentParser(
    prog='eris',
    description='I\'m a Virtual Assistant for your Command Line.',
    epilog='Ask me anything!')

parser.version = __version__

parser.add_argument('-a', '--ask', nargs='*', help='Ask me anything and I\'ll give my best to answer you.', metavar='QUESTION')
parser.add_argument('-s', '--search', nargs='*', help='Make a Google Search', metavar='SEARCH TERM')
parser.add_argument('-yt', '--youtube', nargs='*', help='Search for videos in Youtube.', metavar='SEARCH TERM')
parser.add_argument('-c', '--calculate',  help='I\'ll calculate an arithmetic expression for you.', metavar='EXPRESSION')
parser.add_argument('-w', '--weather', nargs='*', help='I\'ll bring information about the weather in the city you choose.', metavar='CITY NAME')
parser.add_argument('-n', '--news', nargs='*', help='I\'ll look up for news about the term you type.', metavar='SEARCH TERM')
parser.add_argument('-v', '--version',  action='version', help='Show Eris\' current version.')


def main(args):
    _options = {
        'youtube': youtube_search,
        'search': google_search,
        'ask': ask,
        'calculate': calc,
        'weather': current_weather,
        'news': get_news
    }

    for key, arg in args.items():
        if arg:
            if type(arg) == list:
                arg = ' '.join(arg)
                _options[key](arg)
                return
            else:
                _options[key](arg)
                return

    print('For now, please try typing "-h" to see a list of things I can do to help you.')


if __name__ == '__main__':
    args = parser.parse_args()
    main(vars(args))
