int val = 0;       //Int. Magnetico 1
int val1 = 0;      //Int. Magnetico 2 
int val2 = 0;      //Sensor Movimiento 1
int val3 = 0;      //Sensor Movimiento 2

int led = 13;
int IntMagnetico1 = 5;
int IntMagnetico2 = 4;
int buzzer = 8;
int sensorPIR1 = 7;
int sensorPIR2 = 6;

void setup() 
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(IntMagnetico, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(sensorPIR1, INPUT)
  pinMode(sesnorPIR2, INPUT);
}

void loop() 
{
  val = digitalRead(IntMagnetico1);   //Pin 5 Puerta Principal
  val1 = digitalRead(IntMagnetico2);  //Pin 4 Ventana Piso 2
  val2 = digitalRead(sensorPIR1);     //Pin 7 Living
  val3 = digitalRead(sensorPIR2);     //Pin 6 Comedor
  
  if(val == LOW)
   {
    //envio alerta mensaje SMS 
    digitalWrite(led, HIGH);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
    delay(200);
   }
   else
   {
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
   }
  if(val1 == LOW)
   {
    //envio alerta mensaje SMS 
    digitalWrite(led, HIGH);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
    delay(200);
   }
   else
   {
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
   }
  if(val2 == HIGH)
   {
    //envio alerta mensaje SMS 
    digitalWrite(led, HIGH);
    digitalWrite(buzzer, HIGH);
    delay(200);
   }
   else
   {
    digitalWrite(led, LOW);
    digitalWrite(buzzer, LOW);
    delay(200);    
   } 
}

/* Rutina de envio SMS */
