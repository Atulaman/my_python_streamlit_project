import streamlit as st

from galvena import Galvena_lapa
from citati import Citati_lapa
from galerija import Galerija_lapa
from k_mikla import k_mikla_lapa

def main():
    st.set_page_config(
        page_title="E-Avīze",
        page_icon="🧊"
    )

    st.title('E-Avīze')
    st.caption('10E klases avīze')
    st.sidebar.title("Sadaļa")
    menu = "Galvenā"
    menu = st.sidebar.selectbox("Izvēlāties, kādu sadaļu Jūs gribat aplūkot.",
                                    ["Galvenā", "Notikumi", "Intervijas", "Fakti", "Citāti", "Joki", "Krustvārdu mīkla", "Galerija","Pielikums"])
    if menu == "Galvenā":
        Galvena_lapa()
    elif menu == "Citāti":
        Citati_lapa()
    elif menu == "Galerija":
        Galerija_lapa()
    elif menu == 'Krustvārdu mīkla':
        k_mikla_lapa()


if __name__ == '__main__':
    main()