<template>
    <v-item-group data-app>
        <v-container>
            <v-row>
                <v-col cols="4" v-for="(curso, i) in $store.state.cursosDB" :key="i">
                    <v-card width="400px" height="100vh">
                        <v-img width="200px" :src="curso.url">
                            <v-app-bar flat color="rgba(0, 0, 0, 0)">
                                <v-spacer></v-spacer>
                            </v-app-bar>
                        </v-img>
                        <v-card-text>
                            <div class="font-weight-bold ml-8 mb-2">
                                <strong>{{ curso.nombre }}</strong>
                            </div>
                            <v-timeline align-top dense>
                                <v-timeline-item small>
                                    <div>
                                        <div class="font-weight-normal">
                                            <p><strong>Costo</strong>: ${{ curso.costo }} </p>
                                        </div>
                                        <p><strong>duracion</strong>: {{ curso.duracion }} </p>
                                    </div>
                                </v-timeline-item>
                                <v-timeline-item small>
                                    <div>
                                        <div class="font-weight-normal">
                                            <p><strong>Cupos</strong>: {{ curso.cupos }} </p>
                                        </div>
                                        <p>
                                            <strong>Estado</strong>:
                                            <span v-if="curso.estado == true">Completo</span>
                                            <span v-else>Incompleto</span>
                                        </p>
                                    </div>
                                </v-timeline-item>
                                <v-timeline-item small>
                                    <div>
                                        <div class="font-weight-normal">
                                            <p><strong>Fecha de Registro</strong>: </p>
                                        </div>
                                        <p>{{ curso.fecha }} </p>
                                    </div>
                                </v-timeline-item>
                                <v-timeline-item small>
                                    <div>
                                        <div class="font-weight-normal">
                                            <p><strong>Descripción</strong>:</p>
                                        </div>
                                        <p>{{ curso.descripcion }} </p>
                                    </div>
                                </v-timeline-item>
                            </v-timeline>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-item-group>
</template>