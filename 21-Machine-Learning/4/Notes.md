## 21.4 - Classifying Images, Convolutional Neural Networks

### Goals

* Review how to create a neural network, this time using MNIST handwritten digit data.
* Build a Flask app that uses a model to classify images.
* Use a pre-trained Convolutional Neural Network (CNN) model to make predictions.

### Why?

* Image recognition is relevant for many industries, and a lot of fun to work with (should reinforce some principles we learned this week).
* CNNs are one of the best types of models for performing classifications on images, sounds, etc.
* Solidify experience with using models in the context of a full-stack application (with Flask).

### Resources

* [An OK YouTube video that describes some of the principles behind CNNs](https://www.youtube.com/watch?v=FmpDIaiMIeA)
* [The corresponding notes to the above YouTube video](http://brohrer.github.io/how_convolutional_neural_networks_work.html)

### Introduction to Convolutional Neural Networks

* Convolutional Neural Networks (we're doing to call these CNNs from now on) are great for recognizing visual patterns in the input data fed to it.
* You may see CNNs called ConvNets, as well.
* They are used in a wide range of applications including image recognition, self-driving cars, and medical imaging.
* CNNs employ convolutional filtering layers to help detect spatial features in images. Those features are then fed into a final fully connected layer that makes the final predictions.
* Since these networks are multi-layer, one layer will start to identify basic patterns (e.g. the edges of lines), and the next layer will take those patterns and recognize even more complex ones (e.g. whole shapes), and on and on.
* CNNs can become very complex! Just like normal neural networks and deep learning networks like we saw last class, the optimal shape of a network is still an open research problem.
* Keras facilitates the creation of CNNs.

### Exercises

#### MNIST (20 min)

* We'll build a neural network from [MNIST data](http://yann.lecun.com/exdb/mnist/), which contains handwritten digits, labeled with the digit they represent.
* We load the MNIST data from Keras using `from keras.datasets import mnist`
* These images are saved as an array of pixels, where each cell represents the greyscale value of the pixel at that point (0 = white, 255 = black).
* Each image is an array of 28x28 pixels, a total of 784 pixels.
* Remember in the video how we had to take our matrix of pixels (the 28x28 array), and align each pixel vertically for 1-dimensional array of 784 pixel values (1 column, 784 rows).
* MinMaxScaler scales our data from 0 -> 1, which is different than StandardScaler (normally distributes our data with mean 0 and std dev 1). [See this plot for a visual representation](https://sebastianraschka.com/images/blog/2014/about_standardization_normalization/about_standardization_normalization_44_0.png)
* We use MinMaxScaler because bounds of 0 and 1 have a specific meaning for us here: 0 indicates that the pixel is fully white, 1 fully black.
* Why do we have to one-hot encode the categorical labels for digits, since they are already numeric? [See this reference](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/).
* [What is HDF5?](https://www.quora.com/What-is-HDF5-data-format-and-what-is-it-used-for)
* We sometimes have to invert the pixel values. In our original data, we have a black digit on a white background, but the custom image is inverted. We can simply subtract using numpy to invert the pixels using `img = 1 - img`.
* We can load our own image data, scale it, and invert the color using the code in the notebook.
* We chose a loss function of [categorical cross-entropy](http://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html#cross-entropy) since our output is the probability our inputs fall into a specific category (we're performing classification).
* `keras` includes some functions for converting image data to numpy arrays that we can also feed into our network.

#### Instructor Do - Flask Images (10 min)

* This example uses a HTML form to submit the image as a file to Flask.
* Flask can read the file from the `files` dictionary in the request object.
* We can access properties of the file such as the filename using `file.filename`.
* We save the contents of the file using `file.save` in the `uploads/` directory.
* Finally, we simply redirect the user to the path to the file itself, using `url_for` (which returns the file specified by running the [`send_from_directory`](http://flask.pocoo.org/docs/0.12/api/#flask.send_from_directory) code).
* Note: if you run a service on the public internet that accepts image data, it's important to check that the file the user uploads is actually an image. [This Flask example code](http://flask.pocoo.org/docs/1.0/patterns/fileuploads/) includes some best practices.

#### Students Do - Flask Images (15 min + 5 min review)

#### Instructor Do - MNIST Flask (15 min)

* Now, we'll create a Flask app with the functionality of our MNIST digit recognition problem from Exercise 1.
* Given an image, we'll return a JSON string with the predicted digit.
* Some of this code will look strange, since there's some boilerplate to get Keras code working with Flask. [Here's a bit more on the problem](https://github.com/keras-team/keras/issues/5640).
* [This Keras blog post](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html) also describes a bit more about how to think about building a Flask deep learning app.
* You can read more about Tensorflow graphs [here](https://www.tensorflow.org/programmers_guide/graphs).

#### Everyone Do - Deploy App to Heroku (10 min)

* Take the code and associated files in `05-Evr_MNIST_Heroku/Solved`, move that to a separate directory.
* Using the Heroku CLI, create a new app, and follow the instructions to `git push` your code to Heroku.
* It may take a few minutes after deployment for the app to run. If you encounter an application error, wait 2 or 3 minutes and try again.

#### Partners Do - Explore CNNs (10 min + 10 min review)

Work with a partner to answer the following questions:

* What is a Convolutional Neural Network (CNN)?
* What is a CNN typically used for?
* What is the difference between a CNN and Deep Neural Network?

[This reference](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/) and [this one](http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/) may help.

#### LUNCH

#### Instructor Do - Pre-trained models (15 min)

* Training a CNN can actually take quite a bit of time on very high-performance (often expensive) machines. e.g. on AWS, some of the [instances optimized for training models](https://aws.amazon.com/ec2/instance-types/p3/) can cost roughly $25 / hour.
* Luckily, once a model has been trained, it can be shared and re-used elsewhere. We saw how we can use Keras to save a model and re-load it in exercise 1.
* Keras also provides many pre-trained models that we can use out of the box!
* These models have been trained using the [ImageNet](http://www.image-net.org/) training data set. They are trained to recognize many different types of objects (e.g. animals, geographic features, and much more).
* We're going to use a model called [VGG19](https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/).
* Keras provides utility functions to assist with image loading and data pre-processing. In fact, each model provides it's own pre-processing function to resize, scale, and pre-process an input image into the same format that the model was originally trained on. Without such pre-processing functions, you would have to do all of that work yourself before using the model.
* Different pre-trained models take a different image size as inputs to the model. With models that come with Keras, you can find this input size [from the docs](https://keras.io/applications/#vgg19). e.g. for VGG19, "The default input size for this model is 224x224."

#### Students Do - Xception (20 min + 10 min review)

#### Everyone Do - Flask Xception (15 min)

* We're going to take the Xception model we used in a previous exercise, and use it with a Flask app!
* Note the use of the `global` keyword inside of the `load_model()` method. This lets us modify the `model` and `graph` variables inside of this function (and change their values globally). Play around with the `global` keyword [here](https://www.programiz.com/python-programming/global-keyword).
* We'll need the `model` and `graph` later.
* The `prepare_image` function abstracts some of the work necessary to scale our images down to a size where we can feed them into the model, just like in our previous classification example.
* The Image class that comes from the `PIL` library, combined with `io.BytesIO`, allows us to simply read the image into a variable in memory and work with it in a format we can manipulate and process.
* The `graph` object is what TensorFlow will use to make predictions. `with graph.as_default()` uses the graph object we created above as the default graph object the model will use when running preditions within the block after the `with` statement.
