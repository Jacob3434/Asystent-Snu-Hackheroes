from kivymd.app  import MDApp
from kivy.lang import Builder
from core import tools
  

class Asystent(MDApp):

    
    def build(self):
        self.t = tools()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.root = Builder.load_file("Asystent.kv")
        
        self.root.ids.user_name.text = str(self.t.data['name'])
        self.root.ids.user_age.text = str(self.t.data['age'])


    def callback_update(self):
        data = {}
        t = tools()
        data['name'] = self.root.ids.user_name.text
        data['age'] = self.root.ids.user_age.text
        data['sex'] = "K" if self.root.ids.user_female.active == True else "M"
        data["sleep_time"] = t.data['sleep_time']
        data['date_time'] = t.data['date_time']
        print(data)
        self.t.update(data)

    
Asystent().run()
