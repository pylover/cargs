"""Test CArgs.

http home.light set <body>
http home.light set foo=1 bar="bar baz" qux=@path/to/file.ext
http home.light set ?foo=bar ?baz=qux
http home.light set -c json -- {foo: "bar"}
"""

import sys

from bddcli import Given, when, stdout, status, stderr, Application, given


app = Application('cargs', 'cargs:CArgs.quickstart')


def test_contenttypes():
    with Given(app, 'example.com'):
        assert status == 0
        assert stdout == 'example.com'

        when(given + '-cplain')
        assert status == 0
        assert stdout == '-H"Content-Type: text/plain" example.com'

        when(given + '-cjson')
        assert status == 0
        assert stdout == '-H"Content-Type: application/json" example.com'

        when(given + '-cmultipart')
        assert status == 0
        assert stdout == '-H"Content-Type: multipart/form-data" example.com'

        when(given + '-curlencoded')
        assert status == 0
        assert stdout == \
            '-H"Content-Type: application/x-www-form-urlencoded" example.com'


def test_querystring():
    with Given(app, 'example.com'):
        assert status == 0
        assert stdout == 'example.com'

        when(given + 'POST ?foo=bar')
        assert status == 0
        assert stdout == '-XPOST example.com?foo=bar'

        when(given + 'POST ?foo=bar ?baz=qux')
        assert status == 0
        assert stdout == '-XPOST example.com?foo=bar&baz=qux'


def test_verb():
    with Given(app, 'example.com'):
        assert status == 0
        assert stdout == 'example.com'

        when(given + 'POST')
        assert status == 0
        assert stdout == '-XPOST example.com'


def test_plainbody():
    with Given(app, 'example.com post foo bar'):
        assert status == 0
        assert stdout == \
            '-XPOST --data "foo bar" example.com'


def test_multipart():
    with Given(app, 'example.com'):
        assert status == 0
        assert stdout == 'example.com'

        when('example.com post foo=@bar.txt')
        assert status == 0
        assert stdout == \
            '-XPOST -Ffoo=@bar.txt example.com'

        when(given + 'POST foo=bar')
        assert status == 0
        assert stdout == '-XPOST -Ffoo=bar example.com'

        when(given + 'POST foo=bar baz=qux')
        assert status == 0
        assert stdout == '-XPOST -Ffoo=bar -Fbaz=qux example.com'
