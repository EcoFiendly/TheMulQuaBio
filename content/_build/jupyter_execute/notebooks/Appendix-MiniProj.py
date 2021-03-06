#!/usr/bin/env python
# coding: utf-8

# # The Computing Miniproject  <a name="Apx:Miniproj"></a>

# We have talked a lot about workflows and confronting models with data. It's time to do something concrete with all the techniques you have been learning.
# 
# The CMEE Miniproject gives you an opportunity to try the "whole nine yards" of developing and implementing a workflow and delivering a "finished product" — where you ask and answer a scientific question in biology (potentially involving multiple sub-questions/hypotheses). It will give you an opportunity to perform a "dry run" of executing your actual dissertation project, and you may use it to trial some of the techniques and/or explore some of the data/theory you might use in your Dissertation project.
# 
# ## Objectives
# 
# **The general question you will address is:** *What mathematical model best fits an empirical dataset?*
# 
# You may think of this as testing a set of alternative hypotheses — every alternative hypothesis is nothing but an alternative model to describe an observed phenomenon, as you will have learned in the lectures on model fitting.
# 
# The Project 
# -----------
# 
# You will choose a dataset and set of alternative models from the options provided to you.
# 
# *Please read the papers in the [Readings](#Readings) section* — these will help orient you in the right direction for tackling your miniproject.
# 
# The Miniproject must satisfy the following criteria (and follow the accompanying guidelines):
# 
# 1. It should employ all the biological computing tools you have learned so far: shell (bash) scripting, git, LaTeX, R, and Python. Using these tools, you will build a workflow that starts with the data and ends with a written report (in LaTeX). How you choose the different tools (e.g., Python vs R) is your choice. This is part of the assessment. 
# 
# 2. *At least* two different models (hypotheses) must be fitted to the data. The models should be fitted and selected using an appropriate method. Specifically, irrespective of the problem/dataset you choose (see below), use Nonlinear Least Squares (NLLS) to fit $\ge 2$ alternative models to data, followed by model selection using AIC and BIC (read the Johnson and Omland 2005 paper). You may choose additional means for model comparison/selection beyond these.*
# 
# 3. The project should be fully reproducible. Write a script that "glues" the workflow together and runs it, from data processing to model fitting to plotting (e.g., in R) to compilation of the LaTeX written report (*More detailed instructions on report below*). Look back at the TheMulQuaBio to see how you would run the different components. For example, we have covered how to run R and compile $\LaTeX$ using the `subprocess` module in Python. The assessor should be able to run just this script to get everything to work without errors. Use Python or to write this main script. If using bash, call it `run_MiniProject.sh` and if using Python, called it  `run_MiniProject.py`.
# 
# *You will be given lectures and practicals on model fitting before you start on your Miniproject.*
# 
# 
# ## The Report
# 
# The report should,
# 
# * be written in LaTeX  using the article document class, in 11pt (any font will do, within reason!).
# 
# * be double-spaced, with *continuous* line numbers.
# 
# * have a title, author name with affiliation and wordcount (next point) on a separate title page.
# 
# * have an introduction with objectives of the study, and appropriate additional sections such as methods, data, results, discussion, etc.
# 
# * should contain in the *Methods* a sub-section called "Computing tools" which states briefly how each of the three scripting language (bash, R, Python) and what packages within them were used and a justification of why.
# 
# * must contain $\leq$3500 words *excluding the contents of the title page, references, and Figure or Table captions+legends*; there should be a word count at the beginning of the document (typically using the `texcount` package).
# 
# * have references properly cited in text and formatted in a list using bibtex.
# 
# For the writeup, you probably should read the *general* (*not* word count, formatting etc.) dissertation writing guidelines given in the Silwood Masters Student Guidebook.
# 
# Submission
# ----------
# 
# Add, commit and push all your work to your bitbucket repository using a directory called `MiniProject` at the same level as the Week1, Week2 etc. directories, by the Miniproject deadline given in your course guidebook.
# 
# At this stage you are not going to be told you how to organize your project — that's part of the marking criteria (see next section).
# 
# Marking criteria
# ----------------
# 
# *Equal weightage will be given to the code+workflow and writeup components — each component will be marked to a max of 100 pts and then rescaled to a single mark / 100 using equal weightage*
# 
# The assessor will be looking for the following while assessing your submission:
# 
# * A well-organized project where code, results, data, etc., are easy to locate, inspect, and use. In the project's README also include:
# 
#     * Any dependencies or special packages the user/marker should be aware of
# 
#     * What each package you used is for
# 
#     * Version of each language used
# 
# * A project that runs smoothly, without any errors once the appropriate script (i.e., `run_MiniProject.py` or `run_MiniProject.sh`) is called. 
# 
# * A report that contains all the components indicated above in "The Report" subsection, with some original thought and synthesis in the **Introduction** and **Discussion** sections.
# 
# * Quality of the presentation of the graphics and tables in your report, as well as any plots showing model fits to the data.
# 
# * The marking criteria you may refer to is the [summative marking criteria](./MARKING_CRITERIA.pdf).
# 
# 
# The Model Fitting Problems
# --------------------------
# 
# You can pick from one of the following three options. 
# 
# ### Thermal Performance Curves
# 
# #### The Question 
# 
# *How well do different mathematical models, e.g., based upon biochemical (mechanistic) principles  vs. phenomenological ones, fit to the thermal responses of metabolic traits?*
# 
# This is currently a "hot" (no pun intended!) topic in biology. On the *ecological side*, because the temperature-dependence of metabolic rate sets the rate of intrinsic $r_\text{max}$ (papers by Savage et al., Brown et al.) as well as interactions between species, it has a strong effect on population dynamics. In this context, note that 99.9% of life on earth is ectothermic! On the *evolutionary side*, the temperature-dependence of fitness and species interactions also means that warmer environments may have stronger rates of evolution. This may be compounded by the fact that mutation rates may also increase with temperature (papers by Gillooly et al.).
# 
# #### The Data
# 
# The dataset is called `ThermRespData.csv`. It contains a subset of the full "BioTraits" database. This subset contains hundreds of "thermal responses" for growth, respiration and photosynthesis rates in plants and bacteria (both aquatic and terrestrial). These data were collected through lab experiments across the world, and compiled by various people over the years. The field names are defined in a file called `BiotraitsTemplateDescription.pdf`, also in the `data` directory. The two main fields of interest are `OriginalTraitValue` (the trait values responding to temperature), and `ConTemp` (the temperature). Individual thermal response curves can be identified by `ID` values --- each `ID` corresponds to one thermal performance curve.

