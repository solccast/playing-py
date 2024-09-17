from flask import render_template

def not_found_error(e):
    kwargs = {
        "error_name": "404 Not found error",
        "error_description": "La url a la que quiere acceder no existe"
    }

    return render_template("not_found.html", **kwargs), 404