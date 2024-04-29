<template>
    <v-card class="mx-auto overflow-hidden" width="100vw">
        <v-app-bar color="deep-purple" dark>
            <v-app-bar-nav-icon v-if="$store.state.logOutBtn === true" @click="drawer = true"></v-app-bar-nav-icon>

            <v-toolbar-title>Cursos AlfaWeb</v-toolbar-title>
            <v-spacer></v-spacer>

            <v-btn v-if="$store.state.logOutBtn === true" @click="logOut()">
                Salir
                <v-icon right>
                    mdi-logout
                </v-icon>
            </v-btn>
        </v-app-bar>

        <v-navigation-drawer v-model="drawer" height="100vh" absolute temporary>
            <v-list nav dense>
                <v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4">
                    <v-list-item v-if="$store.state.logOutBtn === false">
                        <v-list-item-icon>
                            <v-icon>mdi-home</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>
                            <router-link to="/">Home</router-link>
                        </v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                        <v-list-item-icon>
                            <v-icon>mdi-account</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>
                            <router-link to="/cursos">Cursos</router-link>
                        </v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                        <v-list-item-icon>
                            <v-icon>mdi-account</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>
                            <router-link to="/administracion">Administrar Cursos</router-link>
                        </v-list-item-title>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>
    </v-card>

</template>

<script>
import { mapMutations } from 'vuex';
import { getAuth, signOut } from "firebase/auth";
    export default {
        data: () => ({
            drawer: false,
            group: null,
        }),
        methods: {
            ...mapMutations(['LOG_OUT']),
            logOut(){
                const auth = getAuth();
                signOut(auth).then(() => {
                    alert('Sesión cerrada correctamente')
                    const unshowBtn = false
                    this.$store.commit('LOG_OUT', unshowBtn)
                    this.$router.push("/")
                }).catch((error) => {
                    console.log(error)
                    alert('Error al cerrar la sesión')
                });
            }
        },
    }
</script>