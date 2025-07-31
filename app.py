#import necessary libraries

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit app to visualize NDVI data
st.title("Chennai Crop Health Dashboard")
ndvi = np.load("data/final_data/ndvi.npy")                      # load NDVI data
fig, ax = plt.subplots()                             # create a figure and axes
im = ax.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1) #create an image plot
plt.colorbar(im, label="NDVI" )                       # add a colorbar
ax.set_title("NDVI Map for Chennai")                 # set the title of the plot
st.pyplot(fig)                                       # display the plot as a Streamlit app
st.write("Green = Healthy vegetation (0.6–1), Yellow = Sparse (0.2–0.6), Red = Soil/Water (<0.2)")