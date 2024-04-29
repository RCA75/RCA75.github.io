<template>
  <div class="homeView">
    <h1>¡Bienvenido a DomotikChile</h1>
    <v-content class="loginForm">
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Inicie sesión</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-text-field
                  prepend-icon="mdi-account"
                  name="email"
                  label="Introduzca su email"
                  type="text"
                  v-model="user.email"
                ></v-text-field>
                <v-text-field
                  id="password"
                  prepend-icon="mdi-lock"
                  name="password"
                  label="Introduzca su contraseña"
                  type="password"
                  v-model="user.password"
                ></v-text-field>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" type="submit" @click="sendLogin"
                  >Login</v-btn
                >
              </v-card-actions>
            </v-card>
            <h3 class="loginForm-routeSignUp">
              Si no tiene una cuenta,
              <router-link to="/signup">haga click aquí</router-link>
            </h3>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </div>
</template>
<script>
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
export default {
  data: () => {
    return { user: { email: "", password: "" } };
  },
  methods: {
    async sendLogin() {
      const { email, password } = this.user;
      const auth = getAuth();
      await signInWithEmailAndPassword(auth, email, password);
      this.$router.push("/success");
    },
  },
};
</script>
<style>
.loginForm {
  margin-top: 50px;
}
.loginForm-routeSignUp {
  margin-top: 50px;
}
.homeView {
  text-align: center;
  margin-top: 50px;
}
</style>
