"""Curl Command line argument builder."""
from easycli import Root, Argument as A


__version__ = '0.1.0'


CONTENTTYPES = {
    'none': '',
    'urlencoded': 'application/x-www-form-urlencoded',
    'multipart': 'multipart/form-data',
    'json': 'application/json',
    'plain': 'text/plain',
}


class CArgs(Root):
    """Main entrypoint."""

    __help__ = 'curl argument builder.'
    __arguments__ = [
        A('-c', '--contenttype',
          choices=CONTENTTYPES,
          help='HTTP content type.',
          ),
        A('-v', '--version', action='store_true'),
        A('-d', '--debug', action='store_true', default=False),
        A('url'),
        A('verb', nargs='?'),
        A('fields',
          metavar='[?]NAME=VALUE',
          default=[],
          nargs='*'
          )
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return
        items = []
        querystrings = []
        body = ''

        # Verb
        if args.verb:
            items.append(f'-X{args.verb.upper()}')

        # Fields
        for f in args.fields:
            if '=' not in f:
                body = ' '.join(args.fields)
                break

            if f[0] == '?':
                querystrings.append(f[1:])
            else:
                items.append(f'-F{f}')

        # Body
        if body:
#            if args.contenttype == 'json':
#                items.append(f'--data {body}')

            items.append(f'--data {body}')

        # Content Type
        if args.contenttype:
            ctype = CONTENTTYPES[args.contenttype]
            items.append(f'-H"Content-Type: {ctype}"')

        # Url
        if querystrings:
            items.append(f'{args.url}?{"&".join(querystrings)}')
        else:
            items.append(args.url)

        print(' '.join(items), end='\n' if args.debug else '')
