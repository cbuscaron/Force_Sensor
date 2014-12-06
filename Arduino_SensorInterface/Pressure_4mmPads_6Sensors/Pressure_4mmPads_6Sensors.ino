int fsr1Pin = 0;
int fsr2Pin = 1;
int fsr3Pin = 2;
int fsr4Pin = 3;
int fsr5Pin = 4;
int fsr6Pin = 5;
int fsrPin[] ={0, 1, 2, 3, 4, 5};


int fsrReading[6];
int fsrVoltage[6];
unsigned long fsrResistance[6];
unsigned long fsrPressure[6];

#include <math.h>

void setup(void){Serial.begin(115200);}



void loop(void){
        
        for(int i; i<6; i++){
                fsrReading[i]= analogRead(fsrPin[i]);
                fsrVoltage[i] = map(fsrReading[i], 0, 1023, 0, 5000);
            }  
  
        
          //Voltage = VCC*R/(R+FSR) where R = 10k and Vcc = 5v
        for(int i; i<6; i++){          
            fsrResistance[i] = 5000-fsrVoltage[i];
            fsrResistance[i] *=10000;
            fsrResistance[i] /=fsrVoltage[i];
                        
            fsrPressure[i] = 214386*pow(fsrResistance[i],-1.135);
          }
        
            Serial.println("TS");
        
        
        for(int i; i<6; i++){
          Serial.println(fsrPressure[i]);
                
        }
        
        Serial.println("TE");
        /*Serial.println("--------------------------------------");
        for(int i; i<6; i++){
               
                  if(fsrVoltage[i] == 0){
                      Serial.print("Sensor ");
                      Serial.print(i);
                      Serial.print(" Value =  ");
                      Serial.println(fsr1Pin);
                    }
                    
                 else{
                      Serial.print("Sensor ");
                      Serial.print(i);
                      Serial.print("Value =  ");
                      Serial.println(fsrPressure[i]);
                 
                 
                 }
        
        
        }
        
       Serial.println("--------------------------------------");*/
        
        



}
