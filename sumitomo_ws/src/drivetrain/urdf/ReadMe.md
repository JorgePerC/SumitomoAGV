# URDF
Universal Robot Description File.

A file that contains information about the robot physical structure. Remember using Denavit Hartenberg standart to describe your robot.

## Tips:
* Group all your URDF files under myPackage/urdf/
* Parse your file once you think you've finished. This is to verify it has the correct syntax 
* Follow the [guide](http://wiki.ros.org/urdf/Tutorials/Create%20your%20own%20urdf%20file)!
* See more about [joints](http://wiki.ros.org/urdf/XML/joint) an their [description](https://ocw.tudelft.nl/course-lectures/2-2-1-introduction-to-urdf/)


## Minor dependencies:
* If you haven't, install `sudo apt-get install liburdfdom-tools`