# In[1]:


# Some imports to explore the datasets in Python
import pandas as pd
import scipy as sc
import matplotlib.pylab as pl
import seaborn as sns # You might need to install this (e.g., sudo pip install seaborn)


# Let's have a look at the data:

# In[54]:


data = pd.read_csv("../data/ThermRespData.csv")
print("Loaded {} columns.".format(len(data.columns.values)))


# In[55]:


data.head()


# In[56]:


print(data.columns.values)


# In[57]:


print(data.OriginalTraitUnit.unique()) #units of the response variable 


# In[58]:


print(data.ConTempUnit.unique()) #units of the independent variable 


# In[59]:


print(data.ID.unique()) #units of the independent variable 


# In[60]:


data_subset = data[data['ID']==110]
data_subset.head()


# In[61]:


sns.lmplot("ConTemp", "OriginalTraitValue", data=data_subset, fit_reg=False) # you may ignore the warning taht appears below


# ### The Models
# 
# *All the following parameters and variables are in SI units*.
# 
# There are multiple models that might best describe these data. The simplest are the general quadratic and cubic polynomial models:
# 
# $$\label{eq:quad}
#     B = B_0 + B_1 x + B_2 x^2
# $$
# 
# 
# $$\label{eq:cubic}
#     B = B_0 + B_1 x + B_2 x^2 + B_3 x^3
# $$
# 
# These are phenomenological models, with the parameters $B_0$, $B_1$, $B_2$ and $B_3$ lacking any mechanistic interpretation. $x$ is the independent variable (in this case Temperature, $T$) 
# 
# Another phenomenological model option is the Briere model:
# 
# $$B = B_0 T (T-T_0) \sqrt{T_m-T}$$
# 
# Where $T$ is temperature, $T_0$ and $T_m$ are the minimum and maximum feasible temperatures for the trait (below or above which the traits goes to zero), and $B_0$ is a normalization constant.  
# 
# In contrast, the Schoolfield model (Schoolfield et al 1981) is a mechanistic option that is based upon thermodynamics and enzyme kinetics:
# 
# $$\label{eq:schoolf}
#     B = \frac{B_0 e^{\frac{-E}{k} (\frac{1}{T} - \frac{1}{283.15})}}
#     { 1 + e^{\frac{E_l}{k} (\frac{1}{T_l} - \frac{1}{T})} + 
#     e^{\frac{E_h}{k} (\frac{1}{T_h} - \frac{1}{T})}}
# $$
# 
# *Please also have a look at the Delong et al 2017 paper, which lists this and other mechanistic TPC models* (see [Readings](#Readings)). You may choose additional models listed in that paper for comparison, if you want.
# 
# Here, $k$ is the Boltzmann constant ($8.617 \times 10^{-5}$ eV $\cdot$ K$^{-1}$), $B$ the value of the trait at a given temperature $T$ (K) (K = $^\circ$C + 273.15), while $B_0$ is the trait value at 283.15 K (10$^\circ$C) which stands for the value of the growth rate at low temperature and controls the vertical offset of the curve. $E_l$ is the enzyme's low-temperature de-activation energy (eV) which controls the behavior of the enzyme (and the curve) at very low temperatures, and $T_l$ is the at which the enzyme is 50% low-temperature deactivated. $E_h$ is the
# enzyme's high-temperature de-activation energy (eV) which controls the behavior of the enzyme (and the curve) at very high temperatures, and $T_h$ is the at which the enzyme is 50% high-temperature deactivated. $E$ is the activation energy (eV) which controls the rise of the curve up to the peak in the "normal operating range" for the enzyme (below the peak of the curve and above $T_h$).
# 
# ---
# ![image](./graphics/SchoolfEx.png)
# <small> <center>Example of the Sharpe-Schoolfield eqn, that is,  \ref{eq:quad} and \ref{eq:cubic}, . \ref{eq:schoolf}) fitted to the thermal response curve of a metabolic trait $x$ with resource abundance. 
#     </center> </small>
# 
# ---
# 
# In many cases, a simplified Schoolfield model would be more appropriate for thermal response data, because low temperature inactivation is weak, or is undetectable in the data because low-temperature measurements were not made.
# 
# $$\label{eq:schoolfH}
#       B = \frac{B_0 e^{\frac{-E}{k} (\frac{1}{T} - \frac{1}{283.15})}}
#     { 1 +  e^{\frac{E_h}{k} (\frac{1}{T_h} - \frac{1}{T})}}
# $$
# 
# In other cases, a different simplified Schoolfield model would be more appropriate, because high temperature inactivation was not detectable in the data because measurements were not made at sufficiently high temperatures:
# 
# $$\label{eq:schoolfL}
#       B = \frac{B_0 e^{\frac{-E}{k} (\frac{1}{T} - \frac{1}{283.15})}}
#     { 1 +  e^{\frac{E_l}{k} (\frac{1}{T_l} - \frac{1}{T})}}
# $$
# 
# Note that the cubic model (Equation \ref{eq:cubic}) has the same number of parameters as the the reduced Schoolfield models (eq. \ref{eq:schoolfH} & \ref{eq:schoolfL}). Also, the temperature parameter ($T$) of the cubic model (Equation \ref{eq:cubic}) is in $^\circ$C, whereas the Temperature parameter in the Schoolfield model is in K.
# 
# ## Functional Responses
# 
# ### The Question 
# 
# *How well do different mathematical models, e.g., based upon foraging theory (mechanistic) principles  vs. phenomenological ones, fit to functional responses data across species?*
# 
# In ecological parlance, a functional response is the relationship between a consumer's (e.g., predator) biomass consumption rate and abundance of the target resource (e.g., prey). Functional responses arise from fundamental biological and physical constraints on consumer-resource interactions (e.g., Holling 1959, Pawar et al, 2012), and determine the rate of biomass flow between species in ecosystems across the full scale of sizes, from the smallest (e.g., microbes) to the largest (e.g., blue whales). Functional responses also play a key sole in determining the stability (responses to perturbations) of the food webs that underpin ecosystems.
# 
# ### The Data
# 
# The dataset is called `CRat.csv`. It contains measurements of rates of consumption of a single resource (e.g., prey, plants) species' by a consumer species (e.g., predators, grazers). These data were collected through lab and field experiments across the world. The field names are defined in a file called `BiotraitsTemplateDescription.pdf`, also in the `data` directory. The two main fields of interest are `N_TraitValue` (The number of resources consumed per consumer per unit time), and `ResDensity` (the resource abundance). Individual functional response curves can be identified by `ID` values --- each `ID` corresponds to one curve. Or you can reconstruct them as unique combinations of `Citation` (where the functional response dataset came from), `ConTaxa` (consumer species ID), `ResTaxa` (resource species ID).

