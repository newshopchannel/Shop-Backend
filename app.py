#app.py
# Copyright (C) The New Shop Channel Team. 2024

from flask import Flask, send_file, render_template, request, Response
from urllib.request


import requests
import xml.etree.ElementTree as ET
import ssl
import logging
import os


# Setup our app
app = Flask(__name__)
application = app


#@app.route('/')
#def index():
    #return render_template ('index.jsp')

@app.route('/',methods=['POST', 'GET'])
def W_01():
    return render_template ('W_01.jsp')

@app.route('/W_03.jsp',methods=['POST', 'GET'])
def W_03():
    return render_template ('W_03.jsp')

@app.route('/B_04.jsp')
def B_04():
    return render_template ('B_04.jsp')
    
@app.route('/CheckRegistered.jsp', methods=['POST', 'GET'])
def checkRegistered():
    return render_template ('CheckRegistered.jsp')

@app.route('/CheckBalance.jsp', methods=['POST', 'GET'])
def checkBalance():
    return render_template ('CheckBalance.jsp')

@app.route("/ecs/services/ECommerceSOAP", methods=['POST', 'GET'])
def ecs():
    # Get the XML content from the request
    xml_content = request.data
    
    # Print or log the XML content for tracing purposes
    print("Received XML request:")
    print(xml_content.decode("utf-8"))
    
    # Parse the XML content to extract xsi:type attribute value
    try:
        root = ET.fromstring(xml_content)
        # Search for the 'xsi:type' attribute within the XML tree
        xsi_type = None
        for elem in root.iter():
            xsi_type = elem.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if xsi_type:
                break
    except ET.ParseError as e:
        return Response("Error parsing XML: " + str(e), status=400)

    # Define the path to the XML files directory
    xml_files_dir = 'xml/'

    # Map xsi:type attribute values to corresponding XML file names
    file_mappings = {
        'ecs:CheckDeviceStatusRequestType': 'checkDeviceStatus.xml',
        'ecs:GiftTitleRequestType': 'checkregistration.xml',
        'ecs:ListETicketsRequestType': 'listetickets.xml',
        'ecs:GetETicketsRequestType': 'GetETickets.xml'

        # Add more mappings as needed
    }

    # Print or log the value of xsi_type
    print("xsi_type:", xsi_type)

    # Check if the xsi:type attribute value is not None and has a corresponding XML file
    if xsi_type is not None and xsi_type in file_mappings:
        # Construct the file path
        file_path = os.path.join(xml_files_dir, file_mappings[xsi_type])
        print("File path:", file_path)  # Debug statement
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the contents of the corresponding XML file
            with open(file_path, 'r', encoding='utf-8') as file:
                xml_content = file.read()

            # Print or log the XML content
            print("XML response:")
            print(xml_content)

            # Return the XML content as the response with UTF-8 charset
            return Response(xml_content, mimetype='text/xml; charset=utf-8')
        else:
            print("File not found")  # Debug statement
            return Response("XML file not found", status=404)
    else:
        print("Mapping not found")  # Debug statement
        # Return a 404 Not Found response if xsi:type attribute value is None or doesn't match any mapping
        return Response("XML file not found", status=404)


@app.route('/S_01.jsp', methods=['POST', 'GET'])
def S_01():
    return render_template ('S_01.jsp')


@app.route('/S_02.jsp', methods=['POST', 'GET'])
def S_02():
    return render_template ('S_02.jsp')


@app.route('/S_04.jsp', methods=['POST', 'GET'])
def S_04():
    return render_template ('S_04.jsp')



@app.route('/S_05.jsp', methods=['POST', 'GET'])
def S_05():
    return render_template ('S_05.jsp')


@app.route('/S_07.jsp', methods=['POST', 'GET'])
def S_07():
    return render_template ('S_07.jsp')

@app.route('/S_08.jsp', methods=['POST', 'GET'])
def S_08():
    return render_template ('S_08.jsp')

@app.route('/S_09.jsp', methods=['POST', 'GET'])
def S_09():
    return render_template ('S_09.jsp')

@app.route('/S_10.jsp', methods=['POST', 'GET'])
def S_10():
    return render_template ('S_10.jsp')


@app.route('/S_14.jsp', methods=['POST', 'GET'])
def S_14():
    return render_template ('S_14.jsp')

@app.route('/S_19.jsp', methods=['POST', 'GET'])
def S_19():
    return render_template ('S_19.jsp')

@app.route('/S_22.jsp', methods=['POST', 'GET'])
def S_22():
    return render_template ('S_22.jsp')

@app.route('/S_16.jsp', methods=['POST', 'GET'])
def ambassador():
    return render_template ('S_16.jsp')

@app.route('/S_12.jsp', methods=['POST', 'GET'])
def giftSettings():
    return render_template ('S_12.jsp')


@app.route('/H_01.jsp', methods=['POST', 'GET'])
def accountactivity():
    return render_template ('H_01.jsp')


@app.route('/P_01.jsp', methods=['POST', 'GET'])
def P_01():
    return render_template ('P_01.jsp')

@app.route('/P_02.jsp', methods=['POST', 'GET'])
def P_02():
    return render_template ('P_02.jsp')


@app.route('/P_04.jsp', methods=['POST', 'GET'])
def P_04():
    return render_template ('P_04.jsp')

