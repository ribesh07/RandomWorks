import tkinter as tk
from tkinter import ttk
from datetime import datetime
import nepali_datetime
import speedtest
# import socket


class DateWidget(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Date Widget")
        self.geometry("400x250")

        self.label = ttk.Label(self, text="", font=("Helvetica", 16))
        self.label.pack(pady=20)
        self.label1 = ttk.Label(self, text="", font=("Helvetica", 16))
        self.label1.pack(pady=30)
        self.speed_button = ttk.Button(self,text='SpeedTest',command = lambda:self.perform_speed_test())
        self.speed_button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        self.speedfast_button = ttk.Button(self,text='SpeedTest_fast',command = lambda:self.speedtest_fast())
        self.speedfast_button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
        self.label1.configure(text="No Data !")
        # self.perform_speed_test()
        self.update_date()
        self.after(1000, self.update_date)  # Update every second

    # def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    #     try:
    #         # Create a socket object
    #         socket.create_connection((host, port), timeout=timeout)
    #         print("Internet connection is available.")
    #         return True
    #     except OSError:
    #         print("No internet connection.")
    #         return False

    def perform_speed_test(self):
        # if self.check_internet_connection() :
            st = speedtest.Speedtest()
            st.get_best_server() 
            # Download speed
            download_speed ="{:.2f}".format(st.download()/1048576) # Convert to Mbps
            print(f"Download Speed: {download_speed} Mbps")
            # Upload speed
            upload_speed ="{:.2f}".format(st.upload()/1048576)  # Convert to Mbps
            print(f"Upload Speed: {upload_speed} Mbps")
            # return f"Download :{download_speed} Mbps Upload :{upload_speed} Mbps"
            testresult = f"Down:{download_speed} Mbps Up:{upload_speed} Mbps"
            
            self.label1.configure(text=testresult)
        # else:
        #     self.label1.configure(text="No Internet!") 
        
    def speedtest_fast(self):
        from selenium import webdriver
        from bs4 import BeautifulSoup
        import time
        from selenium.webdriver.chrome.options import Options
        import warnings
        warnings.simplefilter("ignore")
        print('checking...\n')
        chrome_options = Options()
        # chrome_options.headless = True
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('window-size=0x0')
        driver = webdriver.Chrome(options=chrome_options)  # or webdriver.Chrome()
        driver.get('https://fast.com')
        time.sleep(11)  # Wait for test to complete
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        speed = soup.find('div', {'class': 'speed-results-container'}).text
        driver.quit()
        testresult = f"Download Speed:{speed} Mbps"
        print(testresult)
        self.label1.configure(text=testresult)
        
    def update_date(self):
        # NepaliDateTime
        current_date = nepali_datetime.date.today().strftime("%Y %B %d , %A")
        # current_time = datetime.now().strftime(" %H:%M:%S")
        self.label.configure(text=current_date)   
        self.after(1000, self.update_date)
        
if __name__ == "__main__":
    app = DateWidget()
    app.mainloop()
    
