"Micro Night Market" Merchant Touchscreen UI Interface V1.0
User Manual

# 1. Introduction
The purpose of this user manual is to comprehensively describe the functionalities and operating environment of this software, enabling users to understand its scope and methods of use, and providing necessary information for the maintenance and updates of the software.

# 2. Software Overview
2.1 Purpose of the Software
The main purpose of this software is to provide merchants with a touchscreen UI interface for managing their business. The following is a brief description of the main purposes of this software:
- Provides a secure login page where merchants can access the management interface by entering their username and password, ensuring that only authorized users can access the business management interface.
- Provides a main interface containing functions such as order management, shop management, environmental data, cultural community, and settings. Merchants can switch between different functional pages by clicking on corresponding buttons, facilitating efficient management of business operations.
- Merchants can view order details, including customer information, order contents, notes, and estimated completion time. Additionally, it provides functions for contacting customers and updating orders to adjust order statuses in real-time. Overall, this software aims to help merchants efficiently manage orders, inventory, monitor environmental data, and interact with customers to enhance business operations' efficiency and experience.

2.2 Software Operation
This software is designed to run on Raspberry Pi or other development boards installed with Linux operating systems (such as Raspbian). The software has been packaged into an executable program compatible with running on development boards like Raspberry Pi. To install the software on a Raspberry Pi, users can follow the standard software installation process. After installation, users can start the software by entering the appropriate command in the terminal or by clicking on the software icon in the graphical interface. Once launched, the software's login page will be displayed.

2.3 System Configuration
System requirements include installing the appropriate version of the Linux operating system, ensuring that the hardware configuration of the development board is sufficient to meet the software's operational requirements. Ensure that the Raspberry Pi or other development board is correctly connected and running, with a compatible Linux operating system installed. After installing the software, ensure that users have appropriate permissions to execute the software. Ensure that the computer has Python installed and install PyQt5 and related dependencies using the following command:
```
pip install PyQt5
```
Depending on the actual situation, it may be necessary to configure relevant dependencies and set the software's startup parameters.

2.4 Software Structure

# 3. Software Usage Process
3.1 Software Installation
Download the project source code.

3.2 Software Usage Flowchart
3.2.1 Startup
1. Download and extract the software source code.
2. Open the command line or terminal and navigate to the software's root directory.
3. Run the following command to start the software:
```
python main.py
```
4. Enter the login interface.
5. Input the account password and click the login button.
6. The main interface includes functions such as order management, shop management, environmental data, cultural community, and settings.
7. Clicking on different buttons switches to the corresponding functional pages.
8. Order management page: The top of the page displays order-related information, and the bottom has buttons for contacting customers and updating orders.
    - Orders can be displayed by generating order information through code.
    - Clicking on the contact customer button displays the customer's phone number.
    - Clicking on the update order button retrieves the latest order data.
    - Clicking on the complete order button updates the order status on the server.
    - Merchants can select the estimated completion time and submit it.
9. Shop management interface:
    - The sales information display section primarily shows relevant information about orders.
    - The inventory management section displays the shop's inventory information.
    - The system automatically refreshes the order flow and inventory information on the page regularly, maintaining data timeliness. Merchants can adjust their business strategies based on this information.
10. Environmental data page:
    - The top of the page displays weather information.
    - The middle section displays real-time sensor data.
    - Relevant data can be retrieved and displayed by calling APIs.
11. Cultural community page:
    - Displays cultural-related content posted by users, each post includes the poster's nickname, posting time, content text, number of likes, etc. The number of likes is updated in real-time, and comments will be displayed below the content. Content moderation is required to filter out inappropriate content.
12. Settings page introduction:
    - Account settings, notification settings, about us.
    - Users can set their username, password, phone number, etc. When clicking on an input box, an input panel will pop up. After modification, users need to click the save button to submit the changes.
