'''
Created on Apr 6, 2020

@author: anand
'''

from burp import IBurpExtender
from burp import IBurpExtenderCallbacks
from burp import ITab
from burp import IContextMenuFactory
from burp import IMenuItemHandler
from burp import IContextMenuInvocation
from burp import IExtensionHelpers
from burp import IHttpListener
from burp import IHttpRequestResponse
from javax.swing import JPanel, JFrame, JMenuItem, JMenu, JLabel, JComboBox, JTable, JScrollPane
from javax.swing import JSplitPane, JEditorPane, GroupLayout
from javax.swing import JButton
from javax.swing import JTextField
from javax.swing import SwingConstants
from java.awt import FlowLayout, GridBagConstraints, BorderLayout
from javax.swing import JTextArea
from javax.swing import JTabbedPane
from java.awt import Font
import sys
from java.awt.event import ActionListener, KeyAdapter
from javax.swing.table import DefaultTableModel, TableColumn



class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("BurpExtension")
        g = GUI()
        callbacks.addSuiteTab(g)
        callbacks.registerContextMenuFactory(rightClickMenu(g))
        sys.stdout = callbacks.getStdout()
        callbacks.registerHttpListener(CustomServer(sys.stdout))
        
        
    
class rightClickMenu(IContextMenuFactory, ActionListener): #implementation of options 
    def __init__(self, itabobject):
        self._itabobject = itabobject
        return
    def createMenuItems(self, invocation):
        menu = []
        jmi1 = JMenuItem()
        jmi1.setText("Send to Results")
        jm1 = JMenu("Send to Failed Cases")
        jmi_obj1 = JMenuItem()
        jmi_obj2 = JMenuItem()
        jmi_obj3 = JMenuItem()
        jmi_obj4 = JMenuItem()
        jmi_obj5 = JMenuItem()
        jmi_obj6 = JMenuItem()
        jmi_obj7 = JMenuItem()
        jmi_obj8 = JMenuItem()
        jmi_obj9 = JMenuItem()
        jmi_obj10 = JMenuItem()
        jmi_obj11 = JMenuItem()
        jmi_obj12 = JMenuItem()
        jmi_obj13 = JMenuItem()
        jmi_obj14 = JMenuItem()
        jmi_obj15 = JMenuItem()
        jmi_obj16 = JMenuItem()  
        jmi_obj1.setText("Objective-1")
        jmi_obj2.setText("Objective-2")
        jmi_obj3.setText("Objective-3")
        jmi_obj4.setText("Objective-4")
        jmi_obj5.setText("Objective-5")
        jmi_obj6.setText("Objective-6")
        jmi_obj7.setText("Objective-7")
        jmi_obj8.setText("Objective-8")
        jmi_obj9.setText("Objective-9")
        jmi_obj10.setText("Objective-10")
        jmi_obj11.setText("Objective-11")
        jmi_obj12.setText("Objective-12")
        jmi_obj13.setText("Objective-13")
        jmi_obj14.setText("Objective-14")
        jmi_obj15.setText("Objective-15")
        jmi_obj16.setText("Objective-16")
        jmi1.setVisible(True)
        jmi1.addActionListener(self)
        menu.append(jmi1)
        if(self._itabobject.getAppRating()=="Low"):
            jm1.add(jmi_obj1)
            jm1.add(jmi_obj2)
            jm1.add(jmi_obj3)
            jm1.add(jmi_obj4)
            jm1.add(jmi_obj5)
            menu.append(jm1)
        elif(self._itabobject.getAppRating()=="High"):
            jm1.add(jmi_obj1)
            jm1.add(jmi_obj2)
            jm1.add(jmi_obj3)
            jm1.add(jmi_obj4)
            jm1.add(jmi_obj5)
            jm1.add(jmi_obj6)
            jm1.add(jmi_obj7)
            jm1.add(jmi_obj8)
            jm1.add(jmi_obj9)
            jm1.add(jmi_obj10)
            jm1.add(jmi_obj11)
            jm1.add(jmi_obj12)
            jm1.add(jmi_obj13)
            jm1.add(jmi_obj14)
            jm1.add(jmi_obj15)
            jm1.add(jmi_obj16)
            menu.append(jm1)
        else:
            menu = []
        
        return menu
        
    
    def actionPerformed(self, e):
        
        self._itabobject.addDetails()
    
    
