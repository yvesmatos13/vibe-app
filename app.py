from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    page_content = '''
    <!doctype html>
    <html lang="pt-BR">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Vibe Tecnologia</title>
        <style>
          body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
          }
          iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
          }
        </style>
      </head>
      <body>
        <iframe src="https://www.vibetecnologia.com/"></iframe>
      </body>
    </html>
    '''
    return render_template_string(page_content)

if __name__ == '__main__':
    app.run(debug=True)
