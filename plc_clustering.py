import streamlit as st
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer

def visualize_clusters(sentences):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences).toarray()

    pca = PCA(n_components=2).fit_transform(X)
    tsne = TSNE(n_components=2, perplexity=5).fit_transform(X)

    fig1, ax1 = plt.subplots()
    ax1.scatter(pca[:, 0], pca[:, 1])
    ax1.set_title("PCA Projection")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.scatter(tsne[:, 0], tsne[:, 1])
    ax2.set_title("t-SNE Projection")
    st.pyplot(fig2)