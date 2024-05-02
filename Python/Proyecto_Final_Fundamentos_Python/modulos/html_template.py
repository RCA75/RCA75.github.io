# Autor: Reinaldo Carocca

from string import Template

#Desarrollo del Templates index.html
index = Template(
    '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <title>Aves de Chile</title>
    </head>
    <body>
        <div class="container">
            <h1 style="text-align: center;">Aves de Chile</h1>
            <div class="row">
                $card
            </div>
        </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
    '''
)

#Desarrollo del Template para las Cards
card = Template ('''
                <div class="col-12 col-md-3 p-2">
                    <div class="card">
                        <img src=$img_large class="card-img-top" alt="$name_en">
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item">Nombre: $name_es</li>
                            <li class="list-group-item">Name: $name_en</li>
                        </ul>
                    </div>
                </div>
                '''
                )

if __name__ == '__main__' :
    pass