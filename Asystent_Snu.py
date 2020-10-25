from kivymd.app  import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from core import tools
import datetime
  
t = tools()

class Asystent(MDApp):
    nearest_rhytm_point = StringProperty(t.rhytm())
    regularity_of_sleep = StringProperty(t.calculate_correctess_of_sleep_time(t.data['sleep_time'][-1])[0] if len(t.data['sleep_time']) != 0 else "Uzupełnij godzny snu by dowiedzieć sie czy twój sen jest poprawny!")
    if len(t.data['sleep_time']) > 0:
        regularity_of_sleep_bin = ObjectProperty((1,0,0,1) if t.calculate_correctess_of_sleep_time(t.data['sleep_time'][-1])[1] else (0,1,0,1))
    else:
        regularity_of_sleep_bin = ObjectProperty((1,1,1,0))

    
    def build(self):
        #self.t = tools()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.root = Builder.load_file("Asystent.kv")
        
        self.root.ids.user_name.text = str(t.data['name'])
        self.root.ids.user_age.text  = str(t.data['age'])

        if len(t.data['sleep_time']) > 0:
            t.generate_mean_sleep_time_plot()


    def callback_update(self):
        data = {}
        #t = tools()
        time = datetime.datetime.now()
        data['name'] = self.root.ids.user_name.text
        data['age'] = self.root.ids.user_age.text
        data['sex'] = "K" if self.root.ids.user_female.active == True else "M"
        data["sleep_time"] = t.data['sleep_time'] + [[int(self.root.ids.sleep_end.text), int(self.root.ids.sleep_begin.text)]]
        data['date_time'] = t.data['date_time'] + ['{}.{}.{}'.format(time.day, time.month, time.year)]
        t.update(data)

    #def callback_update_dates(self):
    #    data = {}
    #    data['sleep_time'] = t.data['sleep_time'] + [self.root.ids.sleep_end.text]
    #    time = datetime.datetime.now()
    #    data['date_time']  = t.data['date_time'] + ['{}.{}.{}'.format(time.day, time.month, time.year)]
    #    data['name'] = t.data['name']
    #    data['age']  = t.data['age']
    #    data['sex']  = t.data['sex']
    #    t.update(data)

    
Asystent().run()