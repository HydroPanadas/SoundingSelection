Read Me file for sor_id_Mapping.py, sor_id_Mapping.exe

The executable python file .py can be opened in IDLE 2.7 (.15) or double click to be ran using the python command line.

There is also an .exe file in the dist folder that can be run from any windows system without the need to have python installed just double click the icon. 

This script initializes a Graphical User Interface (GUI) where users can create XML Mapping files to map Source Document ID Numbers. 

Functions In File Menu:
	Create Translation File:
		The translation file that maps the contributor layer to the sor_id field in the a Hob sounding file, can be created by a one click here.
		The user is asked for the save location and the translation file is made.
		
		The format of the Translation file that auto-populates the sor_id attribute field with the source document number from the contributor layer is: 

			<?xml version="1.0" encoding="UTF-8"?>
			<Selected_Sounding_Conversion>
				<Contributor New_Acronym="sor_id"/>
			</Selected_Sounding_Conversion>
			
			Using the Translation file:
				Ensure Sounding Selection is done in the Parent of the Depth and Contributor band,
				Select Quick Creator, Create Features From Selected/Superselected, or Sounding Selection
				Upload the Translation file in the Dialog box
	
	To exit the GUI:
				In the File Menu a Close Application function exist that when clicked exits the GUI.
				The close icon [x] at top right of the GUI can also exit the GUI.

GUI Functions:
	Create Mapping XML from user manual input or from a CSV file.
		Create XML:
			The user specifies Source Document Numbers they want to be mapped from 1234|5|6789... format to 1234.... format. This can be done for up to 15 Source Document Numbers.
			When Create XML is pressed an XML file is made and the user specifies the save location. 
			This will be used to map the sor_id attributes field in the HOB file to only contain the Source Document Number. 
		
		Create XML from CSV:
			Similar to Create XML however user is asked to import a CSV file with the following header "Fileno" and rows under this column header 
			containing the Source Document Numbers. (It is not a big deal if there is other information in this column (i.e. Descriptions, Null Values....) 
			the program will only extract and use the Source Document Numbers for this column data)
			The program will create the Mapping XML file and ask the user for a save location. 
			This will be used to map the sor_id attributes field of the sounding feature to only have the Source Document Number.
			
			*To Create the CSV save a spreadsheet containing all the Fileno as the CSV format from Excel's "save as" option in the file menu.*   
			
	The format for the Mapping File is:

		<?xml version="1.0" encoding="UTF-8"?>
		<ObjectToObjectConversionTable Version="1.0" FromType="GO" ToType="GO">
		   <ConversionTableInfo Version="1.1" FromProduct="HOB" ToProduct="HOB" Name="sor_id Mapping" CreationDate="2018-07-24"
			   CreatedBy="CHS Atlantic" Comment="Mapping the sor_id from 1234.... |2|4567..... to 1234.....">
		   </ConversionTableInfo>
		   <AttributeMappings>
			   <MapAttribute Name="sor_idtosor_id">
				   <Entry>
					   <Filter>
						   <AttributeValueIsLike Acronym="sor_id" Value="1\b.*"/>
					   </Filter>
					   <SetAttributeValue Acronym="sor_id" Value="1"/>
				   </Entry>
				   <Entry>
					   <Filter>
						   <AttributeValueIsLike Acronym="sor_id" Value="2\b.*"/>
					   </Filter>
					   <SetAttributeValue Acronym="sor_id" Value="2"/>
				   </Entry>
				   .
				   .
				   .
				   .
				   .
			   </MapAttribute>
		   </AttributeMappings>
		   <ObjectMappings>
			   <Object Acronym= "SOUNDG">
				   <MapObject>
					   <ApplyAttributeMapping Name="sor_idtosor_id"/>
				   </MapObject>
			   </Object>
		   </ObjectMappings>
		</ObjectToObjectConversionTable>
		
	Using the Mapping file:
				To use the Mapping File:
				Ensure ALL the soundings in the sounding layer that need to be mapped are selected. 
				Go to EDIT Menu-ChangeSelection (ChanageALL).
				Go to the Advanced Options, and select Feature Mapping and choose the Rule File (sor_id_mapping)
					Important To have the ability to select this as a rule file the mapping file must be saved in a mapped folder that your BASE Editor is searching for Rule files in. 
					To change this folder or view what the correct folder is head to:
					The Tools Menu- Option - Files and Folders, Search for Rules option located on the left side menu. To the right side window will show the folder that Base Editor is using to search for Rule file. 
					This folder should be changed a new location where the user saves the created mapping file to. 
					
					*Since the default location is on the C drive in the Caris program files, it may be easier to change the folder location over adding the file to this default location since IT Admin Permission may be required. 
					To change the folder location in Caris you do not need such IT Admin Permissions.*

Created July 24, 2018 11:26 AST.