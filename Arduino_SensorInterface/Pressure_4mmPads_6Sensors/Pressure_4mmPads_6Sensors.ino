int fsrPin = 0;
int fsrReading;
int fsrVoltage;
unsigned long fsrResistance;
unsigned long FSR;
unsigned long fsrPressure;

#include <math.h>

void setup(void){Serial.begin(9600);}



void loop(void){
        fsrReading = analogRead(fsrPin);
        fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
        
        if(fsrVoltage == 0){
            Serial.println(fsrPin);
        } else{
            //Voltage = VCC*R/(R+FSR) where R = 10k and Vcc = 5v
            fsrResistance = 5000-fsrVoltage;
            fsrResistance *=10000;
            fsrResistance /=fsrVoltage;
            
            
            fsrPressure = 214386*pow(fsrResistance,-1.135);
            
            Serial.println(fsrPressure);
        
        }
        
        delay(1000);



}
