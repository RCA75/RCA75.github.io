<template>
    <div>
        <h1>Editando el curso : {{ cursos.nombre }}</h1>
        <v-form @submit.prevent="updateCurso(item)" ref="form" v-model="valid" lazy-validation>
            <v-text-field v-model="cursos.nombre" label="Nombre del curso" type="name" :counter="40" required></v-text-field>
            <v-text-field v-model="cursos.url" label="URL de imagen del curso" type="url" required></v-text-field>
            <v-text-field v-model="cursos.cupos" label="Cupos del curso" type="number" required></v-text-field>
            <v-text-field v-model="cursos.inscritos" label="Inscritos en el curso" type="number" required></v-text-field>
            <v-text-field v-model="cursos.duracion" label="Duración del curso" type="text" required></v-text-field>
            <v-text-field v-model="cursos.costo" label="Costo del curso" type="number" required></v-text-field>
            <v-text-field v-model="cursos.codigo" label="Código del curso" type="text" required></v-text-field>
            <v-textarea v-model="cursos.descripcion" filled label="Descripción del curso" required auto-grow></v-textarea>
            <v-text-field v-model="cursos.registro" label="Fecha de registro" type="date" required></v-text-field>
            
            <v-container class="px-0" fluid>
                <v-switch v-model="cursos.estado" :label="`¿Completado? :`"></v-switch>
            </v-container>
            <v-checkbox v-model="checkbox" :rules="[v => !!v || '¡Necesita validar su respuesta!']"
                label="Marque para validar" required></v-checkbox>
            <v-btn :disabled="!valid" color="success" class="mr-4" type="submit">
                Actualizar
            </v-btn>
            <v-btn color="error" class="mr-4" @click="reset">
                Limpiar formulario
            </v-btn>
            <router-link to="/administracion">
                <v-btn color="primary">
                    Regresar
                </v-btn>
            </router-link>
        </v-form>
    </div>
</template>

<script>
import { doc, getDoc, setDoc } from 'firebase/firestore'
import cursosCollection from '../firestore'
    export default {
        data: () => ({
            valid: true,
            cursos: {
                nombre: null,
                url: null,
                cupos: null,
                inscritos: null,
                duracion: null,
                costo: null,
                codigo: null,
                descripcion: null,
                registro: null,
                estado: false,
            },
            checkbox: false,
            id: null,
            docRef: null,
        }
        ),
        methods: {
            Actualizar() {
                this.$refs.form.validate()
            },
            reset() {
                this.$refs.form.reset()
            },
            async getCurso() {
                let cursoRef = doc(cursosCollection, this.id)
                this.docRef = cursoRef
                let ref = await getDoc(this.docRef)
                let curso = ref.data()
                console.log(curso)
                this.cursos.nombre = curso.nombre
                this.cursos.url = curso.url
                this.cursos.cupos = curso.cupos
                this.cursos.inscritos = curso.inscritos
                this.cursos.duracion = curso.duracion
                this.cursos.costo = curso.costo
                this.cursos.codigo = curso.nombre
                this.cursos.descripcion = curso.descripcion
                this.cursos.registro = curso.nombre
                this.cursos.estado = curso.estado
            },
            async updateCurso(){
                await setDoc(this.docRef, this.cursos)
                alert('Curso Actualizado')
                this.$router.push("/cursos")
            }
        },
        created() {
            let cursoId = this.$route.params.id
            this.id = cursoId
            this.getCurso()
        },
    }
</script>