# Let's have a look at the data:

# In[11]:


data = pd.read_csv("../data/CRat.csv")
print("Loaded {} columns.".format(len(data.columns.values)))


# In[12]:


data.head()


# In[13]:


print(data.columns.values)


# In[14]:


print(data.TraitUnit.unique()) #units of the response variable 


# In[15]:


print(data.ResDensityUnit.unique()) #units of the independent variable 


# In[16]:


print(data.ID.unique()) #units of the independent variable 


# In[17]:


data_subset = data[data['ID']==39982]
data_subset.head()


# In[18]:


sns.lmplot("ResDensity", "N_TraitValue", data=data_subset, fit_reg=False)


# ### The Models
# 
# *All the following parameters and variables are in SI units*.
# 
# The fundamental measure of interest (the response variable) is consumption rate ($c$). This is expressed in terms of biomass quantity or number of individuals of resource consumed *per unit time per unit consumer* (so units of Mass (or Individuals) / Time). 
# 
# Again, the simplest mathematical models you can use are the phenomenological quadratic and cubic polynomial models, that is eqns. \ref{eq:quad} and \ref{eq:cubic} (replace $x$ with resource abundance).
# 
# Then, there is the more mechanistic Holling Type II model (Holling, 1959):
# 
# $$\label{eq:FR_II}
#       c = \frac{a x_R}{1 + h a x_R}
# $$
# 
# Here, $x_R$ is resource density (Mass / Area or Volume), $a$ is consumer's search rate (Area or Volume / Time ), and  $h$ is handling time of the consumer for that resource (time taken to overpower and ingest it). 
# 
# Below is an example FR curve from the dataset you have been given with the Type II model fitted to it.  
# 
# ---
# ![image](./graphics/3_FR.svg)
# <small>  <center> Example of the a Type II model (eqn. \ref{eq:FR_II}) fitted to a functional response of a consumer on a resource. 
# </center> </small>
# 
# ---
# 
# There is also the less-mechanistic "generalized" functional response model:  
# 
# $$\label{eq:FR_gen}
#       c = \frac{a x_R^{q + 1}}{1 + h a x_R^{q + 1}}
# $$
# 	   
# Where everything is same as \ref{eq:FR_II}, but the additional parameter $q$ (dimensionless) is a shape parameter that allows the shape of the response to be more flexible/variable, from "Type I" to "Type III". This model is less mechanistic because it includes a phenomenological parameter $q$ which does not have a formal biological meaning. Note that if $q=0$, eqn (\ref{eq:FR_gen} becomes same as the Type II model (eqn. \ref{eq:FR_II})). 
# 
# ---
# ![image](./graphics/FR.svg)
# <small> <center> The range of functional responses captured by the generalized functional response model (eqn. \ref{eq:FR_gen}). 
# </center>
# </small>
# 
# ---
# 
# There are other models for functional responses as well (some more mechanistic), that define parameters of the functional response in terms of body size of predator and prey (Pawar et al 2012).  
# 
# 
# ## Population Growth
# 
# ### The Question 
# 
# *How well do different mathematical models, e.g., based upon population growth (mechanistic) theory  vs. phenomenological ones, fit to functional responses data across species?*
# 
# Fluctuations in the abundance (density) of single populations may play a crucial role in ecosystem dynamics and emergent functional characteristics, such as rates of carbon fixation or disease transmission. A population grows exponentially while its abundance is low and resources are not limiting (the Malthusian principle). This growth then slows and eventually stops as resources become limiting. There may also be a time lag before the population growth really takes off at the start. We will focus on microbial (specifically, bacterial) growth rates. Bacterial growth in batch culture follows a distinct set of phases; lag phase, exponential phase and stationary phase. During the lag phase a suite of transcriptional machinery is activated, including genes involved in nutrient uptake and metabolic changes, as bacteria prepare for growth. During the exponential growth phase, bacteria divide at a constant rate, the population doubling with each generation. When the carrying capacity of the media is reached, growth slows and the number of cells in the culture stabilises, beginning the stationary phase. Traditionally, microbial growth rates were measured by plotting cell numbers or culture density against time on a semi-log graph and fitting a straight line through the exponential growth phase &ndash; the slope of the line gives the maximum growth rate ($r_{max}$). Models have since been developed which we can use to describe the whole sigmoidal bacterial growth curve. 
# 
# ### The Data
# 
# The dataset is called `LogisticGrowthData.csv`. It contains measurements of change in biomass or number of cells of microbes over time. These data were collected through lab experiments across the world. The field names are defined in a file called  `LogisticGrowthMetaData.csv`, also in the `data` directory. The two main fields of interest are `PopBio` (abundance), and `Time`. Single population growth rate curves can be identified by as unique  temperature-species-medium-citation-replicate combinations (concatenate them to get a new string variable that identifies unique growth curves).
# 
# Let's have a look at the data:

