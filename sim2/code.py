# importing essential modules that provides functions 
# to interact with the operating system
import os,sys
# from cv2 import ROTATE_90_COUNTERCLOCKWISE
import traci
import traci.constants as tc
import sumolib
# from collections import Counter
        # setting the path in environment variables 
if 'SUMO_HOME' in os.environ:
    tools= os.path.join(os.environ['SUMO_HOME'],'tools')
    sys.path.append(tools) 
else:
    sys.exit("Declare environment variable 'SUMO_HOME'")

        
def runSimulation():
    # traci.load(["sumo-gui","-c", "sim2.sumocfg"])
    sumoCMD= ["sumo-gui", "-c", "sim2.sumocfg"]
    traci.start(sumoCMD)

    while traci.simulation.getMinExpectedNumber()>0:
        traci.simulationStep

def step():
    s= traci.simulation.getTime() 
    traci.simulationStep()
    return s

def posToString(pos):
    if pos[0]==tc.INVALID_DOUBLE_VALUE:
        return "invalid"
    else:
        return str(pos)


def check(vehID):
    print("All vehicles==",traci.vehicle.getIDList())
    print("Vehicle count==", traci.vehicle.getIDCount()) 
    print("examining==", vehID)  
    print ("position==",posToString(traci.vehicle.getPosition(vehID)))
    print("road==", traci.vehicle.getRoadID(vehID))
    print("route==",traci.vehicle.getRouteID(vehID))
    print("waiting time==",traci.vehicle.getWaitingTime(vehID))
    print("acc waiting time==",traci.vehicle.getAccumulatedWaitingTime(vehID))
    print("travel time==",traci.vehicle.getAdaptedTraveltime(vehID,0,"1o"))

def run():
    step=0
    timeline=[]
    sumoCMD= ["sumo-gui", "-c", "sim2.sumocfg"]
    traci.start(sumoCMD)
    
    

    while step<1000:
        traci.simulationStep()
        vehicles=traci.vehicle.getIDList()
        timeline.append({})
        s=traci.simulation.getTime()
        
        e0=traci.edge.getLastStepVehicleNumber("E0")

        e1=traci.edge.getLastStepVehicleNumber("E1")
        e2=traci.edge.getLastStepVehicleNumber("E2")
        e3=traci.edge.getLastStepVehicleNumber("E3")
        em0=traci.edge.getLastStepVehicleNumber("-E0")
        em1=traci.edge.getLastStepVehicleNumber("-E1")
        em2=traci.edge.getLastStepVehicleNumber("-E2")
        em3=traci.edge.getLastStepVehicleNumber("-E3")
        traffic=traci.trafficlight.getRedYellowGreenState("J1")
        # print(e0)


        
        for v in vehicles:
            # timeline[-1][v]=traci.vehicle.getSpeed(v)
            e0=traci.edge.getLastStepVehicleNumber("E0")
            e1=traci.edge.getLastStepVehicleNumber("E1")
            e2=traci.edge.getLastStepVehicleNumber("E2")
            e3=traci.edge.getLastStepVehicleNumber("E3")
            em0=traci.edge.getLastStepVehicleNumber("-E0")
            em1=traci.edge.getLastStepVehicleNumber("-E1")
            em2=traci.edge.getLastStepVehicleNumber("-E2")
            em3=traci.edge.getLastStepVehicleNumber("-E3")
        
            if s==37.2:
                traffic=traci.trafficlight.getRedYellowGreenState("J1")
            print("traffic state----",traffic)
        
        step=step+1
        print("---------------------------------------------------------------")
        print("step_per_time",s)
        print("vehicles list==",vehicles)
    # print("timeline==",timeline)
        vehnum=len(vehicles)
        print("edge0=====",e0)
        print("edge1=====",e1)
        print("edge2=====",e2)
        print("edge3=====",e3)
        print("edgem0=====",em0)
        print("edgem1=====",em1)
        print("edgem2=====",em2)
        print("edgem3=====",em3)
        print("number of vehicles===",vehnum)
        
        
        
    traci.close()
    return timeline


run()


# while 1:
#  count=traci.edge.getLastStepVehicleNumber("E0")
#  print(count)
#  step+=1

# traci.close(False)