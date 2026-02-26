# Experience Replay Notes
## Overview
Experience Replay is a continual learning technique used to reduce catastrophic forgetting in machine learning models.<br> It works by storing a small portion of previously learned data in a buffer and mixing it with new task data during training.<br> This helps the model retain earlier knowledge while learning new information.<br>
## Core Concept
* A small sample of old dataset examples is stored in a memory buffer.<br>
* During training on a new task, buffered (old) data is combined with new data.<br>
* The model is trained on this mixed dataset to balance old and new knowledge.<br>
## Comparison with Other Techniques
**Joint Training:** Trains on all tasks together at once.<br>
**Elastic Weight Consolidation (EWC):** Protects important parameters using a regularization term instead of storing old data.<br>
**Experience Replay:** Stores and reuses actual past samples, making it simple and effective, especially for classification tasks.<br>
## Advantages
* Easy to implement.<br>
* Effective for classification problems.<br>
* Flexible and adaptable to different tasks.<br>
## Limitations
* Requires extra memory to store previous samples.<br>
* Random sampling works for simple tasks but may not be ideal for sensitive applications where certain data points must be prioritized.<br>
## Implementation Notes
* Use a two-dimensional buffer to store selected images or samples.<br>
* Randomly select and store data from previous tasks.<br>
* Compare task accuracy to evaluate performance.<br                                              
* Datasets can be sourced from platforms like Kaggle and loaded into environments such as Google Colab.<br><br>
Experience Replay provides a practical balance between retaining old knowledge and learning new tasks, making it a widely used approach in continual learning scenarios.<br>
