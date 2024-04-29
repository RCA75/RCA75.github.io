import { initializeApp } from "firebase/app";
import {getAuth} from 'firebase/auth'

const firebaseConfig = {
    apiKey: "AIzaSyDyfU9dcPIJVRA_WHLGWjDxzpHGRZd4dIM",
    authDomain: "proyectosvuereinaldocarocca.firebaseapp.com",
    projectId: "proyectosvuereinaldocarocca",
    storageBucket: "proyectosvuereinaldocarocca.appspot.com",
    messagingSenderId: "436820393173",
    appId: "1:436820393173:web:12a725f737615e1f86b65c",
    measurementId: "G-9DJTPBMZ9B"
  };
    
const app = initializeApp(firebaseConfig);
const auth = getAuth(app)

export default auth