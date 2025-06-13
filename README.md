# MILDEW ALERT!

![mockup](/readme_img/mockup.jpg)

Mildew Alert! is a project that combines data science, machine learning engineering and software development. From collecting and processing cherry leaf image data, to making and training a machine learning model and finally deploying it through a user-friendly Streamlit app, it demonstrates a full pipeline, an end-to-end workflow of turning raw data into an interactive, usable product. You can upload many cherry leaf images and quickly receive information if they contain powdery mildew or not on [live version](https://mildew-alert-5e353bb60aa4.herokuapp.com/).

<br>

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
- The dataset contains 4208 images; 2104 of healthy cherry leaves and 2104 of cherry leaves with powdery mildew, taken from the client's crop fields.

<br>


## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

<br>


## Hypothesis and validation strategy

  ### Hypothesis
  - Machine learning model could be implemented to replace labor-intensive and time-consuming process of powdery mildew detection on cherry plantations. This would significantly speed up detection potentially saving time as well as plantation yield due to early detection.

  ### Validation strategy
  - conduct a visual study to find differences between healthy and infected leaves with the goal of confirming posibility to distinguish them
  - develop and evaluate a machine learning model with the goal of achieving at least 97% accuracy


<br>


## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business requirement 1: Data visualization
    - display and inspect "mean" and "standard deviation" images for both healthy and mildewed leaves
    - display and inspect difference image between average healhy and average mildewed image
    - display image montages and manually inspect for differences

- Business requirement 2: Data classification
    - develop a classification model that accurately distinguishes healthy from mildewed leaves with at least 97% accuracy
    - generate a report with classifications quickly on multiple images

<br>


## ML Business Case Assesment

### 1. What are the business requirements?
- The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### 2. Is there any business requirement that can be answered with conventional data analysis?
- Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

### 3. Does the client need a dashboard or an API endpoint?
- The client needs a dashboard.

### 4. What does the client consider as a successful project outcome?
- A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
- Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.

### 5. Can you break down the project into Epics and User Stories?
- Information gathering and data collection.
- Data visualization, cleaning, and preparation.
- Model training, optimization and validation.
- Dashboard planning, designing, and development.
- Dashboard deployment and release.

### 6. Ethical or Privacy concerns?
- Client is imaginary and data publicly hosted, no concerns

### 7. Does the data suggest a particular model?
- The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.

### 8. What are the model's inputs and intended outputs?
- The input is a cherry leaf image and the output is a prediction of whether the cherry leaf is healthy or contains powdery mildew.

### 9. What are the criteria for the performance goal of the predictions?
- We agreed with the client a degree of 97% accuracy.

### 10. How will the client benefit?
- The client will save work time
- The client will detect infection quicker ultimately leading to higher plantation yields

<br>

## Dashboard Design

<table>

  <!-- Page 1 -->
  <tr>
    <td valign="top" width="60%">
      <strong>Page 1: Project Summary</strong>
      <ul>
        <li><strong>Status element 1:</strong> General Information</li>
        <li><strong>Status element 2:</strong> Dataset information</li>
        <li><strong>Status element 2:</strong> Business requirements</li>
        <li><strong>Status element 3:</strong> Link to more information</li>
      </ul>
    </td>
    <td>
      <img src="./readme_img/page_1.png" alt="Page 1 Preview" width="100%"/>
    </td>
  </tr>

  <!-- Page 2 -->
  <tr>
    <td valign="top">
      <strong>Page 2: Cherry Leaf Visualizer</strong>
      <ul>
        <li><strong>Expander 1:</strong> Average and variability images</li>
        <li><strong>Expander 2:</strong> Differences between healthy and infected images</li>
        <li><strong>Expander 3:</strong> Image montage</li>
      </ul>
    </td>
    <td>
      <img src="./readme_img/page_2.png" alt="Page 2 Preview" width="100%"/>
    </td>
  </tr>

  <!-- Page 3 -->
  <tr>
    <td valign="top">
      <strong>Page 3: Powdery Mildew Classifier</strong>
      <ul>
        <li><strong>Status element:</strong> Usage description</li>
        <li><strong>File uploader:</strong> Allow multiple image upload</li>
        <li><strong>Button 1:</strong> Run classifier and display results</li>
        <li><strong>Button 2:</strong> Generate classification table</li>
        <li><strong>Button 3:</strong> Download report table</li>
      </ul>
    </td>
    <td>
      <img src="./readme_img/page_3.png" alt="Page 3 Preview" width="100%"/>
    </td>
  </tr>

  <!-- Page 4 -->
  <tr>
    <td valign="top">
      <strong>Page 4: Project Hypothesis and Validation</strong>
      <ul>
        <li><strong>Status element 1:</strong> Project hypothesis</li>
        <li><strong>Status element 2:</strong> Validation steps</li>
        <li><strong>Status element 3:</strong> Conclusion</li>
      </ul>
    </td>
    <td>
      <img src="./readme_img/page_4.png" alt="Page 4 Preview" width="100%"/>
    </td>
  </tr>

  <!-- Page 5 -->
  <tr>
    <td valign="top">
      <strong>Page 5: ML Performance Metrics</strong>
      <ul>
        <li><strong>Expander 1:</strong> Dataset distribution</li>
        <li><strong>Expander 2:</strong> Model summary</li>
        <li><strong>Expander 3:</strong> Model training</li>
        <li><strong>Expander 4:</strong> Model performance</li>
      </ul>
    </td>
    <td>
      <img src="./readme_img/page_5.png" alt="Page 5 Preview" width="100%"/>
    </td>
  </tr>

</table>


## Testing information

| **Test**                                         | **Result**                                                                            |
| ------------------------------------------------ | ------------------------------------------------------------------------------------- |
| Click on sidemenu button                         | Sidemenu toggles (shows/hides)                                                        |
| Click on a menu item                             | Corresponding page opens                                                              |
| Click on “Readme” link on summary page           | README opens in a new tab                                                             |
| Click on an expander                             | Corresponding section expands                                                         |
| Click on radio buttons in image montages         | Relevant montage appears                                                              |
| Click on refresh button before rendering montage | No action (intended behavior)                                                         |
| Click “Download Cherry Leaves Sample Dataset”    | Zip file is downloaded                                                                |
| Upload `.jpg` file                               | Upload successful                                                                     |
| Upload `.jpeg` file                              | Upload successful                                                                     |
| Upload `.png` file                               | Upload successful                                                                     |
| Upload `.mp4` file                               | Error message displayed: file type not allowed                                        |
| Attempt analysis with `.mp4` file                | Analysis is disabled                                                                  |
| Upload 100 cherry leaf images                    | Upload successful                                                                     |
| Analyze 100 cherry leaf images                   | Analysis successful (under 5 seconds)                                                 |
| Inspect results output                           | Output matches expectations                                                           |
| Click “Generate Report Table”                    | Report is generated; download button appears                                          |
| Click download button                            | Correct CSV is downloaded; button becomes disabled                                    |
| Modify uploaded files (add/remove)               | Old analysis is cleared; analysis button enabled; table and download buttons disabled |
| Upload random (non-leaf) images                  | Analysis proceeds; results are nonsensical                                            |
| Remove all files from uploader                   | All buttons are disabled                                                              |

<br>

## Unfixed Bugs

- Users can upload any image and model will confidently classify it into one of our classes. It is up to users to only upload cherry leaf images

<br>

## Deployment

### Heroku

- The App live link is: [Mildew Alert!](https://mildew-alert-5e353bb60aa4.herokuapp.com/)

- The project was deployed to Heroku using the following steps:

  1. Set the runtime.txt "Python version" to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version. For this project is is 3.12
  2. Build minimum requirements.txt file required for deployment function without exceeding 500MB limit
  3. Set Procfile and setup.sh file 
  4. Log in to Heroku and create an App
  5. At the Deploy tab, select GitHub as the deployment method.
  6. Select your repository name and click Search. Once it is found, click Connect.
  7. Select the branch you want to deploy, then click Deploy Branch.
  8. On any errors inspect log and correct accordingly repeating required steps
  9. Click on View App and test

<br>

## Main Data Analysis and Machine Learning Libraries

- ### Pandas
  - data organization for plot displays in jupyter notebooks
  - data format for table display in streamlit deployment
  - report generation and export to csv for download in live version

- ### Matplotlib
  - plot generation and export as images in jupyter notebooks
  - all plots in the project generated and saved with matplotlib

- ### Seaborn
  - honorable mention, used to display dataset distribution plot as it was much faster than data manipulation to display with matplotlib

- ### TensorFlow + Keras
  - sequential model and all model layers
  - image data conversion to NumPy arrays
  - entirety of machine learning
  - model saving and loading
  - model loading in live version

- ### Scikit-learn
  - honorable mention, only used encoder to convert target categories to binary as part of pre-processing

- ### NumPy
  - base data manipulation methods used by other libraries
  - shaping dataset for use in machine learning
  - store shaped dataset to file(s)
  - load dataset from file(s)
  - calculation for average, variability and difference image in visual study

<br>

## Credits

- most of the structure of this readme file, "business case asessment" and "business requirements" section completely copied from Code Institute's lesson and suggestions material
- mockup image at the start of this file generated by [Techsini](https://techsini.com/multi-mockup/index.php)
- how to work with session state in Streamlit learned from [here](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
- base idea of convolution neural network design is from [tensorflow tutorial](https://www.tensorflow.org/tutorials/images/cnn)
- idea and code for Streamlit multi-page functionality copied from Code Institute's walkthrough project, noted by code comment
- [ChatGPT](https://chatgpt.com/) generated "what is powdery mildew" section on project summary page and html code for "dashboard design" section of this file
- possibly arrogantly crediting myself for putting in effort and writing all rest of code and information without using help even when it was much slower, all for learning purposes


<br>

## Acknowledgements (optional)

- Thank you to Spencer, my mentor, for clarifying how to do this README and boosting my mood with some praise