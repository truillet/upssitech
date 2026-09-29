#!C:\Program Files\Python313\python.exe
"""An ivyprobe script for ivy-python
"""
import getopt
import os
import signal
import sys
import time
from typing import Any

from ivy.std_api import *

try:
    import readline
except ImportError:
    pass


IVYAPPNAME = 'pyivyprobe'

on_die_accepted = False


def info(fmt: str, *arg: Any) -> None:
    print(fmt % arg)


def usage(cmd: str) -> None:
    usage = '''Usage: %s [options] regexps
Options:
\t-b, --ivybus=bus    defines the Ivy bus to join; defaults to 127:2010
\t-h, --help          this message
\t-n, --name=<name>   changes the name of the agent, defaults to: '%s'
\t-r, --ready=<msg>   sets the ready message (use the empty string to disable it)
\t                    default is: '%s'
\t-s, --show-bindings show changes in other agents' bindings
\t-V, --version       prints the ivy release number
\t-v, --verbose       verbose mode (twice makes it even more verbose)

Type '.help' in ivyprobe for a list of available commands.'''
    print(usage % (os.path.basename(cmd), IVYAPPNAME, f"{IVYAPPNAME} Ready"))


def on_connection_change(agent: IvyClient, event: int) -> None:
    if event == IvyApplicationDisconnected:
        info('Ivy application %r has disconnected', agent)
    else:
        info('Ivy application %r has connected', agent)
    apps = IvyGetApplicationList()
    info(
        'Ivy applications currently on the bus (count: %i): %s',
        len(apps),
        ','.join(apps),
    )


def on_die(agent: IvyClient, _id: int) -> None:
    info('Received the order to die from %r with id = %d', agent, _id)
    global on_die_accepted
    on_die_accepted = True
    # will interrupt the raw_input()/input() in the main loop, below
    os.kill(os.getpid(), signal.SIGINT)


def on_msg(agent: IvyClient, *arg: Any) -> None:
    info('Received from %r: %r', agent, arg and arg or '<no args>')


def on_direct_msg(agent: IvyClient, num_id: int, msg: str) -> None:
    info('%r sent a direct message, id=%s, message=%r', agent, num_id, msg)


def on_regexp_change(agent: IvyClient, event: int, regexp_id: int, regexp: str) -> None:
    from ivy.ivy import IvyRegexpAdded

    info(
        '%r %s regexp id=%s: %r',
        agent,
        event == IvyRegexpAdded and 'added' or 'removed',
        regexp_id,
        regexp,
    )


def on_pong(agent: IvyClient, delta: float) -> None:
    info('%s answered to ping in %fs', agent, delta)


def _set_showbind(showbind: bool) -> None:
    if showbind:
        IvyBindRegexpChange(on_regexp_change)
        info("Changes in applications' bindings are shown")
    else:
        IvyBindRegexpChange(void_function)
        info("Changes in applications' bindings are hidden")