# In[19]:


data = pd.read_csv("../data/LogisticGrowthData.csv")
print("Loaded {} columns.".format(len(data.columns.values)))


# In[22]:


print(data.columns.values)


# In[20]:


pd.read_csv("../data/LogisticGrowthMetaData.csv")


# In[21]:


data.head()


# In[23]:


print(data.PopBio_units.unique()) #units of the response variable 


# In[24]:


print(data.Time_units.unique()) #units of the independent variable 


# Unlike the previous two datasets there are no ID coulmns, so you will have to  infer single growth curves by combining `Species`, `Medium`, `Temp` and `Citation` columns (each species-medium-citation combination is unique):

# In[44]:


data.insert(0, "ID", data.Species + "_" + data.Temp.map(str) + "_" + data.Medium + "_" + data.Citation)


# Note that the `map()` method coverts temperature values to string (`str`) for concatenation.

# In[46]:


print(data.ID.unique()) #units of the independent variable 


# These are rather ungainly IDs, so you might want to replace them with numbers!

# In[47]:


data_subset = data[data['ID']=='Chryseobacterium.balustinum_5_TSB_Bae, Y.M., Zheng, L., Hyun, J.E., Jung, K.S., Heu, S. and Lee, S.Y., 2014. Growth characteristics and biofilm formation of various spoilage bacteria isolated from fresh produce. Journal of food science, 79(10), pp.M2072-M2080.']
data_subset.head()


