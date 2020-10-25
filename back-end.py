import json
import matplotlib.pyplot as plt
import datetime

class tools():
    def __init__(self):
        self.path = 'data.json'
        with open(self.path) as json_file:
            self.data = dict(json.load(json_file))
            
    def update(self, dat):
        self.data = dat
        with open(self.path, "w") as json_file:
            json.dump(self.data, json_file)
            
            
    def calculate_correctess_of_sleep_time(self, sleep_time):
        if self.data['years'] in range(13):
            correct_hours = [9,10,11]
        elif self.data['years'] in range(14,17):
            correct_hours = [8,9,10]
        elif self.data['years'] in range(18,64):
            correct_hours = [7,8,9]
        else: import json
import matplotlib.pyplot as plt
import datetime

class tools():
    def __init__(self):
        self.path = 'data.json'
        with open(self.path) as json_file:
            self.data = dict(json.load(json_file))
            
    def update(self, dat):
        self.data = dat
        with open(self.path, "w") as json_file:
            json.dump(self.data, json_file)
            
            
    def calculate_correctess_of_sleep_time(self, sleep_time):
        if self.data['years'] in range(13):
            correct_hours = [9,10,11]
        elif self.data['years'] in range(14,17):
            correct_hours = [8,9,10]
        elif self.data['years'] in range(18,64):
            correct_hours = [7,8,9]
        else: 
            correct_hours = [7,8]
            
        if sleep_time in correct_hours:
            return ["Twoja długosć snu jest dobra dla twojego wieku.", 0]
        else:
            if min(correct_hours) > sleep_time:
                t = min(correct_hours) - sleep_time
            else:
                t = sleep_time - max(correct_hours)
            return ["Masz nieprawidłową długosć snu o {}h!".format(t), 1]

    def generate_mean_sleep_time_plot(self):
        sleep_time_data = [] 
        beg_time_data = []
        end_time_data = []  
        for n in self.data['sleep_time']:
             sleep_time_data.append(24-n[0] + n[1])
             beg_time_data.append(n[0])
             end_time_data.append(n[1])



        plt.plot(self.data['date_time'], sleep_time_data)
        plt.title('Czas snu poprzez czas')
        plt.ylabel('Czas snu')
        plt.xlabel('Czas')
        plt.gcf().autofmt_xdate()
        plt.savefig('plots/time_plot.jpg')
        plt.gcf().clear()

        plt.plot(self.data['date_time'], beg_time_data)
        plt.title('Początek snu poprzez czas')
        plt.ylabel('Godzina początku snu')
        plt.xlabel('Czas')
        plt.gcf().autofmt_xdate()
        plt.savefig('plots/beg_plot.jpg')
        plt.gcf().clear()

        plt.plot(self.data['date_time'], end_time_data)
        plt.gcf().autofmt_xdate()
        plt.savefig('plots/end_plot.jpg')

        plt.show()

    
if __name__ == '__main__':
    tool = tools()
    tool.generate_mean_sleep_time_plot()
    #print(datetime.datetime.now('%D%M%Y'))
            correct_hours = [7,8]
            
        if sleep_time in correct_hours:
            return ["Twoja długosć snu jest dobra dla twojego wieku.", 0]
        else:
            if min(correct_hours) > sleep_time:
                t = min(correct_hours) - sleep_time
            else:
                t = sleep_time - max(correct_hours)
            return ["Masz nieprawidłową długosć snu o {}h!".format(t), 1]

    def generate_mean_sleep_time_plot(self):
        sleep_time_data = [] 
        beg_time_data = []
        end_time_data = []  
        for n in self.data['sleep_time']:
             sleep_time_data.append(24-n[0] + n[1])
             beg_time_data.append(n[0])
             end_time_data.append(n[1])

        fig, (sleep_time, beg_time, end_time) = plt.subplots(3)

        fig.tight_layout(pad=3.0)

        sleep_time.plot(self.data['date_time'], sleep_time_data)
        sleep_time.title.set_text('Czas snu poprzez czas')
        sleep_time.set_ylabel('Czas snu')
        sleep_time.set_xlabel('Czas')
        #sleep_time.gcf().autofmt_xdate()

        beg_time.plot(self.data['date_time'], beg_time_data)
        beg_time.title.set_text('Początek snu poprzez czas')
        beg_time.set_ylabel('Godzina początku snu')
        beg_time.set_xlabel('Czas')
        #beg_time.gcf().autofmt_xdate()

        end_time.plot(self.data['date_time'], end_time_data)
        fig.autofmt_xdate()
        #fig.savefig('plots/time_plot.jpg')

        plt.show()

    
if __name__ == '__main__':
    tool = tools()
    tool.generate_mean_sleep_time_plot()
    #print(datetime.datetime.now('%D%M%Y'))
