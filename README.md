# Fanuc-Cobot

### Overview
- This temporary repository contains a OpenTAP prototype plugin for Fanuc's CRX-20iA/L collaborative robot.
- The prototype demonstrates how teams can leverage OpenTAP's automation capabilities to streamline repetitive and minor tasks associated with test and measurement.
- This plugin was developed using Fanuc's ROBOGUIDE simulator as a proof of concept. While the design should extrapolate to a physical robot, additional field testing will likely be necessary.

### Demo
Moving the CRX-20iA/L programatically with OpenTAP.
  
<kbd>![fanuc_demo](https://user-images.githubusercontent.com/80125540/236565884-c15f7dab-2ed4-4590-be3e-899b3a7b7999.gif)</kbd>


## Setup

### Requirements
- [Python](https://www.python.org/downloads/)
- [OpenTAP](https://opentap.io/downloads)
- [ROBOGUIDE simulator licences](https://www.fanucamerica.com/products/robots/robot-simulation-software-FANUC-ROBOGUIDE) or Fanuc's physical CRX-20iA/L model
- [Git](https://git-scm.com/downloads)

### Robot Setup
1. Open ROBOGUIDE and create a new work cell with the following actions:
     
   <kbd>![create_Workcell](https://user-images.githubusercontent.com/80125540/236600907-16e3b860-8fc9-4fb0-8408-29f5a6bb7f66.gif)</kbd>
   1. Select **HandlingPRO** then **Next**
   2. Select **Next**
   3. Select **Next**
   4. Select **Next**
   5. Select robot model **CRX-20iA/L** then **Next**
   6. Select **Next**
   7. Select **R632**, **R566** and **R648** from software options then **Next**
   8. Select **Finish** to start the robot controller
   
2. Configure the teach pendant with the following actions:
     
   <kbd>![setup_tp](https://user-images.githubusercontent.com/80125540/236606061-7839e319-f33a-4184-a838-f18c226775cb.gif)</kbd>
   1. Open the Teach Pendant by click on the following icon.
       
       <kbd>![image](https://user-images.githubusercontent.com/80125540/235309815-95141091-f7f5-49e2-89af-d3b497f1b6b6.png)</kbd>

   2. Open the setup menu by clicking the menu button.
        
       <kbd>![image](https://user-images.githubusercontent.com/80125540/235309749-569021d2-1a9c-419a-a6a6-2c4db3e7c340.png)</kbd>
   
   3. Click throgh the setup options as you see fit but ensure you choose **Continue with Guidance** and **Connect to Network** when prompted.
   
   4. Cycle the power when you've finished.
   
3. Load the KAREL server script with the following actions:
     
   <kbd>![build_karel](https://user-images.githubusercontent.com/80125540/236607697-25302285-1197-4ce2-8223-c69d80e1c813.gif)</kbd>
   1. x
   2. y

4. Create the server tag with the following actions:
     
   <kbd>![server_tag](https://user-images.githubusercontent.com/80125540/236607777-cff38654-cf97-42cf-8edf-25226cd5bbbd.gif)</kbd>
   1. x
   2. y
   
5. Load and run the KAREL program with the following actions:
     
   <kbd>![start_server](https://user-images.githubusercontent.com/80125540/236607967-ba88f5e6-57b5-491d-ba11-785ded07eb61.gif)</kbd>
   1. x
   2. y

### OpenTAP Setup
1. If you haven't already, install OpenTAP.
2. Downlaod the CRX-20iA plugin package. Save it in OpenTAP's root directory at the lcoation you installed it. 
3. Open a console and navigate to OpenTAP's root directory. Run the following commands to ensure you have the required plugins.
     
   ```Console
   tap package install editorx
   tap package install Python
   tap package install CRX-20iA
   ```
4. Launch Keysight's Pathwave editor by running the following command in the same directory:
     
   ```Console
   tap editorx
   ```

## Usage

### Create a test plan
details go here


## Technical Details

### High Level Architecture
  
<kbd>![Untitled Diagram (2)](https://user-images.githubusercontent.com/80125540/236608182-5ea98b83-f4b6-4ed0-a743-53e6c81e85e5.jpg)</kbd>

