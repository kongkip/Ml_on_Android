# Flower Type Prediction App

This is an example of an interactive Python console script running in an Android app using
[Chaquopy](https://chaquo.com/chaquopy/). Some starting points:

* The example Python script is in 
  [`app/src/main/python/main.py`](https://github.com/chaquo/chaquopy-console/blob/master/app/src/main/python/main.py).

    I replaced this with my own code for Machine Learning, I trained iris dataset with a simple logistic regression model
* The Android activity which hosts it is in 
  [`app/src/main/java/com/chaquo/python/console/MainActivity.java`](https://github.com/chaquo/chaquopy-console/blob/master/app/src/main/java/com/chaquo/python/console/MainActivity.java).
* The Chaquopy configuration (Python version, pip requirements list, etc.) is in 
  [`app/build.gradle`](https://github.com/chaquo/chaquopy-console/blob/master/app/build.gradle).

# Ml_on_Android

This demo shows iris example on android, it both includes training and inference

![demo](https://github.com/kongkip/Ml_on_Android/blob/master/video/demo.gif)


Credits goes to [Chaquo](https://github.com/chaquo) I merely created a wrapper.