@app.route('/P_06.jsp', methods=['POST', 'GET'])
def P_06():
    return render_template ('P_06.jsp')

@app.route('/P_07.jsp',methods=['POST', 'GET'])
def P_07():
    return render_template ('P_07.jsp')


@app.route('/P_08.jsp',methods=['POST', 'GET'])
def P_08():
    return render_template ('P_08.jsp')



@app.route('/P_12.jsp', methods = ['POST','GET'])
def P_12():
    return render_template ('P_12.jsp')



@app.route('/P_15.jsp',methods=['POST', 'GET'])
def P_15():
    return render_template ('P_15.jsp')

@app.route('/B_01.jsp',methods=['POST', 'GET'])
def B_01():
    return render_template ('B_01.jsp')

@app.route('/B_02.jsp',methods=['POST', 'GET'])
def B_02():
    return render_template ('B_02.jsp')


@app.route('/B_05.jsp',methods=['POST', 'GET'])
def B_05():
    return render_template ('B_05.jsp')


@app.route('/B_06.jsp',methods=['POST', 'GET'])
def B_06():
    return render_template ('B_06.jsp')


@app.route('/B_07.jsp',methods=['POST', 'GET'])
def B_07():
    return render_template ('B_07.jsp')

@app.route('/B_08.jsp',methods=['POST', 'GET'])
def B_08():
    return render_template ('B_08.jsp')

@app.route('/B_09.jsp',methods=['POST', 'GET'])
def B_09():
    return render_template ('B_09.jsp')

@app.route('/B_10.jsp',methods=['POST', 'GET'])
def B_10():
    return render_template ('B_10.jsp')

@app.route('/B_17.jsp',methods=['POST', 'GET'])
def B_17():
    return render_template ('B_17.jsp')

@app.route('/B_18.jsp',methods=['POST', 'GET'])
def B_18():
    return render_template ('B_18.jsp')

@app.route('/B_19.jsp',methods=['POST', 'GET'])
def B_19():
    return render_template ('B_19.jsp')

@app.route('/B_21.jsp',methods=['POST', 'GET'])
def B_21():
    return render_template ('B_21.jsp')

@app.route('/B_22.jsp',methods=['POST', 'GET'])
def B_22():
    return render_template ('B_22.jsp')

@app.route('/B_23.jsp',methods=['POST', 'GET'])
def B_23():
    return render_template ('B_23.jsp')

@app.route('/B_24.jsp',methods=['POST', 'GET'])
def B_24():
    return render_template ('B_24.jsp')

@app.route('/B_25.jsp',methods=['POST', 'GET'])
def B_25():
    return render_template ('B_25.jsp')

@app.route('/B_26.jsp',methods=['POST', 'GET'])
def B_26():
    return render_template ('B_26.jsp')

@app.route('/B_27.jsp',methods=['POST', 'GET'])
def B_27():
    return render_template ('B_27.jsp')

@app.route('/B_28.jsp',methods=['POST', 'GET'])
def B_28():
    return render_template ('B_28.jsp')

@app.route('/B_29.jsp',methods=['POST', 'GET'])
def B_29():
    return render_template ('B_29.jsp')

@app.route('/B_30.jsp',methods=['POST', 'GET'])
def B_30():
    return render_template ('B_30.jsp')

@app.route('/B_31.jsp',methods=['POST', 'GET'])
def B_31():
    return render_template ('B_31.jsp')

@app.route('/B_32.jsp',methods=['POST', 'GET'])
def B_32():
    return render_template ('B_01.jsp')

@app.route('/B_03.jsp',methods=['POST', 'GET'])
def B_03():
    return render_template ('B_03.jsp')

@app.route('/B_16.jsp',methods=['POST', 'GET'])
def B_16():
    return render_template ('B_16.jsp')

@app.route('/F_03.jsp',methods=['POST', 'GET'])
def F_03():
    return render_template ('F_03.jsp')

@app.route('/H_02.jsp',methods=['POST', 'GET'])
def H_02():
    return render_template ('H_02.jsp')

@app.route('/H_03.jsp',methods=['POST', 'GET'])
def H_03():
    return render_template ('H_03.jsp')

@app.route('/H_04.jsp',methods=['POST', 'GET'])
def H_04():
    return render_template ('H_04.jsp')

@app.route('/L_01.jsp',methods=['POST', 'GET'])
def L_01():
    return render_template ('L_01.jsp')

@app.route('/L_02.jsp',methods=['POST', 'GET'])
def L_02():
    return render_template ('L_02.jsp')

@app.route('/L_03.jsp',methods=['POST', 'GET'])
def L_03():
    return render_template ('L_03.jsp')

@app.route('/L_04.jsp',methods=['POST', 'GET'])
def L_04():
    return render_template ('L_04.jsp')

@app.route('/M_01.jsp',methods=['POST', 'GET'])
def M_01():
    return render_template ('M_01.jsp')

@app.route('/W_02.jsp',methods=['POST', 'GET'])
def W_02():
    return render_template ('W_02.jsp')

@app.route('/W_02_1.jsp',methods=['POST', 'GET'])
def W_02_1():
    return render_template ('W_02_1.jsp')

@app.route('/W_04.jsp',methods=['POST', 'GET'])
def W_04():
    return render_template ('W_04.jsp')

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain('ssl/server.pem', 'ssl/server.key')
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=context)