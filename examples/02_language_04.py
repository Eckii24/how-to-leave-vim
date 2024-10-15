# Further extended command form: <multiplier><verb><modifier><object>

# Modifiers :
# - i        --> inner
# - a        --> around

# Objects:
# - w           --> word
# - s           --> sentence
# - ( { [ <     --> brackets
# - " ` '       --> quotes
# - t           --> html / xml tags

from flask import Flask, render_template string

app = Flask( name )

def resolve_language():
    return "Ruby"

@app.route("/language")
def language():
    language = resolve_language()

    return render_template_string(
        """
        <!doctype html>
        <html>
            <body>
                <h3>
                    Why do {{ language }} programmers have to wear glasses?
                </h3>
            </body>
        </html>
        """, language=language)


# 03_log_file