class GUI(ITab, ActionListener, KeyAdapter):
    def __init__(self):
       return
        
    def getTabCaption(self):
        return "BurpExtension"
    
    def getUiComponent(self):
        return self.UI()
        
    def UI(self):
        self.val=""
        self.tabbedPane = JTabbedPane(JTabbedPane.TOP)
        self.panel = JPanel()
        self.tabbedPane.addTab("App Details", None, self.panel, None) # Details of app currently under pentest would be pulled into here through API
        self.panel_1 =  JPanel()
        self.tabbedPane.addTab("Results", None, self.panel_1, None) # passed results would go inside this and connected to reporting system via API
        self.panel_2 =  JPanel()
        self.tabbedPane.addTab("Failed Cases", None, self.panel_2, None) #list of failed tests would go inside this
        self.textField = JTextField()
        self.textField.setBounds(12, 13, 207, 39)
        self.panel.add(self.textField)
        self.textField.setColumns(10)
        self.comboBox = JComboBox()
        self.comboBox.setEditable(True)
        self.comboBox.addItem("Default")
        self.comboBox.addItem("High")
        self.comboBox.addItem("Low")
        self.comboBox.setBounds(46, 65, 130, 28)
        self.comboBox.addActionListener(self)
        self.panel.add(self.comboBox) 
        self.btnNewButton = JButton("Submit")
        self.btnNewButton.setBounds(60, 125, 97, 25)
        self.panel.add(self.btnNewButton)
        editorPane = JEditorPane();
        editorPane.setBounds(12, 35, 1000, 800);
        self.panel_2.add(editorPane);
        self.panel_2.setLayout(BorderLayout())
        return self.tabbedPane
    
    def getAppRating(self):
        sys.stdout.write(str(self.val))      
        return str(self.val)
        
    def actionPerformed(self, e):
        if(e.getSource()==self.comboBox):
            self.val = self.comboBox.getSelectedItem()
        else:
            self.addDetails()
        
    def addDetails(self):
        jf0 = JFrame()
        jf0.setTitle("Add Issue");
        jf0.setLayout(None);
        
        txtEnterIssue = JTextField();
        txtEnterIssue.setName("Enter Issue Name");
        txtEnterIssue.setToolTipText("Enter Issue Name Here");
        txtEnterIssue.setBounds(182, 58, 473, 40);
        jf0.add(txtEnterIssue);
        txtEnterIssue.setColumns(10);
        
        btnNewButton = JButton("Add");
        btnNewButton.setBounds(322, 178, 139, 41);
        jf0.add(btnNewButton);
        
        comboBox = JComboBox();
        comboBox.setMaximumRowCount(20);
        comboBox.setEditable(True);
        comboBox.setToolTipText("Objective Name");
        comboBox.setBounds(182, 125, 473, 40);
        jf0.add(comboBox);
        
        lblNewLabel = JLabel("Issue Name Here");
        lblNewLabel.setFont(Font("Tahoma", Font.PLAIN, 16));
        lblNewLabel.setBounds(25, 58, 130, 40);
        jf0.add(lblNewLabel);
        
        lblNewLabel_1 = JLabel("Objective Name");
        lblNewLabel_1.setFont(Font("Tahoma", Font.PLAIN, 16));
        lblNewLabel_1.setBounds(25, 125, 130, 40);
        jf0.add(lblNewLabel_1);
        jf0.setVisible(True)
        jf0.setBounds(400, 300, 700, 300)
        jf0.EXIT_ON_CLOSE
        
        txtEnterIssue.addKeyListener(self)
    
    def keyPressed(self, e):
               
        self.search_string.__add__(self.search_string)
        self.jtf1.setText(self.search_string)
        sys.stdout.write(self.search_string)
    

class CustomServer(IHttpListener):
    def __init__(self,std):
        self._std = std
        return
    
    
    def processHttpMessage(self, toolFlag, messageisRequest, messsageInfo):
        self._req = messsageInfo.getRequest()
        self._host = messsageInfo.getHttpService()
        self._host = self._host.getHost()
        self._std.write(self._host)
