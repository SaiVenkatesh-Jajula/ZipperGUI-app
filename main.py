import PySimpleGUI as sg
from zipper import zipper

label1=sg.Text("Select Files to Compress : ")
input1=sg.InputText(key='filepaths')
choose1=sg.FilesBrowse("choose")

label2=sg.Text("Select Destination Folder : ")
input2=sg.InputText(key='folderpath')
choose2=sg.FolderBrowse("choose")

compress=sg.Button("compress")
outputlabel=sg.Text(text_color='green', key='output')
window=sg.Window(title="Compressing Files App",
                 layout=[[label1,input1,choose1],
                        [label2,input2,choose2],
                         [compress, outputlabel]
                 ])
while True:
    event,item=window.read()
    filepaths=item['filepaths'].split(';')
    folderpath=item['folderpath']
    zipper(filepaths, folderpath)
    window["output"].update(value="Compressing completed!...")
    exit()
window.close()