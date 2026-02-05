# Machine Learning Concepts
## Overview of the Session
This session focused on understanding the core concepts of Machine Learning, especially the mechanisms that allow machines to learn from data. The emphasis was on grasping the fundamentals clearly, as these concepts form the base of all machine learning and deep learning systems.<br>
Participants were encouraged to stay focused and actively engage, since the ideas discussed in this session directly impact how models are built and trained later on.<br>
## Neural Networks and Perceptrons
The main focus of the session was on the engine of machine learning, which is the neural network. To explain this, the concept of a perceptron was introduced.<br>
* A perceptron works similarly to a human neuron.<br>
* Just like neurons receive signals, a perceptron receives inputs.<br>
* Each input has an associated weight, which shows its importance.<br>
* These inputs and weights are processed using an activation function.
* The final result is produced as an output.<br>
This comparison with human neurons helped in understanding how machines process information and make decisions.<br>
<img width="931" height="309" alt="image" src="https://github.com/user-attachments/assets/6c4edcd9-6dbf-45bf-90b7-df1d702be87c" />

## Data Preprocessing, Noise, and Sparseness
A significant part of the session focused on data preprocessing, which is a crucial step before training any machine learning model.<br>
* Noise refers to irrelevant, incorrect, or unnecessary data that can negatively affect model performance.<br>
* Sparseness refers to data points that are very different from most of the dataset.<br>
An example of bank transactions was discussed to explain sparseness. Unusual transactions that differ from normal spending behavior can indicate important events, such as suspicious or fraudulent activity. Identifying such sparse data helps models detect meaningful patterns rather than ignoring them.<br>
This discussion highlighted why cleaning and understanding data is as important as building the model itself.<br>
<br><img width="469" height="331" alt="image" src="https://github.com/user-attachments/assets/f3535e08-c920-4a0a-9df9-9fb109dfbba6" />

## Structure of a Perceptron and Bias
The internal structure of a perceptron was explained in more detail:<br>
* Inputs to a perceptron usually come from other perceptrons, forming a connected network.<br>
* These interconnected perceptrons together create a neural network.<br>
* The concept of bias was introduced as a constant value added to the input.<br>
* Bias helps the model adjust predictions and can be seen as a systematic error correction mechanism during learning.<br>
Understanding bias is important because it allows the model to fit data more accurately.<br>
<img width="922" height="355" alt="image" src="https://github.com/user-attachments/assets/8c02feaf-6982-4689-8c6b-557df41daa70" />

## Neural Network Learning Process
The session then moved toward how neural networks actually learn:<br>
* Neural networks consist of input layers, hidden layers, and output layers.<br>
* Hidden layers play a key role in learning complex patterns.<br>
* It was explained that adding too many layers can lead to a saturation point, where accuracy no longer improves.<br>
* Learning happens over multiple epochs, where the model repeatedly processes the data.<br>
* During training, weights are updated to minimize errors and improve predictions.<br>
This part of the session helped clarify how training improves a model step by step.<br>
