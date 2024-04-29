<template>
    <v-card>
        <v-tabs color="deep-purple accent-4" right>
            <v-tab>Ingresar</v-tab>
            <v-tab>Registrarse</v-tab>

            <v-tab-item>
                <v-container fluid>
                    <v-row>
                        <v-col cols="12" md="4">
                            <log-in></log-in>
                        </v-col>
                    </v-row>
                </v-container>
            </v-tab-item>
            <v-tab-item>
                <v-container fluid>
                    <v-row>
                        <v-col cols="12" md="4">
                            <sign-in></sign-in>
                        </v-col>
                    </v-row>
                </v-container>
            </v-tab-item>
        </v-tabs>
    </v-card>
</template>

<script>
import LogIn from '../components/LogIn.vue'
import SignIn from '../components/SignIn.vue'
export default {
    components:{
        LogIn,
        SignIn
    }
}
</script>