if __name__ == '__main__':
    import logging

    from ivy.ivy import ivylogger

    ivybus = ''
    readymsg = None
    verbose = 0
    showbind = False
    toggle_showbind = False

    ivylogger.setLevel(logging.WARN)

    try:
        optlist, left_args = getopt.getopt(
            sys.argv[1:],
            'hb:n:r:Vvs',
            ['help', 'ivybus=', 'name=', 'ready=', 'version', 'verbose', 'show-bindings'],
        )
    except getopt.GetoptError:
        usage(sys.argv[0])
        sys.exit(2)
    for opt, arg in optlist:
        if opt in ('-h', '--help'):
            usage(sys.argv[0])
            sys.exit()
        elif opt in ('-b', '--ivybus'):
            ivybus = arg
        elif opt in ('-V', '--version'):
            import ivy

            info('ivyprobe supplied with ivy-python library version%s', ivy.__version__)
            sys.exit()
        elif opt in ('-v', '--verbose'):
            if not verbose:
                ivylogger.setLevel(logging.INFO)
                verbose += 1
            elif verbose == 1:
                ivylogger.setLevel(logging.DEBUG)
                verbose += 1
            else:
                if hasattr(logging, 'TRACE'):
                    ivylogger.setLevel(logging.TRACE)
        elif opt in ('-n', '--name'):
            IVYAPPNAME = arg
        elif opt in ('-r', '--ready'):
            readymsg = arg
        elif opt in ('-s', '--showbind'):
            showbind = True

    if readymsg is None:
        readymsg = '%s Ready' % IVYAPPNAME

    info('Broadcasting on %s', ivybus or os.environ.get('IVYBUS') or 'ivydefault')

    # initialising the bus
    IvyInit(
        IVYAPPNAME,            # application name for Ivy
        readymsg,              # ready message
        0,                     # parameter ignored
        on_connection_change,  # handler called on connection/disconnection
        on_die,                # handler called when a die msg is received
    )

    _set_showbind(showbind)

    # starting the bus
    IvyStart(ivybus)

    # bind the supplied regexps
    for regexp in left_args:
        IvyBindMsg(on_msg, regexp)

    # direct msg
    IvyBindDirectMsg(on_direct_msg)

    # pong
    IvyBindPong(on_pong)

    # Ok, time to go
    time.sleep(0.5)
    info('Go ahead! (type .help for help on commands)')
    while 1:
        if toggle_showbind:
            toggle_showbind = False
            showbind = not showbind
            _set_showbind(showbind)

        try:
            msg = input('')

        except (EOFError, KeyboardInterrupt):
            msg = '.quit'

        if msg == '.help':
            info(
                """Available commands:
        .bind 'regexp'              - add a msg to receive. The displayed index
                                                     can be supplied to .remove
        .die appname                - send die msg to appname
        .die-all-yes-i-am-sure      - send die msg to all applications
        .direct appname id arg      - send direct msg to appname
        .help                       - print this message
        .error appname id err_msg   - send an error msg to an appname
        .ping appname               - send a ping to an appname
        .quit                       - terminate this application
        .remove idx                 - remove a binding (see .bind, .regexps)
        .regexps                    - show current bindings
        .regexps appname            - show all bindings registered for appname
        .showbind                   - show/hide bindings (toggle)
        .where appname              - print the host for appname
        .who                        - display the names of all applications on
                                                                       the bus

Everything that is not a (valid) command is interpreted as a message and sent
to the appropriate applications on the bus.
"""
            )

        elif msg[:5] == '.bind':
            regexp = msg[6:]
            if not regexp:
                print('Error: missing argument')
            info('Bound regexp, id: %d', IvyBindMsg(on_msg, regexp))

        elif msg == '.die-all-yes-i-am-sure':
            app_names = IvyGetApplicationList()
            if not app_names:
                info('No application on the bus')
                continue

            for app_name in IvyGetApplicationList():
                app = IvyGetApplication(app_name)
                if not app:
                    info('No application %r' % app_name)
                else:
                    IvySendDieMsg(app)

        elif msg[:4] == '.die':
            app_name = msg[5:]
            app = IvyGetApplication(app_name)
            if app is None:
                info('No application named %r', app_name)
                continue
            IvySendDieMsg(app)

        elif msg[:7] == '.direct':
            try:
                app_name, num_s, arg = msg[8:].split(' ', 2)
            except ValueError:
                print('Error: wrong number of parameters')
                continue
            try:
                num = int(num_s)
            except ValueError:
                print('Error: the id must be an integer')
                continue
            app = IvyGetApplication(app_name)
            if app is None:
                info('No application named %r', app_name)
                continue

            IvySendDirectMsg(app, num, arg)

        elif msg[:6] == '.error':
            try:
                app_name, num_s, err_msg = msg[7:].split(' ', 2)
            except ValueError:
                print('Error: wrong number of parameters')
                continue
            try:
                num = int(num_s)
            except ValueError:
                print('Error: the id must be an integer')
                continue

            app = IvyGetApplication(app_name)
            if app is None:
                info('No application named %r', app_name)
                continue

            IvySendError(app, num, err_msg)

        elif msg[:7] == '.remove':
            try:
                regexp_id = int(msg[8:])
                info('Removed %d:%r', regexp_id, IvyUnbindMsg(regexp_id))
            except KeyError:
                info('No such binding')
            except ValueError:
                info('Error: expected an integer')

        elif msg[:5] == '.ping':
            app_name = msg[6:]
            app = IvyGetApplication(app_name)
            if app is None:
                info("No application named %r", app_name)
                continue
            IvySendPing(app)
            info('Sent PING')

        elif msg == '.regexps':
            from ivy import std_api

            info(
                'Our subscriptions: %s',
                ', '.join(
                    [
                        "%s:'%s'" % (_id, regexp)
                        for _id, regexp in IvyGetMessages()
                    ]
                ),
            )

        elif msg[:9] == '.regexps ':
            app_name = msg[9:]
            app = IvyGetApplication(app_name)
            if app is None:
                info("Error: no application found with name %r" % app_name)
            else:
                info(
                    'Subscriptions of %r: %s',
                    app_name,
                    ', '.join(
                        [
                            "%s:'%s'" % (_id, regexp)
                            for _id, regexp in IvyGetApplicationMessages(app)
                        ]
                    ),
                )

        elif msg[:9] == '.showbind':
            toggle_showbind = True

        elif msg == '.quit':
            # Do not IvyStop if we were already notified that the
            # agent is about to die
            if not on_die_accepted:
                IvyStop()
            break

        elif msg[:6] == '.where':
            app_name = msg[7:]
            app = IvyGetApplication(app_name)
            if app is None:
                info('No application named %r', app)
                continue
            info('Application %r on %s:%s', app_name, app.ip, app.port)

        elif msg == '.who':
            print(IvyGetApplicationList())

        else:
            info('Sent to %s peers' % IvySendMsg(msg))
