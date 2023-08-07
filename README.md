# Sidebar-nav-custom-icons-streamlit
Add custom icons to your streamlit sidebar navigation. 

```python
import streamlit as st
from custom_sidebar_icons import Set_Nav_Emojis as set_Nav
#Icon libraries this supports
# - "https://icons8.com/icons/",
# - "https://remixicon.com/",
# - "https://icons8.com/line-awesome",
# - "https://tabler-icons.io/",
# - "https://fonts.google.com/icons", 

# Can have a look at source code and add support for more

# When loading from local file or from html without iframe or some container
emojisOrender = set_Nav(emojis_list)
emojisOrender.show_me_the_icons_Render()
# When loading from streamlit Cloud - app loaded in container (iframe)
emojisOrender = set_Nav(emojis_list, streamlit_cloud_app=True)
emojisOrender.show_me_the_icons_Render()
# When loading app from some other cloud deploy container
append_CDN_to = """
                window.top.document.querySelectorAll("iframe[title='streamlitApp']")[0].contentDocument.head
                """
emojisOrender = set_Nav(emojis_list, my_custom_head_CDN_selector=True, append_CDN_to=append_CDN_to)
emojisOrender.show_me_the_icons_Render()

```
