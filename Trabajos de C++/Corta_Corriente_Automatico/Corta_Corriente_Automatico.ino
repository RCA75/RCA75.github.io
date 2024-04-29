int digitalSensor = 0;
int ledPin = 12;
int Led = 10;

void setup() 
{
  Serial.begin(9600);
  pinMode(7, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(Led, OUTPUT);
  digitalWrite (ledPin, HIGH);
  digitalWrite(Led, HIGH);
  Serial.println("MOTOR LISTO CON ENERGIA");
  delay(3000);
}

void loop() 
{
  digitalSensor=digitalRead(7);
  while(digitalSensor == HIGH) //sensor con 5v
  {
    digitalWrite(Led, LOW);     
    Serial.println("SISTEMA ANTI-ROBO DESACTIVADO");         
    digitalWrite(ledPin, HIGH); //Desactivado Normalmente Cerrado Logica Inversa Led Verde Apagado
    delay(500);  
  }
    digitalWrite(ledPin, LOW);  //Activado Normalmente Abierto Logica Inversa (Led Verde Encendido
    Serial.println("SISTEMA ANTI-ROBO ACTIVADO"); 
    digitalWrite(Led, LOW);    
//    delay(20000);      

}
