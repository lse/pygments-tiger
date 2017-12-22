from pygments.lexer import RegexLexer

class TigerLexer(RegexLexer):
    name = 'Tiger'
    aliases = ['tiger']
    filenames = ['*.tc', '*.tiger']
