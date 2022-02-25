#Import Library Tools
from Tkinter import *
import tkFileDialog
import os
from distutils.file_util import move_file
import datetime
import csv
from os import startfile

    
class Application(Frame):
    "This Application creates the translation file to map the contributor to the sor_id attribute field in a HOB file"
    "This Application also creates the mapping file to remove the values trailing the Source Document number when the contributor layer is mapped"
    "There is two options for the user to create the xml mapping file:"
    "The first option is to manually input values (up to 15 total values) into the GUI and press the Create XML button"
    "The Second option is to import a CSV file created from the Source Data Search spreadhseet, and press Create XML from CSV"
    
    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ Create Widgets for Script """

        #Create the Main Menu Bar
        menu.add_cascade(label="File",menu=submenu)

        #Translation File Submenu
        submenu.add_command(label="Create Translation File",command=self.Create_Translationfile)
        
        #Help Submenu
        submenu.add_command(label="Help",command=self.Help)
        
        #Close Submenu
        submenu.add_command(label="Close Application",command=self.close)

        Label(self, text= "Enter Document Numbers (sor_id) or Upload a CSV:").grid(row =0, column =0,columnspan=3, sticky= W)

        #Create the user input option for manual source ID input
        #sor_id 1
        self.instruction = Label (self, text="sor_id 1")
        self.instruction.grid(row=1,column=0, columnspan=2, sticky=W)
        self.d1=Entry(self)
        self.d1.grid(row=1,column=2, sticky=W)
        self.d1.insert(END, '0')
        
        #sor_id 2
        self.instruction = Label (self, text="sor_id 2")
        self.instruction.grid(row=2,column=0, columnspan=2, sticky=W)
        self.d2=Entry(self)
        self.d2.grid(row=2,column=2, sticky=W)
        self.d2.insert(END, '0')

        #sor_id 3
        self.instruction = Label (self, text="sor_id 3")
        self.instruction.grid(row=3,column=0, columnspan=2, sticky=W)
        self.d3=Entry(self)
        self.d3.grid(row=3,column=2, sticky=W)
        self.d3.insert(END, '0')
            
        #sor_id 4
        self.instruction = Label (self, text="sor_id 4")
        self.instruction.grid(row=4,column=0, columnspan=2, sticky=W)
        self.d4=Entry(self)
        self.d4.grid(row=4,column=2, sticky=W)
        self.d4.insert(END, '0')
            
        #sor_id 5
        self.instruction = Label (self, text="sor_id 5")
        self.instruction.grid(row=5,column=0, columnspan=2, sticky=W)
        self.d5=Entry(self)
        self.d5.grid(row=5,column=2, sticky=W)
        self.d5.insert(END, '0')

        #sor_id 6
        self.instruction = Label (self, text="sor_id 6")
        self.instruction.grid(row=6,column=0, columnspan=2, sticky=W)
        self.d6=Entry(self)
        self.d6.grid(row=6,column=2, sticky=W)
        self.d6.insert(END, '0')

        #sor_id 7
        self.instruction = Label (self, text="sor_id 7")
        self.instruction.grid(row=7,column=0, columnspan=2, sticky=W)
        self.d7=Entry(self)
        self.d7.grid(row=7,column=2, sticky=W)
        self.d7.insert(END, '0')

        #sor_id 8
        self.instruction = Label (self, text="sor_id 8")
        self.instruction.grid(row=8,column=0, columnspan=2, sticky=W)
        self.d8=Entry(self)
        self.d8.grid(row=8,column=2, sticky=W)
        self.d8.insert(END, '0')

        #sor_id 9
        self.instruction = Label (self, text="sor_id 9")
        self.instruction.grid(row=9,column=0, columnspan=2, sticky=W)
        self.d9=Entry(self)
        self.d9.grid(row=9,column=2, sticky=W)
        self.d9.insert(END, '0')
                                                                   
        #sor_id 10
        self.instruction = Label (self, text="sor_id 10")
        self.instruction.grid(row=10,column=0, columnspan=2, sticky=W)
        self.d10=Entry(self)
        self.d10.grid(row=10,column=2, sticky=W)
        self.d10.insert(END, '0')

        #sor_id 11
        self.instruction = Label (self, text="sor_id 11")
        self.instruction.grid(row=11,column=0, columnspan=2, sticky=W)
        self.d11=Entry(self)
        self.d11.grid(row=11,column=2, sticky=W)
        self.d11.insert(END, '0')
        
        #sor_id 12
        self.instruction = Label (self, text="sor_id 12")
        self.instruction.grid(row=12,column=0, columnspan=2, sticky=W)
        self.d12=Entry(self)
        self.d12.grid(row=12,column=2, sticky=W)
        self.d12.insert(END, '0')

        #sor_id 13
        self.instruction = Label (self, text="sor_id 13")
        self.instruction.grid(row=13,column=0, columnspan=2, sticky=W)
        self.d13=Entry(self)
        self.d13.grid(row=13,column=2, sticky=W)
        self.d13.insert(END, '0')
        
        #sor_id 14
        self.instruction = Label (self, text="sor_id 14")
        self.instruction.grid(row=14,column=0, columnspan=2, sticky=W)
        self.d14=Entry(self)
        self.d14.grid(row=14,column=2, sticky=W)
        self.d14.insert(END, '0')
        
        #sor_id 15
        self.instruction = Label (self, text="sor_id 15")
        self.instruction.grid(row=15,column=0, columnspan=2, sticky=W)
        self.d15=Entry(self)
        self.d15.grid(row=15,column=2, sticky=W)
        self.d15.insert(END, '0')

        #Create the XML Mapping file using the user input
        self.submit_button=Button(self, text="Create XML", command=self.Create_xml).grid(row=17, column=0, columnspan=3)

        #Create the XML Mapping file using the user imported CSV
        self.submit_button=Button(self, text="Create XML from CSV", command=self.XML_From_CSV).grid(row=18, column=0, columnspan=3)
        

    def XML_From_CSV (self):
        "This function creates the mapping file according to a user imported CSV file with the header for the Source IDs called Fileno"

        #Open and read the CSV file headers and row information
        CSV_File=tkFileDialog.askopenfilename()
        Opened=open(CSV_File)
        csvreader=csv.reader(Opened)
        header=csvreader.next()
        Fileno=header.index("Fileno")
        filenolist=[]

        #Create a list containing all the Source IDs from the CSV
        for row in csvreader:
            fileno=row[Fileno]
            filenolist.append(fileno)

        #Create list only containing Intergers (Remove the test, and null values)
        filenolist_NoNull=[x for x in filenolist if x !='']
        filenolist_NoZeros=[x for x in filenolist_NoNull if x !='0']
        filenolist_Int=[x for x in filenolist_NoZeros if x.isdigit()]

        #Writing the XML Mapping file in correct format and with correct information more information in CARIS HELP
        date=str(datetime.date.today())
        with open("sor_id_mapping.xml", "w") as text_file:
            text_file.write('<?xml version="1.0" encoding="UTF-8"?>'+'\n')
            text_file.write('<ObjectToObjectConversionTable Version="1.0" FromType="GO" ToType="GO">'+'\n')
            text_file.write('   <ConversionTableInfo Version="1.1" FromProduct="HOB" ToProduct="HOB" Name="sor_id Mapping" CreationDate="' + date + '"'+ '\n')
            text_file.write('       CreatedBy="CHS Atlantic" Comment="Mapping the sor_id from 1234.... |2|4567..... to 1234.....">'+'\n')
            text_file.write('   </ConversionTableInfo>'+'\n')
            text_file.write('   <AttributeMappings>'+'\n')
            text_file.write('       <MapAttribute Name="sor_idtosor_id">'+'\n')

            #Create the entry section of the XML for each Source ID number
            for Documentno in filenolist_Int:
                text_file.write('           <Entry>' +'\n')
                text_file.write('               <Filter>'+'\n')
                text_file.write('                   <AttributeValueIsLike Acronym="sor_id" Value="'+ Documentno + '\\b.*"/>' +'\n')
                text_file.write('               </Filter>'+'\n')
                text_file.write('               <SetAttributeValue Acronym="sor_id" Value="'+ Documentno + '"/>'+'\n')
                text_file.write('           </Entry>'+'\n')
                
            text_file.write('       </MapAttribute>'+'\n')
            text_file.write('   </AttributeMappings>'+'\n')
            text_file.write('   <ObjectMappings>'+'\n')
            text_file.write('       <Object Acronym= "SOUNDG">'+'\n')
            text_file.write('           <MapObject>'+'\n')
            text_file.write('               <ApplyAttributeMapping Name="sor_idtosor_id"/>'+'\n')
            text_file.write('           </MapObject>'+'\n')
            text_file.write('       </Object>'+'\n')
            text_file.write('   </ObjectMappings>'+'\n')
            text_file.write('</ObjectToObjectConversionTable>'+'\n')

        #Saving the Mapping file as:
        dest_path=tkFileDialog.askdirectory()
        xml=('sor_id_mapping.xml')
        dst_file = os.path.join(dest_path, xml)
        if os.path.exists(dst_file):
            os.remove(dst_file)
            move_file("sor_id_mapping.xml",dest_path)
        else:
            move_file("sor_id_mapping.xml",dest_path)
        startfile(dest_path)
            
    def Create_xml(self):
        "This function Creates the mapping file according user input boxes in the GUI"

        #Get the user input Source ID numbers
        d1=str(self.d1.get())
        d2=str(self.d2.get())
        d3=str(self.d3.get())
        d4=str(self.d4.get())
        d5=str(self.d5.get())
        d6=str(self.d6.get())
        d7=str(self.d7.get())
        d8=str(self.d8.get())
        d9=str(self.d9.get())
        d10=str(self.d10.get())
        d11=str(self.d11.get())
        d12=str(self.d12.get())
        d13=str(self.d13.get())
        d14=str(self.d14.get())
        d15=str(self.d15.get())

        #Create a list of the user input Source ID numbers and remove all the Zero values
        sorlist=[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15]
        sorlist_NoNull=[x for x in sorlist if x !='']
        sorlist_NoZeros=[x for x in sorlist_NoNull if x !='0']

        #Writing the XML Mapping file in correct format and with correct more information in CARIS HELP
        date=str(datetime.date.today())
        with open("sor_id_mapping.xml", "w") as text_file:
            text_file.write('<?xml version="1.0" encoding="UTF-8"?>'+'\n')
            text_file.write('<ObjectToObjectConversionTable Version="1.0" FromType="GO" ToType="GO">'+'\n')
            text_file.write('   <ConversionTableInfo Version="1.1" FromProduct="HOB" ToProduct="HOB" Name="sor_id Mapping" CreationDate="' + date + '"'+ '\n')
            text_file.write('       CreatedBy="CHS Atlantic" Comment="Mapping the sor_id from 1234.... |2|4567..... to 1234.....">'+'\n')
            text_file.write('   </ConversionTableInfo>'+'\n')
            text_file.write('   <AttributeMappings>'+'\n')
            text_file.write('       <MapAttribute Name="sor_idtosor_id">'+'\n')

            #Create the entry section of the XML for each Source ID number
            for Documentno in sorlist_NoZeros:
                text_file.write('           <Entry>' +'\n')
                text_file.write('               <Filter>'+'\n')
                text_file.write('                   <AttributeValueIsLike Acronym="sor_id" Value="'+ Documentno + '\\b.*"/>' +'\n')
                text_file.write('               </Filter>'+'\n')
                text_file.write('               <SetAttributeValue Acronym="sor_id" Value="'+ Documentno + '"/>'+'\n')
                text_file.write('           </Entry>'+'\n')   
                
            text_file.write('       </MapAttribute>'+'\n')
            text_file.write('   </AttributeMappings>'+'\n')
            text_file.write('   <ObjectMappings>'+'\n')
            text_file.write('       <Object Acronym= "SOUNDG">'+'\n')
            text_file.write('           <MapObject>'+'\n')
            text_file.write('               <ApplyAttributeMapping Name="sor_idtosor_id"/>'+'\n')
            text_file.write('           </MapObject>'+'\n')
            text_file.write('       </Object>'+'\n')
            text_file.write('   </ObjectMappings>'+'\n')
            text_file.write('</ObjectToObjectConversionTable>'+'\n')

        #Saving the Mapping file as:
        dest_path=tkFileDialog.askdirectory()
        xml=('sor_id_mapping.xml')
        dst_file = os.path.join(dest_path, xml)
        if os.path.exists(dst_file):
            os.remove(dst_file)
            move_file("sor_id_mapping.xml",dest_path)
        else:
            move_file("sor_id_mapping.xml",dest_path)
        startfile(dest_path)

    def Create_Translationfile(self):
        "This function Creates the Translation file that is used to map the Contributor Layer to the sor_id field"

        #Writing the Translation file in correct format and with correct information        
        with open("Contributer_sor_id_Translationfile.bsst", "w") as text_file:
            text_file.write('<?xml version="1.0" encoding="UTF-8"?>'+'\n')
            text_file.write('<Selected_Sounding_Conversion>'+'\n')
            text_file.write(' <Contributor New_Acronym="sor_id"/>'+'\n')
            text_file.write('</Selected_Sounding_Conversion>'+'\n')

        #Saving the Translation file as:
        dest_path=tkFileDialog.askdirectory()
        translationfile=('Contributer_sor_id_Translationfile.bsst')
        dst_file = os.path.join(dest_path, translationfile)
        if os.path.exists(dst_file):
            os.remove(dst_file)
            move_file("Contributer_sor_id_Translationfile.bsst",dest_path)
        else:
            move_file("Contributer_sor_id_Translationfile.bsst",dest_path)
        startfile(dest_path)
        
    def Help(self):
        "This function opens the README file"
        startfile('README_sor_id.txt')#Open Help file for application
                 
    def close(self):
        "This function Closes the Application"
        root.destroy() #Option to close Application GUI

root=Tk()
root.title("Create sor_id Mapping File")
root.geometry("350x450")
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
app=Application(root)
root.mainloop()
