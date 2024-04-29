<template>
    <v-form ref="form" v-model="valid" lazy-validation data-app>
        <v-text-field v-model="user.email" :rules="emailRules" label="E-mail" required></v-text-field>

        <v-text-field v-model="user.password" :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, rules.min]"
            :type="show ? 'text' : 'password'" name="input-10-2" label="Contraseña" hint="At least 8 characters" 
            class="input-group--focused" @click:append="show = !show"></v-text-field>

        <v-btn :disabled="!valid" color="success" class="mr-4" @click="signIn()">
            Enviar
        </v-btn>

        <v-btn class="mr-4" color="error" @click="reset">
            Limpiar formulario
        </v-btn>
    </v-form>
</template>

<script>
import { mapMutations } from 'vuex';
import {signInWithEmailAndPassword} from "firebase/auth";
import auth from '../authentification'
export default {
    data() {
        return {
            user: {
                email: "",
                password: ""
            },
            valid: true,
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            show: false,
            rules: {
                required: value => !!value || 'Required.',
                min: v => v.length >= 8 || 'Min 8 characters',
                emailMatch: () => (`The email and password you entered don't match`),
            },
        }
    },

    methods: {
        ...mapMutations(['LOG_OUT']),
        async signIn() {
            const email = this.user.email
            const password = this.user.password
            await signInWithEmailAndPassword(auth, email, password)
            alert(`Bienvenido, ${email}`)
            const showBtn = true
            this.$store.commit('LOG_OUT', showBtn)
            this.$router.push("/cursos")
        },
        reset() {
            this.$refs.form.reset()
        },
        signin() {
            this.$refs.form.resetValidation()
        },
    },
}
</script>