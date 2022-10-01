/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */

#include <ros.h>
#include <std_msgs/Float32.h>
#include <geometry_msgs/Twist.h>
#include <Adafruit_FXOS8700.h>


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
}

void setup()
{

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT

   /* Initialise the sensor */
  if (!accelmag.begin()) {
    /* There was a problem detecting the FXOS8700 ... check your connections */
    Serial.println("Ooops, no FXOS8700 detected ... Check your wiring!");
    while (1);
  }

  nh.getHardware()->setBaud(115200);
  nh.initNode();

  nh.advertise(chatter);
  nh.advertise(chatter2);

}

void loop()
{
  sensors_event_t aevent, mevent;

  /* Get a new sensor event */
  accelmag.getEvent(&aevent, &mevent);

  /* Display the accel results (acceleration is measured in m/s^2) */
  /*
  Serial.println(aevent.acceleration.x, 4);
  Serial.println(aevent.acceleration.y, 4);
  Serial.println(aevent.acceleration.z, 4);
  */
  
  twist.linear.x = aevent.acceleration.x;
  twist.linear.y = aevent.acceleration.y;
  twist.linear.z = aevent.acceleration.z;

  
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
  chatter2.publish( &twist );
  nh.spinOnce();
  delay(1000);
}
