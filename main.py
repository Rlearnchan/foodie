import streamlit as st
from dotenv import load_dotenv
from graph.compile import app

load_dotenv()

st.title("Food Desert Research Assistant")

question = st.text_input("Enter your question:", "How's the definition of food desert changing?")

if st.button("Search"):
    result = app.invoke({"question": question})
    
    # result display
    st.header("Question")
    st.write(result["question"])
    
    st.header("Answer")

    generation = result.get("generation")
    documents = result.get("documents", [])

    if not generation:
        st.write("No answer generated.")
    else:
        st.write(generation)
        
        if documents:
            st.header("Reference Documents")
            for i, doc in enumerate(documents, 1):
                st.subheader(f"Document {i}")
                with st.expander(f"Document {i} Details"):
                    st.write(f"**Source:** {doc.metadata['source']}")
                    st.write(f"**Page:** {doc.metadata['page']}")
                    content = ' '.join(
                        filter(
                            None, 
                            [line.strip() for line in doc.page_content.split('\n')]
                        )
                    )
                    content = ' '.join(content.split())
                    st.write(f"**Content:** {content}")
                    st.divider()
   
