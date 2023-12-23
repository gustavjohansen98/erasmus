import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.card import card
from streamlit_extras.grid import grid

# 🇪🇺
# 🇫🇮
# 🇵🇱
# 🇵🇹
# 🇩🇰
# 📑 🏠 ↗️

st.set_page_config(
        page_title="Home | SAFE",
        page_icon="🇪🇺",
        layout="centered",
        initial_sidebar_state="expanded",
    )

# add_logo(
#     logo_url="https://static.wixstatic.com/media/9628d6_7940515619a142ea906e8cd16af09c73~mv2.png/v1/fill/w_420,h_103,al_c,lg_1,q_85,enc_auto/logo%20erasmus.png",
#     height=100,
# )

st.image(image="https://static.wixstatic.com/media/9628d6_7940515619a142ea906e8cd16af09c73~mv2.png/v1/fill/w_420,h_103,al_c,lg_1,q_85,enc_auto/logo%20erasmus.png")
# st.title('Welcome to `Erasmus+`')

"""
## Education for Future and Safetey cross-curricular tools for primary schools

_Project co-founded by the European Union under Erasmus+ Programme_
"""

st.header("Partner schools", divider=True)


# poland, finland, portugal, denmark = st.tabs(
#     [
#         "Poland",
#         "Finland",
#         "Portugal",
#         "Denmark"
#     ]
# )

my_grid = grid(2, 2, 2, 2, vertical_align='center')

my_grid.link_button('I Społeczna Szkoła Podstawowa, **Poland** ↗️', 'http://unia.zam.pl/', use_container_width=True)
my_grid.link_button('Emäkosken koulu, **Finland** ↗️', 'https://www.nokiankaupunki.fi/varhaiskasvatus-ja-koulutus/perusopetus/peruskoulut/', use_container_width=True)
my_grid.link_button('Agrupamento de Escolas, **Portugal** ↗️', 'https://www.escolasdevnpaiva.pt/', use_container_width=True)
my_grid.link_button('Provstegårdskolen, **Denmark** ↗️', 'https://provstegaardskolen.aula.dk/', use_container_width=True)

# with my_grid.container():
#     card(
#         title="Provstegaardsskolen",
#         text="Lorem Ipsum dolor sit",
#         image="https://scontent-cph2-1.xx.fbcdn.net/v/t39.30808-1/295074808_503836558209609_4807329987829343954_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=596444&_nc_ohc=nu-x9QqajO4AX9e6JEY&_nc_ht=scontent-cph2-1.xx&oh=00_AfCXYYOJ2FNeVcO7w2z96MQlt0-c9RXALihjc1nJ0ogvsA&oe=658B64EB",
#         url="https://provstegaardskolen.aula.dk/",
#         styles={
#             "card": {
#                 "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
#                 "height": "150px" # <- if you want to set the card height to 300px
#             }
#         }
#     )

# with st.expander(label="Poland"):
#     """
#     School info
#     """
#     st.link_button("website", "https://provstegaardskolen.aula.dk/", use_container_width=True)

# with st.expander(label="Finland"):
#     """
#     School info
#     """
#     st.link_button("website", "https://provstegaardskolen.aula.dk/", use_container_width=True)

# with st.expander(label="Portugal"):
#     """
#     School info
#     """
#     st.link_button("website", "https://provstegaardskolen.aula.dk/", use_container_width=True)

# with st.expander(label="Denmark"):
#     """
#     School info
#     """
#     st.link_button("website", "https://provstegaardskolen.aula.dk/", use_container_width=True)


st.header("About the project", divider=True)

"""
The project 'Personalised Education For Social Activity' is to combine innovative personalized learning approach with entrepreneurial and social education of students with various educational needs and equip teachers with innovative and effective teaching methods.

The main problem the project addresses is that students' social and entrepreneurial awareness is too theoretical, teachers lack effective teaching methods to support such education. Schools lack tools to deal with differentiated needs of students, those with specific learning difficulties and students excelling at chosen fields. Lack of effective solutions to address learners of various abilities makes it harder to introduce effective education in the field of entrepreneurship and social skills.

At the same time, there is growing demand for personalisation of the education process, allowing young people to make the most of their potential and to activate them in community life.

The main project objective is to introduce personalised education integrated with entrepreneurial competences, in particular social ones, to groups of varied abilities and strengths. It is to allow them to develop practical entrepreneurial skills and become more active, to foster innovative, out-of-box thinking and equip schools and teachers with innovative tools.

Providing personalised learning opportunities on international ground will contribute to best practice exchange. Integrating innovative personalized approach to address differentiated educational needs, will not only ensure the development of basic key competences but it will create an entrepreneurial mindset in project participants.

The project is innovative because it will introduce and test out innovative approach to teaching social entrepreneurial skills in personalised school environment. It will make use of the newest technological innovations and tools to create the innovative teaching aid database for partner schools to be implemented and others to follow.

The target groups are teenagers (12-14), for whom social entrepreneurial education intermingled with innovative personal approach is something new and unavailable within the regular school curricula, and their teachers who will learn how to put this idea into practice (at least 150 students, 30 teachers).

Project partners will closely cooperate with local civil society organisations, educational institutions and specialists to make the interconnection between personalised learning approach and entrepreneurial education most effective.

The activities will take place at local, regional and international levels. Workshops for teachers on how to implement personalised learning in groups of varied educational needs, teach entrepreneurial skills (including social ones), workshops for students using activating methods of teaching/learning and studies conducted during mobilities will foster innovative approach to promoting social involvement with the use of social entrepreneurial skills.

Cooperation with local civil society organisations, educational centres and companies will enhance the participants' practical social and entrepreneurial skills and become the basis for future cooperation in the field of responsible citizenship.

As project partners' expertise in fields related to the project is varied, international exchange of good practices is the key to success. The strength of this cooperation lies in the innovative combination of all the elements together: personalised learning, entrepreneurship, social involvement, newest methodologies to activate students of various educational needs.

Tangible results of the project (Best Practice In Personalised Education For Social Entrepreneurship ebook, 'You Can Do It!' educational games, innovative lesson plans) will be disseminated at local, regional and European levels to make sure the project ideas are available for everyone.

A multimedia teaching aid base will be available to all partners and anyone interested.

Erasmus+ Project Results Platform will help show the outcomes of the project, sharing good practice and experience within schools, communities and regions, allowing others to learn from it. The project will bring longer term benefits.

Personalised education will become better known and together with social entrepreneurial elements will become part of school curricula. Cooperation with local civil society organisations will be continued, ensuring effective involvement of young citizens in their community life.

Students will become familiar with culture and natural heritage of other countries and break down barriers and prejudices between nations. They will improve linguistic and IT skills, which will constitute the basis for future cooperation.

Above all, the participants of Erasmus+ 'Personalised Education For Social Activity' project will develop the need to become active European citizens taking responsibility for their social involvement.
"""
