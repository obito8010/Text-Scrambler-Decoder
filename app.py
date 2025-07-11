import streamlit as st
import base64

# Title
st.title("🔐 Text & File Encryptor / Decryptor")

# Encryption function
def encrypt(text):
    encrypted = text.replace("a", "dfg82jr")
    encrypted = encrypted.replace("e", "hskfk7rnv")
    encrypted = encrypted.replace("i", "kjfvnawd8dn")
    encrypted = encrypted.replace("o", "xmzn29qwe")
    encrypted = encrypted.replace("u", "plz90mbvc")
    encrypted = encrypted.replace(" ", "xxspxx")
    return encrypted

# Decryption function
def decrypt(text):
    decrypted = text.replace("xxspxx", " ")
    decrypted = decrypted.replace("plz90mbvc", "u")
    decrypted = decrypted.replace("xmzn29qwe", "o")
    decrypted = decrypted.replace("kjfvnawd8dn", "i")
    decrypted = decrypted.replace("hskfk7rnv", "e")
    decrypted = decrypted.replace("dfg82jr", "a")
    return decrypted

# Text section
st.subheader("📝 Text Input")
text = st.text_area("Enter your text:")
choice = st.radio("Choose an action for text:", ["Encrypt", "Decrypt"])

if st.button("Submit Text"):
    if choice == "Encrypt":
        result = encrypt(text)
        st.success("🔐 Encrypted Text:")
    else:
        result = decrypt(text)
        st.success("🔓 Decrypted Text:")

    st.code(result, language='text')

    # Download button
    b64 = base64.b64encode(result.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="result.txt">📥 Download Result</a>'
    st.markdown(href, unsafe_allow_html=True)

# Divider
st.markdown("---")

# File section
st.subheader("📁 File Input")
uploaded_file = st.file_uploader("Upload a text file (.txt)", type=["txt"])
file_choice = st.radio("Choose an action for file:", ["Encrypt", "Decrypt"])

if uploaded_file is not None:
    file_text = uploaded_file.read().decode("utf-8")
    st.text_area("File Preview", file_text, height=150)

    if st.button("Submit File"):
        if file_choice == "Encrypt":
            processed_file = encrypt(file_text)
            st.success("🔐 File encrypted successfully.")
        else:
            processed_file = decrypt(file_text)
            st.success("🔓 File decrypted successfully.")

        # Download button
        file_b64 = base64.b64encode(processed_file.encode()).decode()
        file_href = f'<a href="data:file/txt;base64,{file_b64}" download="processed_file.txt">📥 Download Processed File</a>'
        st.markdown(file_href, unsafe_allow_html=True)

        # Show content
        st.code(processed_file, language='text')
