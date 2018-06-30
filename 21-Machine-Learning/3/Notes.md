## 21.3 - Neural Networks and Deep Learning

### Goals

* Understand the types of problems where neural networks work well.
* Use Keras to build and train neural networks.
* Use Keras to build and train a _deep_ neural network.
* Learn how to save the models you create and train.
* Introduce unsupervised learning with k-means clustering.

### Why?

* Neural networks excel at finding patterns in non-linear data.
* Really good at problems of image, speech recognition (lots of features, data are not linearly-separable).

### Notes

* Even more than last time, we'll have to skip over details of what many of these parameters mean. We must balance the need to learn first principles with the need to get y'all productive.
* With that said, I've tried to either define everything in these notes, or link to resources on nearly every parameter / concept we won't get to discuss in detail.

### Resources

* [Neural Networks and Deep Learning - Michael Nielsen](http://neuralnetworksanddeeplearning.com/chap1.html)
* [Neural Network TensorFlow Playground](http://playground.tensorflow.org/)
* [Explain overfitting to me like I'm 5](https://www.quora.com/What-is-an-intuitive-explanation-of-over-fitting-particularly-with-a-small-sample-set-What-are-you-essentially-doing-by-over-fitting-How-does-the-over-promise-of-a-high-R%C2%B2-low-standard-error-occur)

### Exercises

#### Introduction to Neural Networks - Slideshow

* Nodes are neurons
* Input layer - our features
* Output layer - final layer that outputs a probability that our input belongs to the predicted class.
* Hidden layers - layers of neurons in between input and output neurons
* Bias - if you had no other inputs, you'd output the value of the bias. Changing the bias helps us shift our decision boundary to the left or right to better classify items.

#### Everyone Do - TensorFlow playground

* You can configure and train a neural network on some test data and see how it works in real time!
* For now, we won't change the default learning rate, activation function or regularization.
* Activation function: the function used to output a value given the inputs, at each node. The network uses this output to classify input accordingly. [This article](https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0) discusses the intuition behind why we're using activation functions like Tanh and Relu.
* Regularization: a technique to help reduce overfitting. See [Chapter 3 of Nielsen's book](http://neuralnetworksanddeeplearning.com/chap3.html#overfitting_and_regularization) and [this reference](https://chatbotslife.com/regularization-in-deep-learning-f649a45d6e0).
* Choose the dataset with two blobs, and keep only features X1 and X2 as your inputs to the network.
* Remove all but one hidden layer.
* Add neurons on this layer until you have 6.
* When you hit Play, the network begins learning.
* Epochs = # of training cycles.
* [How do we know how many nodes to add in our hidden layer?](https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw)
* [Another reference on choosing the right number of layers, and nodes](https://stackoverflow.com/questions/35520587/how-to-determine-the-number-of-layers-and-nodes-of-a-neural-network)
* This dataset is linearly separable, and this separates classes with a line down the middle of them. This is similar to what we saw with logistic regression and Linear SVC (SVM).
* But neural networks excel at solving non-linear problems. Let's examine the dataset with a blue blob inside of the larger orange circle.
* This helps us solve some problems we couldn't before with other classification methods!
* Each layer distills and refines the output it gets from previous layers.
* More complex problems require more layers, additional features, and tuning of some of the parameters like the activation function, regularization, etc.
* Loss is the difference between the predicted value and actual value for our test set. The loss function describes how we calculate loss. The loss you then see displayed is the average of the individual loss values. [Loss functions explained](https://www.youtube.com/watch?v=Skc8nqJirJg)
* Spend a few minutes playing in the playground.

#### Instructor Do - Introduction to Keras

* Keras is a wrapper on top of TensorFlow, a Google-developed library for machine learning. It facilitates the creation of neural networks.

#### Everyone Do - One Hot Encoding

* [Two](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/) [references](https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f) on one-hot encoding.

#### Everyone Do - Building Neural Nets with Keras

* [Getting Started with Keras](https://keras.io/getting-started/sequential-model-guide/)
* [Optimizing Neural Networks, conceptually (chapter 3 of Michael Nielsen's Book)](http://neuralnetworksanddeeplearning.com/chap3.html)
* `pip install keras`, and maybe `pip install tensorflow` for good measure (I had to install both separately).
* For neural networks we're using for classification, we've got to label and one-hot encode our data.
* With Keras, you first create your network with shapes and layers. Then, we "compile" a network (configure the training process, e.g. how the network evaluates loss, etc.). Finally, we fit our network to our data.
* We're using the `Sequential` model from Keras, which is a linear stack of layers used to build your network.
* A [`Dense`](https://www.quora.com/In-Keras-what-is-a-dense-and-a-dropout-layer) layer is just a normal hidden layer of our network: each node is connected to input nodes from the left, and connect to other nodes on the right.
* `input_dim` -> the number of features we're using to predict outcomes.
* [What are RELU and softmax activation functions?](https://github.com/Kulbear/deep-learning-nano-foundation/wiki/ReLU-and-Softmax-Activation-Functions)
* The optimization function helps us minimize loss. Here, we use [Adam](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/).
* Model accuracy (# of correct classifications / total classifications) is not calculated by default. You have to pass it in a list of `metrics` in the arguments to `model.compile()`.
* Since the order of input records your neural network uses to process data can matter on the weights chosen by the network, [shuffling your data can help better train the model](https://datascience.stackexchange.com/questions/24511/why-should-the-data-be-shuffled-for-machine-learning-tasks).

#### Everyone Do Introduction to Deep Learning

* We'll first create a neural network (reinforcing what we learned last exercise) and then we'll create a deep learning model, comparing the two.
* The data we generate in this example is a non-linear classification problem.
* Neural networks are great for classifying non-linear data.
* Remember that we'll need to 1.) scale our input features and 2.) one-hot encode our response vector before passing the data to our neural network.
* Deep artificial neural network = a neural network with more than one hidden layer (the layers go deep), which can improve the learning process at the expense of it taking longer to train.

#### Students Do - Moons (15 min)

#### Students Do - Deep Voice (20 min)

* Note that neural networks can be prone to overfitting. Always split data into training and test set, and confirm accuracy on the test set.
* The `inverse_transform` method of our label encoder object converts the labels our encoder applied to the original labels in our dataset.

#### Instructor Do - Saving Models

* Training a model can be time-consuming. Depending on the complexity of the problem and the amount of data, it also might be costly! Large deep networks are typically trained on GPUs now. The machines that utilize GPUs for learning on platforms like AWS can be costly.
* Once we have our model, we don't want to have to train it from scratch again! We want to save our model.
* Given a model, `model.save('filename_of_model.h5')` will save the model to disk using the HDF5 binary file format.
