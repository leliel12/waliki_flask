from flask.signals import Namespace

wiki_signals = Namespace()

page_saved = wiki_signals.signal('page-saved')
pre_display = wiki_signals.signal('pre-display')
