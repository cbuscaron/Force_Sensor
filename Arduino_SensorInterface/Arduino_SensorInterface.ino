float PVal = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  }
 
void loop() {
  // put your main code here, to run repeatedly:
  if(PVal <=1){PVal++;}
  if(PVal >=40){PVal--;}
  else{PVal++;}
  
  Serial.println(PVal);
  
  delay(2000); //delay tenth of a  second to slow things down a little.
}

