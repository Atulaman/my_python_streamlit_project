import streamlit as st
from PIL import Image

from easter_egg import rickroll

def Galvena_lapa():
    # WELCOME TEXT
    st.markdown("```print('Čau!')```")
    st.markdown('Mēs esam Rīgas Valsts 1. ģimnāzijas programmēšanas novirziena 10. klase!')

    main_image = Image.open('images/main_photo.jpeg')
    st.image(main_image, caption='10.E klase mūsu pirmajā pasakumā Mangaļsalā.')
    st.markdown('Un šajā mājās lapā pēc mūsu klases audzinātājas pieprasījuma Jūs varat mūs iepazīt tuvāk!')

    st.markdown('\n\n\n')
    st.markdown('Varbūt Jums būs noderīgas saites:')
    st.markdown("-  [A.L. apsveikums Ziemassvētkos](https://fulcrum101.github.io/gift_for_teacher/)")
    st.markdown("-  [Mūsu Instagram konts](https://www.instagram.com/rv1g10e/)")
    st.markdown("-  [RV1Ģ Vidusskolēnu domes Instagram konts](https://www.instagram.com/rv1g_vd/)")
    st.markdown("-  [Mūsu skolas kaimiņu Instagram konts](https://www.instagram.com/rv1g10a/)")

    st.markdown('\n\n\n\n\n\n\n')
    password = st.text_input('Secret password', 'ONLY FOR TRUE DEVELOPERS')
    if password == '10E is the best':
        rickroll()

