## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
- The dataset contains 4208 images; 2104 of healthy cherry leaves and 2104 of cherry leaves with powdery mildew, taken from the client's crop fields. Powdery mildew is a fungal disease that affects many plant species.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- Cherry leaves with powdery mildew have visual signs
    - average image of healthy leaf differs from average image of a leaf with powdery mildew

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business requirement 1: Data visualization
    - As a client I want to see mean and standard deviaton images for both healthy and infected cherry leaves, so that I can confirm visual difference
    - As a client I want to see the difference between average image of a healthy leaf and an average image of infected cherry leaf, so that I can confirm visual difference
    - As a client I want to see an image montage of dataset images for both healthy and infected leaves, so that I can confirm correct data input

- Business requirement 2: Data classification
    - As a client I want to have a machine learning model that distinguishes healthy from infected leaves quickly on multiple leaf image input, so that I can speed up diagnosing and treatment procedure

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

### Page 1: Quick project summary

  - Status element 1
    - General Information
    - Project dataset information

  - Status element 2
    - Business requirements

  - Status element 3
    - Link to more information

### Page 2: Cherry leaf visualizer

  - Expander 1 
    - Average and variability images

  - Expander 2 
    - Differences between healthy and infected average images

  - Expander 3 
    - Image montage

### Page 3: Powdery mildew classifier

  - Status element
    - Usage description

  - File uploader
    - Allow multiple image upload

  - Button 1
    - Run ML classifier model on uploaded images and display results
    - Display table showing uploaded images and ML model classifications

  - Button 2
    - Generate table with image names and ML model classifications with option to download

### Page 4: Project Hypothesis and Validation

- TODO: self-explanatory by page name

### Page 5: ML Performance Metrics

- TODO: descriptive performance metrics

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.