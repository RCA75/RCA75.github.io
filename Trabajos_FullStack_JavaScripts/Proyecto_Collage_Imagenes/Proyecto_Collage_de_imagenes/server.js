const express = require('express')
//Integración de express-fileupload
const expressFileUpload = require('express-fileupload')
const fs = require('fs')

const app = express()
const config = {
    limits: {fileSize: 5000000}, //Definición del limite de carga
    abortOnLimit: true,
    responseOnLimit: "Se ha sobrepasado el límite de tamaño de imagen."
}
app.use(expressFileUpload(config))
app.use(express.json())
app.use("/imgs", express.static(__dirname + "/imgs"))

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/formulario.html")
})

app.get("/collage", (req, res) => {
    res.sendFile(__dirname + "/collage.html")
})
//Creación Ruta POST /imagen que recibe y almacena una imagen en carpeta publica del servidor
app.post("/imagen", (req, res) => {
    const {posicion} = req.body
    const {target_file} = req.files 
    target_file.mv(`${__dirname}/imgs/imagen-${posicion}.jpg`, (err) => {
        res.sendFile(__dirname + "/collage.html")
    })
})
//Creación Ruta GET /deleteImg/:nombre que recibe como parametro el nombre de la imagen y la elimina de carpeta
app.get("/deleteImg/:imagen", (req, res) => {
    const {imagen} = req.params
    fs.unlinkSync(__dirname + `/imgs/${imagen}`)
    res.redirect("/collage")
})

app.listen(3000)
console.log("Server Online Port:3000");