# In[49]:


sns.lmplot("Time", "PopBio", data = data_subset, fit_reg = False) # will give warning - you can ignore it


# ### The Models
# 
# Yet again, the simplest mathematical models you can use are the phenomenological quadratic and cubic polynomial models, that is eqns. 1 and 2 above (replace $x$ with Time). A Polynomial model may be able to capture decline in population size after some maximum value (the carrying capacity) has been reached (the "death phase" of population growth).For mechanistic models of population, growth, have a look at the Model fitting notebook's [section on this](./Appendix-ModelFitting.ipynb#Population-growth-rate-example).
# 
# ---
# 
# ![image](./graphics/Pop_Grow.svg)
# <small> <center> An example population growth curve dataset to which the modified Gompertz model (Zwietering et. al., 1990) has been fitted.
# </center></small>
# 
# (See the [Model fitting notebook](./20-ModelFitting.ipynb) for more information)
# 
# ---
# 
# 
# ## Additional models and questions you can tackle
# 
# In all three options above, you may try to tackle fitting to additional models you find in the literature. [Some readings](#Readings) have been provided for each of the three data types. In addtion, you may wish to tackle some other hypotheses or explore patterns by considering additional covariates. For example, 
# 
# *Do different models fit different types of thermal performance curves (e.g., Photosynthesis vs Respiration)?* 
# 
# *Do different taxa show different functional responses?*
# 
# *Does temperature or taxon identity affect which population growth rate model fits best?*
# 
# You may also want to revisit the results of another paper that has done comparisons of the models you have chosen with your new dataset. 

