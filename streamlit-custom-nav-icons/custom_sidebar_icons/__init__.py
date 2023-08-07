import streamlit as st
import time
  
class Set_Nav_Emojis:

    def __init__(self, emojisToRender, uniform_icon_ID="page-title-icon", streamlit_cloud_app=False, my_custom_head_CDN_selector=False, append_CDN_to=""):
        """
        Load in the emojis to show - list of dictionaries. Also the uniform id for all icon ids
        """
        self.emojisToRender = emojisToRender
        self.uniform_icon_ID = uniform_icon_ID
        self.streamlit_cloud_app = streamlit_cloud_app
        self.my_custom_head_CDN_selector = my_custom_head_CDN_selector
        self.append_CDN_to = append_CDN_to

    def create_important_session_state(self):
        """
        Create session variables to highlight that function has run. This will help to remove the iframe created from st.components.v1.html so that space is created in the app.
        """
        if "sideNav" not in st.session_state:
            st.session_state['sideNav'] = False

        if "codeHasRun" not in st.session_state:
            st.session_state['codeHasRun'] = False

    def Load_All_CDNs(self):
        """
        Load all the CDNs for the supported icon libraries. These include:
        - Google-material-symbols
        - Remix icon
        - Tabler Icons
        - Icon-8
        - line-awesome
        """

        linkJS = """
            <script>
                const GoogleEmoji = document.createElement("link");
                GoogleEmoji.href = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0";
                GoogleEmoji.rel = "stylesheet";
                window.top.document.head.appendChild(GoogleEmoji);

                const remixIcon = document.createElement("link");
                remixIcon.href = "https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css";
                remixIcon.rel = "stylesheet";
                window.top.document.head.appendChild(remixIcon);

                const tablerIcons = document.createElement("link");
                tablerIcons.href = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/iconfont/tabler-icons.min.css";
                tablerIcons.rel = "stylesheet";
                window.top.document.head.appendChild(tablerIcons); 

                const tablerIcons_2 = document.createElement("link");
                tablerIcons_2.href ="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css";      
                tablerIcons_2.rel = "stylesheet";
                window.top.document.head.appendChild(tablerIcons_2);   

                const tablerIcons_3 = document.createElement("script")
                tablerIcons_3.src = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons-react/dist/index.umd.min.js"
                window.top.document.head.appendChild(tablerIcons_3) 

                const icon8_line_awesome = document.createElement("link");
                icon8_line_awesome.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/font-awesome-line-awesome/css/all.min.css";
                icon8_line_awesome.rel = "stylesheet";
                window.top.document.head.appendChild(icon8_line_awesome);

                const icon8_line_awesome2 = document.createElement("link");
                icon8_line_awesome2.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css";
                icon8_line_awesome2.rel = "stylesheet";
                window.top.document.head.appendChild(icon8_line_awesome2);

            </script>
        """
        st.components.v1.html(linkJS, height=0, width=0)

    def Load_All_CDNs_to_streamlit_cloud(self):
        query = "iframe[title='streamlitApp']"

        linkJS = f"""
            <script>
                headToAppendIframe = window.top.document.querySelectorAll("{query}")[0].contentDocument.head

                const GoogleEmoji = document.createElement("link");
                GoogleEmoji.href = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0";
                GoogleEmoji.rel = "stylesheet";
                headToAppendIframe.appendChild(GoogleEmoji);

                const remixIcon = document.createElement("link");
                remixIcon.href = "https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css";
                remixIcon.rel = "stylesheet";
                headToAppendIframe.appendChild(remixIcon);

                const tablerIcons = document.createElement("link");
                tablerIcons.href = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/iconfont/tabler-icons.min.css";
                tablerIcons.rel = "stylesheet";
                headToAppendIframe.appendChild(tablerIcons); 

                const tablerIcons_2 = document.createElement("link");
                tablerIcons_2.href ="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css";      
                tablerIcons_2.rel = "stylesheet";
                headToAppendIframe.appendChild(tablerIcons_2);   

                const tablerIcons_3 = document.createElement("script")
                tablerIcons_3.src = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons-react/dist/index.umd.min.js"
                headToAppendIframe.appendChild(tablerIcons_3) 

                const icon8_line_awesome = document.createElement("link");
                icon8_line_awesome.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/font-awesome-line-awesome/css/all.min.css";
                icon8_line_awesome.rel = "stylesheet";
                headToAppendIframe.appendChild(icon8_line_awesome);

                const icon8_line_awesome2 = document.createElement("link");
                icon8_line_awesome2.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css";
                icon8_line_awesome2.rel = "stylesheet";
                headToAppendIframe.appendChild(icon8_line_awesome2);

            </script>
        """
        st.components.v1.html(linkJS, height=0, width=0)

    def custom_query_for_my_app_head_tag_CDN(self):

        linkJS = f"""
            <script>
                headToAppendIframe = {self.append_CDN_to}

                const GoogleEmoji = document.createElement("link");
                GoogleEmoji.href = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0";
                GoogleEmoji.rel = "stylesheet";
                headToAppendIframe.appendChild(GoogleEmoji);

                const remixIcon = document.createElement("link");
                remixIcon.href = "https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css";
                remixIcon.rel = "stylesheet";
                headToAppendIframe.appendChild(remixIcon);

                const tablerIcons = document.createElement("link");
                tablerIcons.href = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/iconfont/tabler-icons.min.css";
                tablerIcons.rel = "stylesheet";
                headToAppendIframe.appendChild(tablerIcons); 

                const tablerIcons_2 = document.createElement("link");
                tablerIcons_2.href ="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css";      
                tablerIcons_2.rel = "stylesheet";
                headToAppendIframe.appendChild(tablerIcons_2);   

                const tablerIcons_3 = document.createElement("script")
                tablerIcons_3.src = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons-react/dist/index.umd.min.js"
                headToAppendIframe.appendChild(tablerIcons_3) 

                const icon8_line_awesome = document.createElement("link");
                icon8_line_awesome.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/font-awesome-line-awesome/css/all.min.css";
                icon8_line_awesome.rel = "stylesheet";
                headToAppendIframe.appendChild(icon8_line_awesome);

                const icon8_line_awesome2 = document.createElement("link");
                icon8_line_awesome2.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css";
                icon8_line_awesome2.rel = "stylesheet";
                headToAppendIframe.appendChild(icon8_line_awesome2);

            </script>
        """
        st.components.v1.html(linkJS, height=0, width=0)
        

    def create_unique_class_for_streamlitTabs(self):
        """
            Need to create a unique identified for the <span></span> tag that contains the navigation title. This is especially important because 
            when using multiple icon libraries together, we need to position the icons next to the title. Without this unique identifier, icons will be added to the same page title.
            For example using the google-material-symbols uses <span> tag to render its icons (can also use <i> too). If we were to combine google-material-symbols and line-awesome icon library,
            when running the loop for these two libraries, javascript will continue to append icons to the first page title instead of going to the next page as it found
            google-material-sybmols icon's <span> first and thus appends the icon to its left instead of the next page title's left. A unique identified prevents this behaviour. 

            We could use Streamlit's starts with `css` but future updates could change this. We want predictability. 

            Also created unique names for other aspects of the sidebar so users can style sidebar as they see fit.
        """
        js = f"""
                <script>
                    sidebar_nav_container = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul');
                    sidebar_nav_parent_el = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li');
                    sidebar_nav_page_title_icon_container_el = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li div');
                    sidebar_nav_page_link = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a');
                    page_links_title = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a span')

                    sidebar_nav_container[0].classList.add('sidebar-nav-list-container-streamlit')
                    sidebar_nav_parent_el.forEach((el) => {{
                        el.classList.add('sidebar-individual-page-container-streamlit')
                    }})

                    sidebar_nav_page_title_icon_container_el.forEach((el) => {{
                        el.classList.add('sidebar-page-title-icon-container-streamlit')
                    }})

                    sidebar_nav_page_link.forEach((el) => {{
                        el.classList.add('sidebar-page-link-container-streamlit')
                    }})

                    page_links_title.forEach((el) => {{
                        el.classList.add('page-title-streamlit')
                    }})
                </script>
            """
        st.components.v1.html(js)

    def create_unique_class_for_streamlitTabs_(self):
        """
        Activate `create_unique_class_for_streamlitTabs()` method with placeholder so that it deletes the iframe on running. 
        """
        placeholder = st.empty()
        with placeholder.container():
            self.create_unique_class_for_streamlitTabs()
            time.sleep(1)
            placeholder.empty() 
        
    
    def tabler_icons(self, data_object, index):
        """
        Function to render icons from tabler icons. For icons, view:https://tabler-icons.io/
        """

        js = f"""
            <script>
                page_title_name = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a span[class*="page-title-streamlit"]')
                const nav_emoji = document.createElement('i');
                nav_emoji.className = '{data_object['iconName']}';
                nav_emoji.id = !!'{data_object['elementID']}'.trim() ? '{data_object['elementID']}' : '{self.uniform_icon_ID}';
                nav_emoji.style = '{data_object['style']}';
                page_title_name[{index}].insertAdjacentElement('beforebegin',nav_emoji);

            </script>

            """

        st.components.v1.html(js)
    
    def Google_material_symbols(self, data_object, index):
        """
        Function to render icons from google-material-symbols. For icons, view:https://fonts.google.com/icons
        """

        js = f"""
            <script>
                
                page_title_name = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a span[class*="page-title-streamlit"]')
                const nav_emoji = document.createElement('i');
                nav_emoji.innerText = '{data_object['iconName']}';
                nav_emoji.className  = 'material-symbols-outlined';
                nav_emoji.id = !!'{data_object['elementID']}'.trim() ? '{data_object['elementID']}' : '{self.uniform_icon_ID}';
                nav_emoji.style = '{data_object['style']}';
                page_title_name[{index}].insertAdjacentElement('beforebegin',nav_emoji);
                
                
            </script>
            """

        st.components.v1.html(js)
    
    def icon_8(self, data_object, index):
        """
        Function to render icons from icon-8. For icons, view: https://icons8.com/icons. If you use this icon package for free, need to reference it somewhere in your app. For more information view: https://icons8.com/license
        """

        js = f"""
        <script>
            page_title_name = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a span[class*="page-title-streamlit"]')
            
            const nav_emoji = document.createElement('img');
            nav_emoji.id = !!'{data_object['elementID']}'.trim() ? '{data_object['elementID']}' : '{self.uniform_icon_ID}';
            nav_emoji.src = '{data_object['emojiObject']['src']}'; 
            nav_emoji.height = '{data_object['emojiObject']['height']}'; 
            nav_emoji.width = '{data_object['emojiObject']['width']}'; 
            nav_emoji.alt = '{data_object['emojiObject']['alt']}';
            nav_emoji.style = '{data_object['style']}';
            page_title_name[{index}].insertAdjacentElement('beforebegin',nav_emoji);
        </script>
            
            """

        st.components.v1.html(js)

    def line_awesome(self, data_object, index):

        """
        Function to render icons from line-awesome. For icons, view: https://icons8.com/line-awesome
        """

        js = f"""
            <script>

                page_title_name = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a span[class*="page-title-streamlit"]')
                const nav_emoji = document.createElement('i');
                nav_emoji.className = '{data_object['iconName']}';
                nav_emoji.id = !!'{data_object['elementID']}'.trim() ? '{data_object['elementID']}' : '{self.uniform_icon_ID}';
                nav_emoji.style = '{data_object['style']}';
                page_title_name[{index}].insertAdjacentElement('beforebegin',nav_emoji);

            </script>
            """

        st.components.v1.html(js)

    def remix_icon(self, data_object, index):
        """
        Function to render icons from remix-icon. For icons, view: https://remixicon.com/
        """

        js = f"""
            <script>
                page_title_name = parent.document.querySelectorAll('[data-testid="stSidebarNav"] ul li a span[class*="page-title-streamlit"]')
                const nav_emoji = document.createElement('i');
                nav_emoji.className = '{data_object['iconName']}';
                nav_emoji.id = !!'{data_object['elementID']}'.trim() ? '{data_object['elementID']}' : '{self.uniform_icon_ID}';
                nav_emoji.style = '{data_object['style']}';
                page_title_name[{index}].insertAdjacentElement('beforebegin',nav_emoji);
            </script>
        """

        st.components.v1.html(js)
    
    def show_me_the_icons_Render(self):
        """
        Render the emojis based on list of objects inputed. 
        - Load in the initiated session state variables to distinguish between the function having being run and not.
        - Create a placeholder container to contain the output components.html iframes to run all the functions in them. This makes it easier to remove it later to make space in the app after their use has been fulfilled (loading emojis). 
        - We also don't need to re-run the function again as the appended elements remain. 
        - Load all the unique element IDs
        - Render emojis and change session states to demonstrate code has been run. 
        - re-run the code from top to bottom so that we can remove the placeholder container that contains the iframe components.
        - Emojis will be loaded thereafter and code will re-run after the page is re-loaded where the code is called. 
        """

        self.create_important_session_state()

        if st.session_state['codeHasRun'] == False:
            placeholder = st.empty()
            if st.session_state['sideNav'] == False:
                with placeholder.container():

                    if self.streamlit_cloud_app == True:
                        self.Load_All_CDNs_to_streamlit_cloud() 
                    elif self.my_custom_head_CDN_selector == True:
                        self.custom_query_for_my_app_head_tag_CDN()
                    else:
                        self.Load_All_CDNs()
                    time.sleep(2)
                    
                    self.create_unique_class_for_streamlitTabs()

                    for data_object, index in zip(self.emojisToRender, range(len(self.emojisToRender))):
                        if data_object['iconLibrary'] == "Google_material_symbols":
                            self.Google_material_symbols(data_object, index)
                        elif data_object['iconLibrary'] == "line_awesome":
                            self.line_awesome(data_object, index)
                        elif data_object['iconLibrary'] == "icon_8":
                            self.icon_8(data_object, index)
                        elif data_object['iconLibrary'] == "remix_icon":
                            self.remix_icon(data_object, index)
                        elif data_object['iconLibrary'] == "tabler_icons":
                            self.tabler_icons(data_object, index) 
                        print(data_object, index)
                    
                    st.session_state['sideNav'] = True 
                    time.sleep(1)
                    st.experimental_rerun()
            else: 
                placeholder.empty()
                st.session_state['codeHasRun'] = True

"""
 -- Example --

emojis_list = [
    {"iconLibrary":"remix_icon", "pageT":"two", "iconName":"ri-verified-badge-fill", "emojiObject":{}, "style":"", "elementID":"",},
    {"iconLibrary":"icon_8", "pageT":"init", "iconName":"settings", "emojiObject":{'src':"https://img.icons8.com/fluency/48/smiling.png", 'height':'50', 'width':'50', 'alt':'smiling'}, "style":"", "elementID":"", },
    {"iconLibrary":"tabler_icons", "pageT":"one", "iconName":"ti ti-adjustments-pin", "emojiObject":{}, "style":"", "elementID":"",},

]
emojisOrender = Set_Nav_Emojis(emojis_list)
emojisOrender.show_me_the_icons_Render()
emojisOrender.create_unique_class_for_streamlitTabs()

"""
