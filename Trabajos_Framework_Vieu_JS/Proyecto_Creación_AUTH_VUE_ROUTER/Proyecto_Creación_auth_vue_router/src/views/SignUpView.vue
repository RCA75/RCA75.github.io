<template>
  <v-content class="signUpForm">
    <v-container fluid fill-height>
      <v-layout justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="purple">
              <v-toolbar-title>Crea una cuenta</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                prepend-icon="mdi-account"
                name="email"
                label="Introduzca su email"
                type="text"
                v-model="signUpUser.email"
              ></v-text-field>
              <v-text-field
                id="password"
                prepend-icon="mdi-lock"
                name="password"
                label="Contraseña de mínimo 6 caracteres"
                type="password"
                v-model="signUpUser.password"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" type="submit" @click="saveNewUser"
                >SIGNUP</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>
<script>
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
export default {
  data() {
    return { signUpUser: { email: "", password: "" } };
  },
  methods: {
    async saveNewUser() {
      const { email, password } = this.signUpUser;
      const auth = getAuth();
      await createUserWithEmailAndPassword(auth, email, password);
      this.$router.push("/");
    },
  },
};
</script>
<style>
.signUpForm {
  margin-top: 50px;
}
</style>