# ## Suggested Workflow
# 
# You will build a workflow that starts with the data and ends with a report written in LaTeX. I suggest the following components and sequence in your workflow (you may choose to do it differently):
# 
# ### Data preparation script 
# 
# First, a script that imports the data and prepares it for NLLS fitting. This may be in Python or R, and will typically have the following features:
# 
# * Creates unique ids so that you can identify unique datasets (e.g., single thermal responses or functional responses). *This may not always be necessary because your data might already contain a field that delineates single curves (e.g., an `ID` field/column)* 
# * Filters out datasets with less than $x$ data points, where $x$ is the minimum number of data points needed to fit the models. Note that this step is not necessary because in any case, the model fitting (or estimation of goodness of fit statistics) will fail for datasets with small sample sizes anyway, and you can then filter these datasets *after* the NLLS fitting script (see below) has finished running and you are in the analysis phase.  
# * Deals with missing, and other problematic data values.
# * Saves the modified data to one or more csv file(s).
# 
# ### NLLS fitting script
# 
# A separate script that does the NLLS fitting. For example, it may have the following features: 
# 
# * Opens the (new, modified) dataset from previous step.
# 
# * Calculates [starting values](more on this [below](#Obtaining-starting-values)). 
# 
# * Does the NLLS fitting.
#     * If you choose Python for this use `lmfit` (look up submodules `minimize`, `Parameters`, `Parameter`, and `report_fit`. *Have a look through* <http://lmfit.github.io/lmfit-py>, especially <http://lmfit.github.io/lmfit-py/fitting.html#minimize> . You will have to install `lmfit` using `pip` or `easy_install`  (use sudo mode). Lots if examples of using lmfit online.
#     * If you choose `R`, examples are [here](Appendix-ModelFitting.ipynb). 
#     
# * Uses the `try` construct because not all runs will converge: for Python, see [this](https://docs.python.org/3.6/tutorial/errors.html); for R, [recall this](07-R.ipynb#Errors-and-Debugging). *The more data curves you are able to fit, the better — that is part of the challenge*
# 
# * Calculates AIC, BIC, R$^{2}$, and other statistical measures of model fit (you decide what you want to include)
# 
# * Exports the results to a csv that the [final plotting script](#Final-plotting-script) can read.
# 
# #### Obtaining starting values 
# 
# The main challenge for NLLS fitting is finding starting values. Ideally, you should determine starting values specific to each dataset (e.g., single thermal performance, functional response, or population growth rate curve) that you are trying to fit a model to. To do so, understanding how each parameter in the model corresponds to features of the actual data is key. For example, in the Gompertz population growth rate model(eq. \ref{eq:Gompertz}), your starting values generator would essentially be an algorithm which, for each dataset,   
# *  Calculates a starting value for $r_{max}$ by searching for the steepest slope of the growth curve using the first few data points (fitting a straight line using OLS)
# * Calculates a starting value of $t_{lag}$ by intersecting the fitted line with the x (time)-axis 
# * Calculates a starting value for the asymptote $A$ as the highest data (abundance) value in the dataset. 
# 
# In general, a good strategy to optimize fits (and maximize how many dataseta are successfully fitted to a non-linear model) is to not sample starting values from a distribution. For example, you can choose a gaussian (high confidence in mean of parameter) or a uniform distribution (low confidence in mean, high confidence in the range of values that the parameter can take) with the mean being the value you inferred from the data.
# 
# *We suggest you write a separate script/module/function that calculates starting values for the model parameters.*  
# 
# ### Final plotting and analysis script  
# 
# Next, you can import the results from the previous step and plot every curve with the two (or more) models (or none, if nothing converges) overlaid. Doing this will help you identify poor fits visually and help you decide whether the previous, NLLS fitting script can be further optimized (e.g., by improving the starting values generator). All plots should be saved in a single separate sub-directory. This script will also perform any analyses of the results of the Model fitting, for example to summarize which model(s) fit(s) best, and address any biological questions involving co-variates.    
# 
# ### Report compiling script
# 
# Then comes the $\LaTeX$ source code and a (typically, Bash) script that compiles it. 
# 
# ### A single script to run them all
# 
# Finally, write a Python or Bash script called `run_MiniProject.py` or `run_MiniProject.sh` respectively, which runs the whole project, right down to compilation of the LaTeX  document.
# 
# ## Getting started 
# 
# Doing all this may seem a bit scary at the start. However, if you approach the problem systematically and methodically, you will soon be on your way. 
# 
# Here are some suggested first steps to get started:
# 
# * Explore the data in R or Python (e.g., using Jupyter). 
# 
# * Write a preliminary version of the plotting script without the fitted models overlaid. That will also give you a feel for the data and allow you to see (literally) what shapes the curves can take.
# 
# * Explore the models you will be fitting. Basically, be able to plot them. Write them as functions in your Python/R script (you can then re-use these functions in your NLLS fitting script as well). Then do some plotting of the functions (you can suppress or sandbox those code lines for exploratory plotting of the functions in the final product).
# 
# * Figure out, using a minimal example (say, with one, "nice-looking" thermal performance, functional response, or population growth curve/dataset) to see how the NLLS fitting package and its commands work. This is your minimal example
# 
# * next, write a loop over all unique datasets (data curves) using the `try` to catch errors in case the fitting doesn't converge.
# 
# *One thing to note is that you may need to do the NLLS fitting on the logarithm of the function (and therefore, the data) to facilitate convergence.*

