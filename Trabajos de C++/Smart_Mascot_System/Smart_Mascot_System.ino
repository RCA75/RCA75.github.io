#include <Servo.h>
long distancia;
long distancia2;
long tiempo;
long tiempo2;
Servo myservo;                  //declaramos un objeto miservo de la la libreria Servo
int VALOR;                      // variable que recibe el dato
int led1 = 13;                  // redefinicion del pin de arduino para led indicador Sensor Ultrasonico 1
int led2 = 12;                  // redefinicion del pin de arduino para led indicador Sensor Ultrasonico 2
int led3 = 4;
int releled1 = 11;              // pin del arduino para indicar funcionamiento sensor ultrasonido y Servo
int electroval = 10;            // pin del arduino para indicar funcionamiento electrovalvula
const int bomba = 3;            // pin del arduino para indicar funcionamiento bomba de extraccion.
const int pinBuzzer =  2;       // BUZZER ALARMA            

void setup() 
{  
  pinMode(9, OUTPUT);           //Declaramos el pin 9 como salida sensor ultrasonico1 de nivel 
  pinMode(8, INPUT);            //Declaramos el pin 8 como entrada Sensor ultrasonico1 de nivel
   
  pinMode(7, OUTPUT);           //Declaramos el pin 7 como salida Sensor ultrasonico2 de nivel
  pinMode(6, INPUT);            //Declarsamos el pin6 como entrada sensor ultrasonico2 de nivel
  
  pinMode(led1, OUTPUT);        //Led 1 indica estado funcionamiento Sensor Ultrasonico 1
  pinMode(led2, OUTPUT);         //Led 2 indica estado funcionamiento Sensor Ultrasonico 2
  
  pinMode(releled1, OUTPUT);    // Indica accionamiento sensor ultrasonico de Nivel y Servo 
  pinMode(bomba, OUTPUT);       // Pin de salida para activar bomba
  pinMode(pinBuzzer, OUTPUT);   // pin de salida activar buzzer
 
  myservo.attach(5);            //definimos el pin5 para controlar el servo    
  myservo.write(0);             // coloca el servo en su posición inicial
  Serial.begin(9600);           // velocidad comunicacion serial
}

void Sensores_Ultrasonico ()
{
 digitalWrite(9, LOW);                         // Por cuestión de estabilización del sensor ULTRASONICO
 delayMicroseconds(5);
 digitalWrite(9, HIGH);                        // Envío del pulso ultrasónico*/
 delayMicroseconds(10);
 tiempo=pulseIn(8, HIGH);                      //Función para medir la longitud del pulso entrante
 distancia= int(0.017*tiempo);                 //fórmula para calcular la distancia obteniendo un valor entero
 digitalWrite(7, LOW);
 delayMicroseconds(5);
 digitalWrite(7, HIGH);                        // Envío del pulso pulso ultrasonico*/
 delayMicroseconds(10);
 tiempo2=pulseIn(6, HIGH);                     // Función para medir la longitud del pulso entrante
 distancia2= int(0.017*tiempo2);               // Fórmula para calcular la distancia obteniendo un valor entero
}

void loop() 
{
// digitalWrite(9, LOW);                         // Por cuestión de estabilización del sensor ULTRASONICO
// delayMicroseconds(5);
// digitalWrite(9, HIGH);                        // Envío del pulso ultrasónico*/
// delayMicroseconds(10);
// tiempo=pulseIn(8, HIGH);                      //Función para medir la longitud del pulso entrante
// distancia= int(0.017*tiempo);                 //fórmula para calcular la distancia obteniendo un valor entero
// digitalWrite(7, LOW);
// delayMicroseconds(5);
// digitalWrite(7, HIGH);                        // Envío del pulso pulso ultrasonico*/
// delayMicroseconds(10);
// tiempo2=pulseIn(6, HIGH);                     // Función para medir la longitud del pulso entrante
// distancia2= int(0.017*tiempo2);               // Fórmula para calcular la distancia obteniendo un valor entero

 Sensores_Ultrasonico ();                       // Ajustes de Sensor 1 (Alimento) y Sensor 2 (Agua)
 
  if((distancia > 5) && (distancia2 >= 4))     // Condiciones a Cumplir si ambos estanques estan vacios
   {
      digitalWrite(releled1, HIGH);            // Envia pulso para activar Servo y girar 45 grados
      digitalWrite(led1,HIGH);                 // Enciende LED pin 13
      Serial.println("ESTANQUES VACIOS");      // Mensaje de Funcionamiento
      delay(5000);                             // Probar con tiempo mas bajo antes de montar (5 Seg)
          
      tone(pinBuzzer, 440);                    // Se Activa Alarma
      delay(5000);
      noTone(pinBuzzer);                       // Se desactiva Alarma
      delay(100);
       
      digitalWrite(electroval,HIGH);           // Activa Electrovalvula 
      delay(5000);                             // Tiempo activacion Electrovalvula
      digitalWrite(electroval,LOW);            // Desactiva Electrovalvula
     
    }
     else if((distancia < 5) && (distancia2 <= 3))    // Condiciones a cumplir si ambos estanques estan Llenos
      {
        digitalWrite(led3,HIGH);                 // Enciende LED pin 4
        myservo.write(45);                       // Movemos el servo en una dirección 45 grados
        delay(2000);                             // Tiempo de activacion Servo
        myservo.write(0);                        // Volvemos el servo en posicion inicial
        digitalWrite(led3,LOW);                  // Apaga LED pin 4
    
        digitalWrite(bomba,HIGH);                // Se Activa bomba extraccion 
        delay(5000);                             // Tiempo activacion bomba extraccion
        digitalWrite(bomba,LOW);                 // Desactiva bomba extracion 
        
      }
       else if((distancia < 5) && (distancia2 >= 4))    // Condiciones a cumplir si ambos estanques 1 lleno y estanque 2 vacio
       {
        digitalWrite(led3,HIGH);                 // Enciende LED pin 4
        myservo.write(45);                       // Movemos el servo en una dirección 45 grados
        delay(2000);                             // Tiempo de activacion Servo
        myservo.write(0);                        // Volvemos el servo en posicion inicial
        digitalWrite(led3,LOW);                  // Apaga LED pin 4
        delay(10);                               // Tiempo de espera para activar Electrovalvula
        digitalWrite(electroval,HIGH);           // Activa Electrovalvula 
        delay(5000);                             // Tiempo activacion Electrovalvula
        digitalWrite(electroval,LOW);            // Desactiva Electrovalvula
        }
         else if((distancia > 5) && (distancia2 <= 3))    // Condiciones a cumplir si ambos estanques 1 vacio y estanque 2 lleno
          {
            tone(pinBuzzer, 440);                    // Se Activa Alarma
            delay(5000);
            noTone(pinBuzzer);                       // Se desactiva Alarma
            delay(100);              
           }
   delay(2700000);
} 
