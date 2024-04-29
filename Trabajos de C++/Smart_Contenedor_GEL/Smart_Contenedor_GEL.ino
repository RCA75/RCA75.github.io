#include <Servo.h>
#include <Ultrasonic.h>

long distancia;
long tiempo;
Servo myservo;                  //declaramos un objeto miservo de la la libreria Servo
    
void setup() 
{  
  pinMode(9, OUTPUT);           //Declaramos el pin 9 como salida  (Echo) Sensor ultrasonico1
  pinMode(8, INPUT);            //Declaramos el pin 8 como entrada (Trigger) Sensor ultrasonico1
  myservo.attach(5);            //definimos el pin5 para controlar el servo    
  myservo.write(0);             // coloca el servo en su posición inicial
  Serial.begin(9600);           // velocidad comunicacion serial
}

void loop() 
{
 Sensores_Ultrasonico ();        // Ajustes de Sensor 1 

  myservo.write(0);
if((distancia < 15))              // Si distancia menor a 15 cm el servo se situa en 90 grados
{
  myservo.write(90);
  delay(3000);
  myservo.write(0);
}else         
 {  
  myservo.write (0);            
 }
  myservo.write (0);  
  Serial.println("");  
  Serial.print("  Distancia estimada: "); //Comandos para ver en pantalla la distancia al cual está el obstaculo
  Serial.print(distancia);
  Serial.println(" cm");
}

void Sensores_Ultrasonico ()
{
 digitalWrite(9, LOW);          // Por cuestión de estabilización del sensor ULTRASONICO
 delayMicroseconds(5);
 digitalWrite(9, HIGH);         // Envío del pulso ultrasónico*/
 delayMicroseconds(10);
 tiempo=pulseIn(8, HIGH);       //Función para medir la longitud del pulso entrante
 distancia= int((tiempo/2)/29);  //fórmula para calcular la distancia obteniendo un valor entero
}
