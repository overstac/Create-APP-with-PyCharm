from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout    #QV- V=vertical/ H=horizontal
from PyQt6.QtWidgets import  QLabel, QPushButton, QLineEdit

def make_sentence():                        # == SLOTH== the function triggered by clicked slignal
    input_text= text.text()
    output_label.setText(input_text.capitalize() + ".")

app= QApplication([])               # the entire app , the application
window= QWidget()                   # the window
window.setWindowTitle("Sentence Maker")             # the title

layout= QVBoxLayout()       # layout set, on Vertical

text= QLineEdit()           # ADD the first widget= text box
layout.addWidget(text)      # add to layout

btn= QPushButton("Make")        # ADD the button
layout.addWidget(btn)           # add to layout
btn.clicked.connect(make_sentence) # button= widget// clicked(checked etc.)= signal// make_sentence= sloth (what is triggered)
                                                #THE TRIGGER
output_label= QLabel("")                        # result down below before the typing result
layout.addWidget(output_label)

window.setLayout(layout)                
window.show()
app.exec()