# Data-Collection-Algorithms
This is a git repository for the creation of Image Capture Algorithms for Data Collection Systems.

Here is where I intend to familiarize myself with OpenCV by first creating my own Image Capture
program that builds of whats been shown and given in the tutorial video and series below:

https://www.youtube.com/watch?v=dZ4itBvIjVY

My first goal when building upon the dataCollection.py program given within this video is to create
Data Collection algorithm that oscillates between different camera setting such as in brightness, 
contrast, saturation, etc. With the aim of improving my methodology around the creation of haar 
cascades for future projects.

In other repositories I'll deep dive into the actual object recognition side of things with the use
of haar cascades to become more sophisticated with my object recognition algorithms. Mixing togther
features that can detect objects, object amount, object location, distance from object, object size,
etc.

There's a huge sea of tutorials around Computer Vision that I look to dive into and use to integrate
Computer Vision into the technologies I work on.

When looking at all the program created thus far for observing how the image changes whiles having
various VideoCapture properties tinkered with. To keep things moving, I'll be picking a set of the
properties with the most visible change to be fused into a single data collection program that not
only collects images in the default settings of the camera but also oscilates the values for a 
variety of different properties belonging to the VideoCapture stream.

It would have also been more efficient to test this kind of thing under an object oriented scheme 
where theres a main tester file for all the different properties using a hierarchy to require less
copying and pasting between programs.
