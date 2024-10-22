# Simplest command form: <multiplier><motion>

# More motions commands:
# - f<char> F<char>    --> find next / previous <char>
# - t<char> T<char>    --> go in front of next / previous <char>
# - /<term> ?<term>    --> search <term> forward / backward


from flask import Flask

app = Flask( name )

@app. route("/")
def index():
    return """99 little bugs in the code,
              99 bugs in the code,
              1 bug fixed... compile again,
              100 little bugs in the code."""


# 02_language_03.py