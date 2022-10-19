/*
   rosserial Publisher Example
   Prints "hello world!"
*/
#include <ros.h>
#include <std_msgs/Float32.h>
#include <geometry_msgs/Twist.h>
#include <Adafruit_FXOS8700.h>
#include <Wire.h>




#define echoPin 4 // Attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 0 // Attach pin D3 Arduino to pin Trig of HC-SR04

long duration; // variable for the duration of sound wave travel
float distance; // variable for the distance measurement


Adafruit_FXOS8700 accelmag = Adafruit_FXOS8700(0x8700A, 0x8700B);

ros::NodeHandle  nh;

std_msgs::Float32 dist_msg;
geometry_msgs::Twist twist;

ros::Publisher chatter("Ultra", &dist_msg);
ros::Publisher chatter2("IMU", &twist);


void displaySensorDetails() {
  sensor_t accel, mag;
  accelmag.getSensor(&accel, &mag);
  delay(500);
}

void setup()
{
  
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT


  nh.getHardware()->setBaud(57600);
  nh.initNode();
  
  nh.advertise(chatter);
  nh.advertise(chatter2);

  /* Initialise the sensor */
  if (!accelmag.begin()) {
    /* There was a problem detecting the FXOS8700 ... check your connections */
    //Serial.println("Ooops, no FXOS8700 detected ... Check your wiring!");
    while (1)
      ;
  }
}

void loop()
{
  sensors_event_t aevent, mevent;

  accelmag.getEvent(&aevent, &mevent);


  twist.linear.x = aevent.acceleration.x;
  twist.linear.y = aevent.acceleration.y;
  twist.linear.z = aevent.acceleration.z;
  chatter2.publish( &twist );
  nh.spinOnce();
  
  delayMicroseconds(100);

  // ====================================
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;

  dist_msg.data = distance;
  chatter.publish( &dist_msg );
  nh.spinOnce();


}