# ## Readings
# 
# Many of these papers are in pdf format in the Readings directory on TheMulQuaBio repository.
# 
# ### General
# 
# * Levins, R. (1966) The strategy of model building in population biology. Am. Sci. 54, 421–431.
# 
# * Johnson, J. B. & Omland, K. S. (2004) Model selection in ecology and evolution. Trends Ecol. Evol. 19, 101–108.
# 
# * Motulsky, H. & Christopoulos A. (2004) Fitting models to biological data using linear and nonlinear regression: a practical guide to curve fitting. Oxford University Press, USA. 
# 
# * Bolker, B. M. et al. (2013) Strategies for fitting nonlinear ecological models in R, AD Model Builder, and BUGS. Methods Ecol. Evol. 4, 501–512.
#     
# 
# ### Thermal Performance Curves
# 
# * Schoolfield, R. M., P. J H Sharpe, and C. E. Magnuson. 1981. Non-Linear Regression of Biological Temperature-Dependent Rate Models Based on Absolute Reaction-Rate Theory. Journal of Theoretical Biology 88 (4): 719–31. https://doi.org/10.1016/0022-5193(81)90246-0.
# 
# * Zwietering, M. H.,  J. T de Koos, B. E. Hasenack, J. C. de Witt,  and K. van't Riet. 1991. Modeling of bacterial growth as a function of temperature. Appl. Environ. Microbiol. 57, 1094–101.
# 
# * Dell, A. I., S. Pawar, and V. M. Savage. 2011. Systematic Variation in the Temperature Dependence of Physiological and Ecological Traits. Proceedings of the National Academy of Sciences of the United States of America 108 (26): 10591–10596. https://doi.org/doi: 10.1073/pnas.1015178108.
# 
# * DeLong, J. P., J. P. Gibert, T. M. Luhring, G. Bachman, B. Reed, A. Neyer, and K. L. Montooth. 2017. The Combined Effects of Reactant Kinetics and Enzyme Stability Explain the Temperature Dependence of Metabolic Rates. Ecology and Evolution 7 (11): 3940–50. https://doi.org/10.1002/ece3.2955.
# 
# ### Functional responses
# 
# * Holling, C. S. 1959. Some Characteristics of Simple Types of Predation and Parasitism. The Canadian Entomologist 91 (7): 385–98. https://doi.org/10.4039/Ent91385-7.
# 
# * Holling, C S. 1966. The Functional Response of Invertebrate Predators to Prey Density. Mem. Entomol. Soc. Canada 48 (48): 1–86.
# 
# * Aljetlawi, A. A., E. Sparrevik, and K. Leonardsson. 2004. Prey-predator size-dependent functional response: derivation and rescaling to the real world. J. Anim. Ecol. 73, 239–252.
# 
# * Jeschke, J. M.,  M. Kopp & R. Tollrian. 2002. Predator functional responses: Discriminating between handling and digesting prey. Ecol. Monogr. 72, 95–112.
# 
# * Pawar, S., A. I. Dell, and V. M. Savage. 2012. Dimensionality of Consumer Search Space Drives Trophic Interaction Strengths. Nature 486 (7404): 485–89. https://doi.org/10.1038/nature11131.
# 
# * Pritchard, D. W., R. A. Paterson, H. C. Bovy, and D. Barrios-O'Neill. 2017. frair: an R package for fitting and comparing consumer functional responses. Methods Ecol. Evol. 8, 1528–1534.
# 
# ### Population Growth
# 
# * Zwietering, M. H., I. Jongenburger, F. M. Rombouts, and K. Van't Riet. 1990. Modeling of the Bacterial Growth Curve. Applied and Environmental Microbiology 56 (6): 1875–81.
# 
# * Buchanan, R. L., R. C. Whiting, and W. C. Damert. 1997. When Is Simple Good Enough: A Comparison of the Gompertz, Baranyi, and Three-Phase Linear Models for Fitting Bacterial Growth Curves. Food Microbiology 14 (4): 313–26. https://doi.org/10.1006/fmic.1997.0125.
# 
# * Grijspeerdt, K. and P. Vanrolleghem. 1999. Estimating the parameters of the Baranyi model for bacterial growth. Food Microbiol. 16, 593–605.
# 
# * Micha, P., and M. G. Corradini. 2011. Microbial Growth Curves: What the Models Tell Us and What They Cannot. Critical Reviews in Food Science and Nutrition. https://doi.org/10.1080/10408398.2011.570463.
