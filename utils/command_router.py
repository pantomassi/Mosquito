""" {drone.drone} commands are original Djitellopy methods, the other are Mosquito's own.
"""

from utils.voice_num_to_int import voice_num_to_int


AIRBORNE_COMMANDS = ('emergency', 'land', 'keep', 'go', 'turn', 'flip', 'set')


def process_static_command(drone, command):
    if command[0] == 'battery':
        print(f"Battery: {drone.drone.get_battery()}%")
    elif command[0] == 'altitude':
        print(f"The drone is {drone.drone.get_height()}cm above the ground.")
    elif command[0] == 'temp':
        print(f"Temperature: {drone.drone.get_temperature()} C")
    elif command[0] == 'picture':
        drone.screenshot()
    elif command[0] == 'video':
        drone.start_video()
    # elif ' '.join(command[:2]) == 'stop video':
    #     drone.stop_video()
    elif ' '.join(command[:2]) == 'take off':
        drone.drone.takeoff()



def process_airborne_command(drone, command):
    direction = ''
    measurement = 0

    if len(command) > 1:
        direction = command[1]
    if len(command) > 2:
        measurement = voice_num_to_int(command[2:])

    if command[0] == 'emergency':
        drone.drone.emergency()
    elif command[0] == 'land':
        drone.drone.land()
    elif " ".join(command[:2]) == 'set speed':
        drone.set_speed(measurement)
    elif command[0] == 'flip':
        drone.flip(direction)
    elif command[0] == 'go':
        drone.go(direction, measurement)
    elif command[0] == 'turn':
        drone.turn(direction, measurement)
    else:
        print("[!] Command incomplete.")



def command_router(drone, command):
    try:

        if command[0] == 'empty':
            if drone.drone.is_flying == True:
                drone.keep_alive_turn()  # Prevent auto-landing after 15s of no actions by Tello
            else:
                pass

        elif command[0] == 'invalid':
            print(f'[Invalid operation] Command \"{" ".join(command)}\" is invalid. Please try again.')

        elif command[0] == 'exit':
            return drone.drone.__del__()

        elif command[0] in AIRBORNE_COMMANDS:
            if drone.drone.is_flying == True:
                process_airborne_command(drone, command)
            else:
                print("*The drone needs to be in the air to make any kind of movement or to set speed*")
                pass
            
        else:
            process_static_command(drone, command)

    except Exception as e:
        print(f'[PROCESSING ERROR] Details: {e.__class__.__name__} / {e}')



# Start propellers when grounded - without taking off - to cool the drone down. It overheats when on & not flying. Disconnects also happen more often due to overheating than low battery. !! This doesn't seem to work for me despite updated firmware --> "command 'motoron' not found"
# if command == "cool":
#     drone.drone.send_command_with_return("motoron")
# elif command == "cool stop":
#     drone.drone.send_command_with_return("motoroff")