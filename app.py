import streamlit as st
from recommender import load_data, prepare_data, vectorize_data, recommend_jobs

@st.cache_data
def load_and_prepare():
    df = load_data()
    df = prepare_data(df)
    vectorizer, vectors = vectorize_data(df)
    return df, vectorizer, vectors

# Center content using columns
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.title("Job Recommendation System")
    st.markdown("Find the best job matches based on your skills and interests")
    st.markdown("---")  # Divider line
    
    # Load data
    df, vectorizer, vectors = load_and_prepare()
    
    # Input section
    st.markdown("### Enter Your Skills or Interests")
    x = st.text_input("", placeholder="e.g., python data analysis, react frontend, machine learning")
    st.caption("**Try:** 'machine learning tensorflow' or 'react frontend design' or 'devops cloud kubernetes'")

    st.markdown("")  # Add space
    
    # Button
    if st.button('Recommend Jobs', use_container_width=True):
        if x.strip() == "":
            st.warning("Please enter some skills or interests")
        else:
            results = recommend_jobs(x, df, vectorizer, vectors)
            st.success("Here are your top job matches:")
            st.markdown("---")
            for i, job in enumerate(results, 1):
                st.markdown(f"**{i}.** {job}")
