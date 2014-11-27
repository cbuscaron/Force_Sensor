float PVal = 0;
boolean Up = false;
boolean Down = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  }
 
void loop() {
  // put your main code here, to run repeatedly:
  if(PVal <=1){PVal++; Up = true; Down = false;}
  else if(PVal >=40){PVal--; Down = true; Up = false;}
  else{
      if(Up)
        PVal++;
      else if (Down)
        PVal--;
}
  
  Serial.println(PVal);
  
 
}

