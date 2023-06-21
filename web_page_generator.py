import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # creating a label for
        # name using widget Label
        self.custom_label = tk.Label(self.master, text = "Enter custom text or click the Default HTML page button")
        self.custom_label.grid(row = 0, column = 0, padx = 20, pady = (20,0), sticky = W)

        # Input text for user
        self.inputText = tk.Entry(self.master, width = 150)
        self.inputText.grid (row = 1, column = 0, columnspan = 3, padx = (10, 10), pady = (10, 10), sticky = W+E)

        # Default button
        self.default_btn = Button (self.master, text = "Default HTML Page", width = 30, height = 2, command = self.defaultHTML)
        self.default_btn.grid (row = 2, column = 1, padx = (0,10), pady = (0, 10))

        # Submit custom text button
        self.submit_btn = Button (self.master, text = "Subtmit Custom Text", width = 30, height = 2, command = self.submitHTML)
        self.submit_btn.grid (row = 2, column = 2, padx = (0, 10), pady = (0, 10))


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    # Function to return the Input data   
    def submitHTML(self):
        # Made variable get input data from self.inputText
        htmlText = self.inputText.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
