import { initializeApp } from "firebase/app";
import {getFirestore, collection} from 'firebase/firestore'

const firebaseConfig = {
    apiKey: "AIzaSyDyfU9dcPIJVRA_WHLGWjDxzpHGRZd4dIM",
    authDomain: "proyectosvuereinaldocarocca.firebaseapp.com",
    projectId: "proyectosvuereinaldocarocca",
    storageBucket: "proyectosvuereinaldocarocca.appspot.com",
    messagingSenderId: "436820393173",
    appId: "1:436820393173:web:12a725f737615e1f86b65c",
    measurementId: "G-9DJTPBMZ9B"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app)
const cursosCollection = collection(db, 'cursos')

export default cursosCollection