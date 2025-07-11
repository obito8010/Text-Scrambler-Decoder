import streamlit as st

# Title
st.title("🔐 Text Encryptor & Decryptor")

# Input
text = st.text_area("Enter your text:")

# Action
choice = st.radio("Choose an action:", ["Encrypt", "Decrypt"])

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

# Perform Action
if st.button("Submit"):
    if choice == "Encrypt":
        result = encrypt(text)
        st.success("🔐 Encrypted Text:")
        st.code(result, language='text')
    else:
        result = decrypt(text)
        st.success("🔓 Decrypted Text:")
        st.code(result, language='text')
